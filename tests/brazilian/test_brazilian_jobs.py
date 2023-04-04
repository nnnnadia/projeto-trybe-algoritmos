from src.pre_built.brazilian_jobs import read_brazilian_file
from unittest.mock import patch, mock_open


mock_file_pt = [
    {"salário": "2000", "título": "Maquinista", "tipo": "trainee"},
]


mock_file_en = [
    {"salário": "2000", "título": "Maquinista", "tipo": "trainee"},
]


def test_brazilian_jobs():
    with patch("src.insights.jobs.read", mock_open(return_value=mock_file_pt)):
        assert read_brazilian_file("some_path") == mock_file_en
