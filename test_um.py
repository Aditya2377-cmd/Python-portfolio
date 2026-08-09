from um import count


def test_single_um():
    assert count("um") == 1
    assert count("um?") == 1
    assert count("Um, thanks for the album.") == 1


def test_multiple_um():
    assert count("Um, thanks, um...") == 2
    assert count("um? Um! UM.") == 3


def test_word_substrings():
    # Ensures "yummy", "album", "umbrella" are not counted
    assert count("yummy") == 0
    assert count("album") == 0
    assert count("umbrella") == 0


def test_case_insensitivity():
    assert count("UM") == 1
    assert count("uM") == 1
