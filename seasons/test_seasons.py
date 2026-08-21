import pytest
from datetime import date
from seasons import get_minutes, convert_to_words


def test_get_minutes():
    assert get_minutes("2020-01-01", date(2021, 01, 01)) == 525600
    assert get_minutes("2020-01-01", date(2022, 01, 01)) == 1051200


def test_invalid_date():
    with pytest.raises(ValueError):
        get_minutes("February 6th, 1998", date.today())


def test_convert_to_words():
    assert convert_to_words(525600) == "Five hundred twenty-five thousand, six hundred"
