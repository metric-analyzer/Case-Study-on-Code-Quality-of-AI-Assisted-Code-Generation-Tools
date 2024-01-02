
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

METADATA = { 'author': 'jt', 'dataset': 'test' } 
def check(parse_music): 
    assert parse_music('') == [] 
    assert parse_music('o o o o') == [4, 4, 4, 4] 
    assert parse_music('.| .| .| .|') == [1, 1, 1, 1] 
    assert parse_music('o| o| .| .| o o o o') == [2, 2, 1, 1, 4, 4, 4, 4] 
    assert parse_music('o| .| o| .| o o| o o|') == [2, 1, 2, 1, 4, 2, 4, 2] 
    
check(parse_music)