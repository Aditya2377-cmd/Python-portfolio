from twttr import shorten


def test_lowercase():
    assert shorten("twitter") == "twttr"


def test_uppercase():
    assert shorten("TWITTER") == "TWTTR"


def test_mixed_case():
    assert shorten("CS50p") == "CS50p"


def test_numbers():
    assert shorten("1234") == "1234"


def test_punctuation():
    assert shorten("what's your name?") == "wht's yr nm?"
