from src.pre_built.counter import count_ocurrences
from unittest.mock import patch, mock_open


def test_counter():
    text = "a A a s f t w e f w y i f q F s e f g "
    with patch("builtins.open", mock_open(read_data=text)):
        assert count_ocurrences("some_path", word="f") == 5
