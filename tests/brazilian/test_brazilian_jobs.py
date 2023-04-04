from src.pre_built.brazilian_jobs import read_brazilian_file
from unittest.mock import patch, Mock


mock_file_pt = [
    {"salario": "2000", "titulo": "Maquinista", "tipo": "trainee"},
]


mock_file_en = [
    {"salary": "2000", "title": "Maquinista", "type": "trainee"},
]


def test_brazilian_jobs():
    with patch("src.insights.jobs.read", Mock(return_value=mock_file_pt)):
        assert read_brazilian_file("some_path") == mock_file_en
