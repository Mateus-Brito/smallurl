from random import choice
from string import ascii_letters, digits
from typing import List

from django.conf import settings

AVAIABLE_CHARS = ascii_letters + digits
MAXIMUM_CODE_LENGTH = getattr(settings, "MAXIMUM_CODE_LENGTH", 7)


def generate_code(
    chars: List[str] = AVAIABLE_CHARS, length: int = MAXIMUM_CODE_LENGTH
) -> str:
    """generate random code by given chars

    :param List[str] chars: _description_, defaults to AVAIABLE_CHARS
    :param int length: _description_, defaults to MAXIMUM_CODE_LENGTH
    :return str: code generated from chars and length parameters
    """
    return "".join([choice(chars) for _ in range(length)])


def generate_absolute_redirection_url(absolute_uri: str, uri: str) -> str:
    """generate absolute url redirection from absolute uri and uri target

    :param str absolute_uri: absolute website uri
    :param str uri: target website uri
    :return str: final url generated
    """
    return absolute_uri + uri
