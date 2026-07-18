import pytest

from src.utils.helpers import validate_prompt
from src.utils.helpers import clean_text


def test_clean_text():

    texto = "   Olá Mundo   "

    assert clean_text(texto) == "Olá Mundo"


def test_validate_prompt_ok():

    assert validate_prompt("Teste") == True


def test_validate_prompt_empty():

    with pytest.raises(ValueError):
        validate_prompt("")