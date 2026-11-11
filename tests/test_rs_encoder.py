"""Testy Etapu 2: koder RS."""

import pytest


@pytest.mark.skip(reason="TODO: Etap 2")
def test_generator_poly_degree_and_roots():
    """G(x) ma stopień 2t, współczynnik wiodący 1 i pierwiastki alfa^0 .. alfa^(2t-1)."""


@pytest.mark.skip(reason="TODO: Etap 2")
def test_encode_is_systematic():
    """Pierwsze K symboli słowa kodowego == wiadomość; długość słowa == N."""


@pytest.mark.skip(reason="TODO: Etap 2")
def test_codeword_has_zero_syndromes():
    """Każde słowo kodowe ma wszystkie syndromy S_i == 0 (C(alfa^i) == 0)."""


@pytest.mark.skip(reason="TODO: Etap 2")
def test_encode_zero_message():
    """Wiadomość zerowa -> parzystość zerowa (kod liniowy)."""


@pytest.mark.skip(reason="TODO: Etap 2")
def test_encode_linearity():
    """encode(a) XOR encode(b) == encode(a XOR b)."""
