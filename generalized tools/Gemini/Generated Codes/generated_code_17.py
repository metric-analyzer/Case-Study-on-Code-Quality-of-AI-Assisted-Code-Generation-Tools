
from typing import List


def parse_music(music_string: str) -> List[int]:
    """Parses a string of musical notes in ASCII format and returns a list of beat durations."""

    note_durations = {
        "o": 4,  # Whole note
        "o|": 2,  # Half note
        ".|": 1,  # Quarter note
    }

    beats = []
    for note in music_string.split():
        beats.append(note_durations[note])

    return beats
