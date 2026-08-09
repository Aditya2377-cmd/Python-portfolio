from response import validate


def test_valid_emails():
    assert validate("malan@harvard.edu") == "Valid"
    assert validate("student_123@gmail.com") == "Valid"
    assert validate("test.user@domain.co.uk") == "Valid"


def test_invalid_emails():
    assert validate("malan@@harvard.edu") == "Invalid"
    assert validate("malan@harvard..edu") == "Invalid"
    assert validate("cat") == "Invalid"
    assert validate("malan@harvard") == "Invalid"
    assert validate("malan@") == "Invalid"



def test_empty_input():
    assert validate("") == "Invalid"
