from math import ceil
from typing import List, Tuple, Dict, Optional, Union, Any

import numpy as np
from miditoolkit import Instrument, Note, TempoChange

from ..midi_tokenizer import MIDITokenizer, _in_as_seq, _out_as_complete_seq
from ..classes import TokSequence
from ..constants import (
    TIME_DIVISION,
    TEMPO,
    MIDI_INSTRUMENTS,
)


class OctupleMono(MIDITokenizer):
    r"""OctupleMono is similar to :ref:`Octuple`
    (`MusicBert (Zeng et al.) <https://arxiv.org/abs/2106.05630>`_) but without the
    *Program* token. OctupleMono is hence better suited for tasks with one track.
    Each pooled token will be a list of the form (index: Token type):
    * 0: Pitch
    * 1: Velocity
    * 2: Duration
    * 3: Position
    * 4: Bar
    * (+ Optional) Tempo
    * (+ Optional) TimeSignature
    """

    def _tweak_config_before_creating_voc(self):
        self.config.use_chords = False
        self.config.use_rests = False
        self.config.use_programs = False

        # used in place of positional encoding
        # This attribute might increase over tokenizations, if the tokenizer encounter longer MIDIs
        if "max_bar_embedding" not in self.config.additional_params:
            self.config.additional_params["max_bar_embedding"] = 60

        token_types = ["Pitch", "Velocity", "Duration", "Position", "Bar"]
        if self.config.use_tempos:
            token_types.append("Tempo")
        if self.config.use_time_signatures:
            token_types.append("TimeSignature")
        self.vocab_types_idx = {
            type_: idx for idx, type_ in enumerate(token_types)
        }  # used for data augmentation

    @_out_as_complete_seq
    def track_to_tokens(self, track: Instrument) -> TokSequence:
        r"""Converts a track (miditoolkit.Instrument object) into a sequence of tokens (:class:`miditok.TokSequence`).
        A time step is a list of tokens where:
            (list index: token type)
            0: Pitch
            1: Velocity
            2: Duration
            4: Position
            5: Bar
            (6: Tempo)

        :param track: MIDI track to convert
        :return: :class:`miditok.TokSequence` of corresponding tokens.
        """
        # Make sure the notes are sorted first by their onset (start) times, second by pitch
        # notes.sort(key=lambda x: (x.start, x.pitch))  # done in midi_to_tokens
        ticks_per_sample = self._current_midi_metadata["time_division"] / max(
            self.config.beat_res.values()
        )
        ticks_per_bar = self._current_midi_metadata["time_division"] * 4
        dur_bins = self._durations_ticks[self._current_midi_metadata["time_division"]]

        # Check bar embedding limit, update if needed
        nb_bars = ceil(
            max(note.end for note in track.notes)
            / (self._current_midi_metadata["time_division"] * 4)
        )
        if self.config.additional_params["max_bar_embedding"] < nb_bars:
            for i in range(self.config.additional_params["max_bar_embedding"], nb_bars):
                self.add_to_vocab(f"Bar_{i}", 4)
            self.config.additional_params["max_bar_embedding"] = nb_bars

        tokens = []
        current_tick = -1
        current_bar = -1
        current_pos = -1
        current_tempo_idx = 0
        current_tempo = self._current_midi_metadata["tempo_changes"][
            current_tempo_idx
        ].tempo
        for note in track.notes:
            # Positions and bars
            if note.start != current_tick:
                pos_index = int((note.start % ticks_per_bar) / ticks_per_sample)
                current_tick = note.start
                current_bar = current_tick // ticks_per_bar
                current_pos = pos_index

            # Note attributes
            duration = note.end - note.start
            dur_index = np.argmin(np.abs(dur_bins - duration))
            token_ts = [
                f"Pitch_{note.pitch}",
                f"Velocity_{note.velocity}",
                f'Duration_{".".join(map(str, self.durations[dur_index]))}',
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
                token_ts.append(f"Tempo_{current_tempo}")

            tokens.append(token_ts)

        return TokSequence(tokens=tokens)

    def tokens_to_track(
        self,
        tokens: TokSequence,
        time_division: Optional[int] = TIME_DIVISION,
        program: Optional[Tuple[int, bool]] = (0, False),
    ) -> Tuple[Instrument, List[TempoChange]]:
        r"""Converts a sequence of tokens into a track object
        A time step is a list of tokens where:
            (list index: token type)
            0: Pitch
            1: Velocity
            2: Duration
            4: Position
            5: Bar
            (+ TimeSignature)
            (+ Tempo)

        :param tokens: sequence of tokens to convert. Can be either a Tensor (PyTorch and Tensorflow are supported),
                a numpy array, a Python list or a TokSequence.
        :param time_division: MIDI time division / resolution, in ticks/beat (of the MIDI to create)
        :param program: the MIDI program of the produced track and if it drum, (default (0, False), piano)
        :return: the miditoolkit instrument object and tempo changes
        """
        assert (
            time_division % max(self.config.beat_res.values()) == 0
        ), f"Invalid time division, please give one divisible by {max(self.config.beat_res.values())}"
        tokens = tokens.tokens

        ticks_per_sample = time_division // max(self.config.beat_res.values())
        name = "Drums" if program[1] else MIDI_INSTRUMENTS[program[0]]["name"]
        instrument = Instrument(program[0], is_drum=program[1], name=name)

        tempo_changes = [TempoChange(TEMPO, 0)]
        if self.config.use_tempos:
            for i in range(len(tokens)):
                if tokens[i][-1].split("_")[1] != "None":
                    tempo_changes = [TempoChange(int(tokens[i][-1].split("_")[1]), 0)]
                    break

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
            current_pos = int(time_step[3].split("_")[1])
            current_bar = int(time_step[4].split("_")[1])
            current_tick = (
                current_bar * time_division * 4 + current_pos * ticks_per_sample
            )

            # Append the created note
            instrument.notes.append(
                Note(vel, pitch, current_tick, current_tick + duration)
            )

            # Tempo, adds a TempoChange if necessary
            if self.config.use_tempos and time_step[-1].split("_")[1] != "None":
                tempo = int(time_step[-1].split("_")[1])
                if tempo != tempo_changes[-1].tempo:
                    tempo_changes.append(TempoChange(tempo, current_tick))

        return instrument, tempo_changes

    def _create_base_vocabulary(self, sos_eos_tokens: bool = None) -> List[List[str]]:
        r"""Creates the vocabulary, as a list of string tokens.
        Each token as to be given as the form of "Type_Value", separated with an underscore.
        Example: Pitch_58
        The :class:`miditok.MIDITokenizer` main class will then create the "real" vocabulary as
        a dictionary.
        Special tokens have to be given when creating the tokenizer, and
        will be added to the vocabulary by :class:`miditok.MIDITokenizer`.

        :return: the vocabulary as a list of string.
        """
        vocab = [[] for _ in range(5)]

        # PITCH
        vocab[0] += [f"Pitch_{i}" for i in range(*self.config.pitch_range)]

        # VELOCITY
        vocab[1] += [f"Velocity_{i}" for i in self.velocities]

        # DURATION
        vocab[2] += [
            f'Duration_{".".join(map(str, duration))}' for duration in self.durations
        ]

        # POSITION
        nb_positions = max(self.config.beat_res.values()) * 4  # 4/4 time signature
        vocab[3] += [f"Position_{i}" for i in range(nb_positions)]

        # BAR
        vocab[4] += [
            f"Bar_{i}"
            for i in range(self.config.additional_params["max_bar_embedding"])
        ]  # bar embeddings (positional encoding)

        # TEMPO
        if self.config.use_tempos:
            vocab.append([f"Tempo_{i}" for i in self.tempos])

        return vocab

    def _create_token_types_graph(self) -> Dict[str, List[str]]:
        r"""Returns a graph (as a dictionary) of the possible token
        types successions.
        Not relevant for Octuple.

        :return: the token types transitions dictionary
        """
        return {}  # not relevant for this encoding

    @_in_as_seq()
    def tokens_errors(
        self, tokens: Union[TokSequence, List, np.ndarray, Any]
    ) -> Union[float, List[float]]:
        r"""Checks if a sequence of tokens is made of good token values and
        returns the error ratio (lower is better).
        The token types are always the same in Octuple so this method only checks
        if their values are correct:
            - a bar token value cannot be < to the current bar (it would go back in time)
            - same for positions
            - a pitch token should not be present if the same pitch is already played at the current position

        :param tokens: sequence of tokens to check
        :return: the error ratio (lower is better)
        """
        # If list of TokSequence -> recursive
        if isinstance(tokens, list):
            return [self.tokens_errors(tok_seq) for tok_seq in tokens]

        err = 0
        current_bar = current_pos = -1
        current_pitches = []

        for token in tokens.tokens:
            if any(tok.split("_")[1] == "None" for tok in token):
                err += 1
                continue
            has_error = False
            bar_value = int(token[4].split("_")[1])
            pos_value = int(token[3].split("_")[1])
            pitch_value = int(token[0].split("_")[1])

            # Bar
            if bar_value < current_bar:
                has_error = True
            elif bar_value > current_bar:
                current_bar = bar_value
                current_pos = -1
                current_pitches = []

            # Position
            if pos_value < current_pos:
                has_error = True
            elif pos_value > current_pos:
                current_pos = pos_value
                current_pitches = []

            # Pitch
            if pitch_value in current_pitches:
                has_error = True
            else:
                current_pitches.append(pitch_value)

            if has_error:
                err += 1

        return err / len(tokens)
