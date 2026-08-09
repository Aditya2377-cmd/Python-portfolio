from numb3rs import validate


def test_correct_format():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True


def test_range_first_byte():
    assert validate("256.1.1.1") == False


def test_range_other_bytes():
    # CS50 explicitly checks byte 2, byte 3, and byte 4!
    assert validate("1.256.1.1") == False
    assert validate("1.1.256.1") == False
    assert validate("1.1.1.256") == False


def test_invalid_length():
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False  # Five-byte test case!


def test_non_numeric():
    assert validate("cat") == False
    assert validate("1.2.cat.4") == False
