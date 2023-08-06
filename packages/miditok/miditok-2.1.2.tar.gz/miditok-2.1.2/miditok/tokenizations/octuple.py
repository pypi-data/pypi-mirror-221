from math import ceil
from pathlib import Path
from typing import List, Tuple, Dict, Optional, Union, Any

import numpy as np
from miditoolkit import MidiFile, Instrument, Note, TempoChange, TimeSignature

from ..midi_tokenizer import MIDITokenizer, _in_as_seq, _out_as_complete_seq
from ..classes import TokSequence, Event
from ..constants import (
    TIME_DIVISION,
    TIME_SIGNATURE,
    TEMPO,
    MIDI_INSTRUMENTS,
)


class Octuple(MIDITokenizer):
    r"""Introduced with `MusicBert (Zeng et al.) <https://arxiv.org/abs/2106.05630>`_,
    the idea of Octuple is to use embedding pooling so that each pooled embedding
    represents a single note. Tokens (*Pitch*, *Velocity*...) are first independently
    converted to embeddings which are then merged (pooled) into a single one.
    Each pooled token will be a list of the form (index: Token type):
    * 0: Pitch
    * 1: Velocity
    * 2: Duration
    * 3: Program (track)
    * 4: Position
    * 5: Bar
    * (+ Optional) Tempo
    * (+ Optional) TimeSignature

    Its considerably reduces the sequence lengths, while handling multitrack.
    The output hidden states of the model will then be fed to several output layers
    (one per token type). This means that the training requires to add multiple losses.
    For generation, the decoding implies sample from several distributions, which can be
    very delicate. Hence, we do not recommend this tokenization for generation with small models.

    **Notes:**
    * Tokens are first sorted by time, then track, then pitch values.
    * Tracks with the same *Program* will be merged.
    """

    def _tweak_config_before_creating_voc(self):
        self.config.use_chords = False
        self.config.use_rests = False
        self.one_token_stream = True

        # used in place of positional encoding
        # This attribute might increase over tokenizations, if the tokenizer encounter longer MIDIs
        if "max_bar_embedding" not in self.config.additional_params:
            self.config.additional_params["max_bar_embedding"] = 60

        token_types = ["Pitch", "Velocity", "Duration", "Program", "Position", "Bar"]
        if self.config.use_tempos:
            token_types.append("Tempo")
        if self.config.use_time_signatures:
            token_types.append("TimeSignature")
        self.vocab_types_idx = {
            type_: idx for idx, type_ in enumerate(token_types)
        }  # used for data augmentation

    @_out_as_complete_seq
    def _midi_to_tokens(self, midi: MidiFile, *args, **kwargs) -> TokSequence:
        r"""Override the parent class method
        Converts a MIDI file in a token representation, a sequence of "time steps".
        A time step is a list of tokens where:
            (list index: token type)
            0: Pitch
            1: Velocity
            2: Duration
            3: Program (track)
            4: Position
            5: Bar
            (6: Tempo)
            (7: TimeSignature)

        :param midi: the MIDI object to convert
        :return: sequences of tokens
        """
        # Check bar embedding limit, update if needed
        nb_bars = ceil(midi.max_tick / (midi.ticks_per_beat * 4))
        if self.config.additional_params["max_bar_embedding"] < nb_bars:
            for i in range(self.config.additional_params["max_bar_embedding"], nb_bars):
                self.add_to_vocab(f"Bar_{i}", 5)
            self.config.additional_params["max_bar_embedding"] = nb_bars

        # Convert each track to tokens
        tokens = []
        for track in midi.instruments:
            if track.program in self.config.programs:
                tokens += self.track_to_tokens(track)

        tokens.sort(
            key=lambda x: (x[0].time, x[0].desc, x[0].value)
        )  # Sort by time, then track, then pitch

        # Convert pitch events into tokens
        for time_step in tokens:
            time_step[0] = str(time_step[0])

        return TokSequence(tokens=tokens)

    def track_to_tokens(self, track: Instrument) -> List[List[Union[Event, str]]]:
        r"""Converts a track (miditoolkit.Instrument object) into a sequence of tokens (:class:`miditok.TokSequence`).
        A time step is a list of tokens where:
            (list index: token type)
            0: Pitch (as an Event object for sorting purpose afterwards)
            1: Velocity
            2: Duration
            3: Program (track)
            4: Position
            5: Bar
            (6: Tempo)
            (7: TimeSignature)

        :param track: track object to convert
        :return: sequence of corresponding tokens
        """
        # Make sure the notes are sorted first by their onset (start) times, second by pitch
        # notes.sort(key=lambda x: (x.start, x.pitch))  # done in midi_to_tokens
        time_division = self._current_midi_metadata["time_division"]
        ticks_per_sample = time_division / max(self.config.beat_res.values())
        dur_bins = self._durations_ticks[time_division]

        tokens = []
        current_tick = -1
        current_bar = -1
        current_pos = -1
        current_tempo_idx = 0
        current_tempo = self._current_midi_metadata["tempo_changes"][
            current_tempo_idx
        ].tempo
        current_time_sig_idx = 0
        current_time_sig_tick = 0
        current_time_sig_bar = 0
        time_sig_change = self._current_midi_metadata["time_sig_changes"][
            current_time_sig_idx
        ]
        current_time_sig = self._reduce_time_signature(
            time_sig_change.numerator, time_sig_change.denominator
        )
        ticks_per_bar = time_division * current_time_sig[0]

        for note in track.notes:
            # Positions and bars
            if note.start != current_tick:
                pos_index = int(
                    ((note.start - current_time_sig_tick) % ticks_per_bar)
                    / ticks_per_sample
                )
                current_tick = note.start
                current_bar = (
                    current_time_sig_bar
                    + (current_tick - current_time_sig_tick) // ticks_per_bar
                )
                current_pos = pos_index

            # Note attributes
            duration = note.end - note.start
            dur_index = np.argmin(np.abs(dur_bins - duration))
            token = [
                Event(
                    type="Pitch",
                    value=note.pitch,
                    time=note.start,
                    desc=-1 if track.is_drum else track.program,
                ),
                f"Velocity_{note.velocity}",
                f'Duration_{".".join(map(str, self.durations[dur_index]))}',
                f"Program_{-1 if track.is_drum else track.program}",
                f"Position_{current_pos}",
                f"Bar_{current_bar}",
            ]

            # (Tempo)
            if self.config.use_tempos:
                # If the current tempo is not the last one
                if current_tempo_idx + 1 < len(
                    self._current_midi_metadata["tempo_changes"]
                ):
                    # Will loop over incoming tempo changes
                    for tempo_change in self._current_midi_metadata["tempo_changes"][
                        current_tempo_idx + 1 :
                    ]:
                        # If this tempo change happened before the current moment
                        if tempo_change.time <= note.start:
                            current_tempo = tempo_change.tempo
                            current_tempo_idx += (
                                1  # update tempo value (might not change) and index
                            )
                        elif tempo_change.time > note.start:
                            break  # this tempo change is beyond the current time step, we break the loop
                token.append(f"Tempo_{current_tempo}")

            # (TimeSignature)
            if self.config.use_time_signatures:
                # If the current time signature is not the last one
                if current_time_sig_idx + 1 < len(
                    self._current_midi_metadata["time_sig_changes"]
                ):
                    # Will loop over incoming time signature changes
                    for time_sig_change in self._current_midi_metadata[
                        "time_sig_changes"
                    ][current_time_sig_idx + 1 :]:
                        # If this time signature change happened before the current moment
                        if time_sig_change.time <= note.start:
                            current_time_sig = self._reduce_time_signature(
                                time_sig_change.numerator, time_sig_change.denominator
                            )
                            current_time_sig_idx += 1  # update time signature value (might not change) and index
                            current_time_sig_bar += (
                                time_sig_change.time - current_time_sig_tick
                            ) // ticks_per_bar
                            current_time_sig_tick = time_sig_change.time
                            ticks_per_bar = time_division * current_time_sig[0]
                        elif time_sig_change.time > note.start:
                            break  # this time signature change is beyond the current time step, we break the loop
                token.append(f"TimeSig_{current_time_sig[0]}/{current_time_sig[1]}")

            tokens.append(token)

        return tokens

    @_in_as_seq()
    def tokens_to_midi(
        self,
        tokens: Union[TokSequence, List, np.ndarray, Any],
        _=None,
        output_path: Optional[str] = None,
        time_division: Optional[int] = TIME_DIVISION,
    ) -> MidiFile:
        r"""Override the parent class method
        Convert multiple sequences of tokens into a multitrack MIDI and save it.
        The tokens will be converted to event objects and then to a miditoolkit.MidiFile object.
        A time step is a list of tokens where (list index: token type):
        * 0: Pitch
        * 1: Velocity
        * 2: Duration
        * 3: Program (track)
        * 4: Position
        * 5: Bar
        * (6: Tempo)
        * (7: TimeSignature)
        :param tokens: tokens to convert. Can be either a Tensor (PyTorch and Tensorflow are supported),
                a numpy array, a Python list or a TokSequence.
        :param _: unused, to match parent method signature
        :param output_path: path to save the file (with its name, e.g. music.mid),
                        leave None to not save the file
        :param time_division: MIDI time division / resolution, in ticks/beat (of the MIDI to create)
        :return: the midi object (miditoolkit.MidiFile)
        """
        assert (
            time_division % max(self.config.beat_res.values()) == 0
        ), f"Invalid time division, please give one divisible by {max(self.config.beat_res.values())}"
        midi = MidiFile(ticks_per_beat=time_division)
        ticks_per_sample = time_division // max(self.config.beat_res.values())
        tokens = tokens.tokens

        tempo_changes = [TempoChange(TEMPO, 0)]
        if self.config.use_tempos:
            for i in range(len(tokens)):
                if tokens[i][6].split("_")[1] != "None":
                    tempo_changes = [TempoChange(int(tokens[i][6].split("_")[1]), 0)]
                    break

        time_sig = TIME_SIGNATURE
        if self.config.use_time_signatures:
            for i in range(len(tokens)):
                if tokens[i][-1].split("_")[1] != "None":
                    time_sig = self._parse_token_time_signature(
                        tokens[i][-1].split("_")[1]
                    )
                    break

        ticks_per_bar = time_division * time_sig[0]
        time_sig_changes = [TimeSignature(*time_sig, 0)]

        current_time_sig_tick = 0
        current_time_sig_bar = 0

        tracks = dict([(n, []) for n in self.config.programs])
        for time_step in tokens:
            if any(tok.split("_")[1] == "None" for tok in time_step[:6]):
                continue  # Either padding, mask: error of prediction or end of sequence anyway

            # Note attributes
            pitch = int(time_step[0].split("_")[1])
            vel = int(time_step[1].split("_")[1])
            duration = self._token_duration_to_ticks(
                time_step[2].split("_")[1], time_division
            )

            # Time and track values
            program = int(time_step[3].split("_")[1])
            current_pos = int(time_step[4].split("_")[1])
            current_bar = int(time_step[5].split("_")[1])
            current_tick = (
                current_time_sig_tick
                + (current_bar - current_time_sig_bar) * ticks_per_bar
                + current_pos * ticks_per_sample
            )

            # Append the created note
            tracks[program].append(
                Note(vel, pitch, current_tick, current_tick + duration)
            )

            # Tempo, adds a TempoChange if necessary
            if self.config.use_tempos and time_step[6].split("_")[1] != "None":
                tempo = int(time_step[6].split("_")[1])
                if tempo != tempo_changes[-1].tempo:
                    tempo_changes.append(TempoChange(tempo, current_tick))

            # Time Signature, adds a TimeSignatureChange if necessary
            if (
                self.config.use_time_signatures
                and time_step[-1].split("_")[1] != "None"
            ):
                time_sig = self._parse_token_time_signature(time_step[-1].split("_")[1])
                if time_sig != (
                    time_sig_changes[-1].numerator,
                    time_sig_changes[-1].denominator,
                ):
                    current_time_sig_tick += (
                        current_bar - current_time_sig_bar
                    ) * ticks_per_bar
                    current_time_sig_bar = current_bar
                    ticks_per_bar = time_division * time_sig[0]
                    time_sig_changes.append(
                        TimeSignature(*time_sig, current_time_sig_tick)
                    )

        # Tempos
        midi.tempo_changes = tempo_changes

        # Time Signatures
        midi.time_signature_changes = time_sig_changes

        # Appends created notes to MIDI object
        for program, notes in tracks.items():
            if len(notes) == 0:
                continue
            if int(program) == -1:
                midi.instruments.append(Instrument(0, True, "Drums"))
            else:
                midi.instruments.append(
                    Instrument(
                        int(program), False, MIDI_INSTRUMENTS[int(program)]["name"]
                    )
                )
            midi.instruments[-1].notes = notes

        # Write MIDI file
        if output_path:
            Path(output_path).mkdir(parents=True, exist_ok=True)
            midi.dump(output_path)
        return midi

    def tokens_to_track(
        self,
        tokens: TokSequence,
        time_division: Optional[int] = TIME_DIVISION,
        program: Optional[Tuple[int, bool]] = (0, False),
    ) -> Tuple[Instrument, List[TempoChange]]:
        r"""NOT RELEVANT / IMPLEMENTED FOR OCTUPLE
        Use tokens_to_midi instead

        :param tokens: sequence of tokens to convert. Can be either a Tensor (PyTorch and Tensorflow are supported),
                a numpy array, a Python list or a TokSequence.
        :param time_division: MIDI time division / resolution, in ticks/beat (of the MIDI to create)
        :param program: the MIDI program of the produced track and if it drum, (default (0, False), piano)
        :return: the miditoolkit instrument object and tempo changes
        """
        pass

    def _create_base_vocabulary(self) -> List[List[str]]:
        r"""Creates the vocabulary, as a list of string tokens.
        Each token as to be given as the form of "Type_Value", separated with an underscore.
        Example: Pitch_58
        The :class:`miditok.MIDITokenizer` main class will then create the "real" vocabulary as
        a dictionary.
        Special tokens have to be given when creating the tokenizer, and
        will be added to the vocabulary by :class:`miditok.MIDITokenizer`.

        :return: the vocabulary as a list of string.
        """
        vocab = [[] for _ in range(6)]

        # PITCH
        vocab[0] += [f"Pitch_{i}" for i in range(*self.config.pitch_range)]

        # VELOCITY
        vocab[1] += [f"Velocity_{i}" for i in self.velocities]

        # DURATION
        vocab[2] += [
            f'Duration_{".".join(map(str, duration))}' for duration in self.durations
        ]

        # PROGRAM
        vocab[3] += [f"Program_{i}" for i in self.config.programs]

        # POSITION
        nb_positions = max(self.config.beat_res.values()) * 4  # 4/4 time signature
        vocab[4] += [f"Position_{i}" for i in range(nb_positions)]

        # BAR (positional encoding)
        vocab[5] += [
            f"Bar_{i}"
            for i in range(self.config.additional_params["max_bar_embedding"])
        ]

        # TEMPO
        if self.config.use_tempos:
            vocab.append([f"Tempo_{i}" for i in self.tempos])

        # TIME_SIGNATURE
        if self.config.use_time_signatures:
            vocab.append([f"TimeSig_{i[0]}/{i[1]}" for i in self.time_signatures])

        return vocab

    def _create_token_types_graph(self) -> Dict[str, List[str]]:
        r"""Returns a graph (as a dictionary) of the possible token
        types successions.
        Not relevant for Octuple.

        :return: the token types transitions dictionary
        """
        return {}  # not relevant for this encoding

    @_in_as_seq()
    def tokens_errors(self, tokens: Union[TokSequence, List, np.ndarray, Any]) -> float:
        r"""Checks if a sequence of tokens is made of good token values and
        returns the error ratio (lower is better).
        The token types are always the same in Octuple so this methods only checks
        if their values are correct:
            - a bar token value cannot be < to the current bar (it would go back in time)
            - same for positions
            - a pitch token should not be present if the same pitch is already played at the current position

        :param tokens: sequence of tokens to check
        :return: the error ratio (lower is better)
        """
        err = 0
        current_bar = current_pos = -1
        current_pitches = {p: [] for p in self.config.programs}

        for token in tokens.tokens:
            if any(tok.split("_")[1] == "None" for tok in token):
                err += 1
                continue
            has_error = False
            bar_value = int(token[5].split("_")[1])
            pos_value = int(token[4].split("_")[1])
            pitch_value = int(token[0].split("_")[1])
            program_value = int(token[3].split("_")[1])

            # Bar
            if bar_value < current_bar:
                has_error = True
            elif bar_value > current_bar:
                current_bar = bar_value
                current_pos = -1
                current_pitches = {p: [] for p in self.config.programs}

            # Position
            if pos_value < current_pos:
                has_error = True
            elif pos_value > current_pos:
                current_pos = pos_value
                current_pitches = {p: [] for p in self.config.programs}

            # Pitch
            if pitch_value in current_pitches[program_value]:
                has_error = True
            else:
                current_pitches[program_value].append(pitch_value)

            if has_error:
                err += 1

        return err / len(tokens)
