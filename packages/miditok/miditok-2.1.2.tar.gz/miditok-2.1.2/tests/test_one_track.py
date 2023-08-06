#!/usr/bin/python3 python

"""One track test file
This test method is to be used with MIDI files of one track (like the maestro dataset).
It is mostly useful to measure the performance of encodings where time is based on
time shifts tokens, as these files usually don't contain tracks with very long pauses,
i.e. long duration / time-shift values probably out of range of the tokenizer's vocabulary.

NOTE: encoded tracks has to be compared with the quantized original track.

"""

from copy import deepcopy
from pathlib import Path, PurePath
from typing import Union

import miditok
from miditoolkit import MidiFile, Marker
from tqdm import tqdm

from .tests_utils import (
    ALL_TOKENIZATIONS,
    track_equals,
    tempo_changes_equals,
    time_signature_changes_equals,
    adapt_tempo_changes_times,
)

# Special beat res for test, up to 64 beats so the duration and time-shift values are
# long enough for MIDI-Like and Structured encodings, and with a single beat resolution
BEAT_RES_TEST = {(0, 64): 8}
TOKENIZER_PARAMS = {
    "beat_res": BEAT_RES_TEST,
    "use_chords": False,  # set false to speed up tests as it takes some time on maestro MIDIs
    "use_rests": True,
    "use_tempos": True,
    "use_time_signatures": True,
    "use_programs": False,
    "rest_range": (4, 16),
    "nb_tempos": 32,
    "tempo_range": (40, 250),
    "time_signature_range": (16, 2),
    "chord_maps": miditok.constants.CHORD_MAPS,
    "chord_tokens_with_root_note": True,  # Tokens will look as "Chord_C:maj"
    "chord_unknown": False,
}


def test_one_track_midi_to_tokens_to_midi(
    data_path: Union[str, Path, PurePath] = "./tests/Maestro_MIDIs",
    saving_erroneous_midis: bool = True,
):
    r"""Reads a few MIDI files, convert them into token sequences, convert them back to MIDI files.
    The converted back MIDI files should identical to original one, expect with note starting and ending
    times quantized, and maybe a some duplicated notes removed

    :param data_path: root path to the data to test
    :param saving_erroneous_midis: will save MIDIs converted back with errors, to be used to debug
    """
    files = list(Path(data_path).glob("**/*.mid"))
    at_least_one_error = False

    for i, file_path in enumerate(tqdm(files, desc="Testing One Track")):
        # Reads the midi
        midi = MidiFile(file_path)
        adapt_tempo_changes_times(midi.instruments, midi.tempo_changes)
        tracks = [deepcopy(midi.instruments[0])]
        has_errors = False

        for tokenization in ALL_TOKENIZATIONS:
            tokenizer_config = miditok.TokenizerConfig(**TOKENIZER_PARAMS)
            # Increase the number of rest just to cover very long pauses / rests in test examples
            if tokenization in ["MIDILike", "TSD"]:
                tokenizer_config.rest_range = (
                    tokenizer_config.rest_range[0],
                    max(t[1] for t in BEAT_RES_TEST),
                )
            tokenizer: miditok.MIDITokenizer = getattr(miditok, tokenization)(
                tokenizer_config=tokenizer_config
            )

            # printing the tokenizer shouldn't fail
            _ = str(tokenizer)

            # Convert the track in tokens
            tokens = tokenizer(midi)
            if not tokenizer.one_token_stream:
                tokens = tokens[0]

            # Checks types and values conformity following the rules
            tokens_types = tokenizer.tokens_errors(tokens)
            if tokens_types != 0.0:
                print(
                    f"Validation of tokens types / values successions failed with {tokenization}: {tokens_types:.2f}"
                )

            # Convert back tokens into a track object
            if not tokenizer.one_token_stream:
                tokens = [tokens]
            new_midi = tokenizer.tokens_to_midi(
                tokens, time_division=midi.ticks_per_beat
            )
            track = new_midi.instruments[0]
            tempo_changes = new_midi.tempo_changes
            time_sig_changes = None
            if tokenization == "Octuple":
                time_sig_changes = new_midi.time_signature_changes

            # Checks its good
            errors = track_equals(midi.instruments[0], track)
            if len(errors) > 0:
                has_errors = True
                if errors[0][0] != "len":
                    for err, note, exp in errors:
                        midi.markers.append(
                            Marker(
                                f"ERR {tokenization} with note {err} (pitch {note.pitch})",
                                note.start,
                            )
                        )
                print(
                    f"MIDI {i} - {file_path} failed to encode/decode NOTES with {tokenization} ({len(errors)} errors)"
                )
                # return False
            track.name = f"encoded with {tokenization}"
            tracks.append(track)

            # Checks tempos
            if tempo_changes is not None and tokenizer.config.use_tempos:
                tempo_errors = tempo_changes_equals(midi.tempo_changes, tempo_changes)
                if len(tempo_errors) > 0:
                    has_errors = True
                    print(
                        f"MIDI {i} - {file_path} failed to encode/decode TEMPO changes with "
                        f"{tokenization} ({len(tempo_errors)} errors)"
                    )

            # Checks time signatures
            if time_sig_changes is not None and tokenizer.config.use_time_signatures:
                time_sig_errors = time_signature_changes_equals(
                    midi.time_signature_changes, time_sig_changes
                )
                if len(time_sig_errors) > 0:
                    has_errors = True
                    print(
                        f"MIDI {i} - {file_path} failed to encode/decode TIME SIGNATURE changes with "
                        f"{tokenization} ({len(time_sig_errors)} errors)"
                    )

        if has_errors:
            at_least_one_error = True
            if saving_erroneous_midis:
                midi.instruments[0].name = "original quantized"
                tracks[0].name = "original not quantized"

                # Updates the MIDI and save it
                midi.instruments += tracks
                midi.dump(PurePath("tests", "test_results", file_path.name))

    assert not at_least_one_error


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="MIDI Encoding test")
    parser.add_argument(
        "--data",
        type=str,
        default="tests/Maestro_MIDIs",
        help="directory of MIDI files to use for test",
    )
    args = parser.parse_args()
    test_one_track_midi_to_tokens_to_midi(args.data)
