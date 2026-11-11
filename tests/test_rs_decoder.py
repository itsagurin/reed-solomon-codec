"""Testy Etapu 3: dekoder RS - korekcja błędów różnych krotności i rodzajów."""

import pytest


@pytest.mark.skip(reason="TODO: Etap 3")
def test_no_errors():
    """Słowo bez błędów: success=True, num_errors=0, słowo niezmienione."""


@pytest.mark.skip(reason="TODO: Etap 3")
@pytest.mark.parametrize("num_errors", range(1, 17))
def test_corrects_up_to_t_symbol_errors(num_errors):
    """Losowe e = 1..t błędnych symboli na losowych pozycjach jest w pełni korygowane."""


@pytest.mark.skip(reason="TODO: Etap 3")
def test_error_in_parity_section():
    """Błędy w części parzystości (pozycje 223..254) również są korygowane."""


@pytest.mark.skip(reason="TODO: Etap 3")
def test_more_than_t_errors_detected_or_miscorrected():
    """Dla e = t+1 dekoder zgłasza success=False (lub miskorekcję do innego słowa kodowego - policzyć odsetek)."""


@pytest.mark.skip(reason="TODO: Etap 3")
@pytest.mark.parametrize("burst_len_bits", [8, 16, 32, 64])
def test_corrects_burst_errors_within_capability(burst_len_bits):
    """Wiązki do 64 bitów (maks. 9 symboli) są korygowane niezależnie od wyrównania."""


@pytest.mark.skip(reason="TODO: Etap 3")
def test_burst_128_bits_borderline():
    """Wiązka 128 bitów zajmuje 16 lub 17 symboli: 16 -> korekcja, 17 -> NACK. Sprawdzić oba przypadki."""


@pytest.mark.skip(reason="TODO: Etap 3")
def test_syndromes_match_manual_evaluation():
    """compute_syndromes zgodne z poly_eval(received, alfa^i) dla znanego wektora błędów."""


@pytest.mark.skip(reason="TODO: Etap 3")
def test_berlekamp_massey_degree_equals_error_count():
    """Dla e <= t stopień Lambda(x) == e."""
