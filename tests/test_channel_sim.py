"""Testy Etapu 4: symulator kanału."""

import pytest


@pytest.mark.skip(reason="TODO: Etap 4")
def test_bsc_zero_probability_is_identity():
    """p_b = 0 -> dane bez zmian; p_b = 1 -> wszystkie bity odwrócone."""


@pytest.mark.skip(reason="TODO: Etap 4")
def test_bsc_error_rate_statistics():
    """Dla dużej próbki empiryczny BER ~ p_b (z tolerancją statystyczną)."""


@pytest.mark.skip(reason="TODO: Etap 4")
def test_burst_flips_exactly_L_consecutive_bits():
    """Odległość Hamminga == L, a przekłamane bity tworzą jeden ciągły obszar."""


@pytest.mark.skip(reason="TODO: Etap 4")
def test_inject_symbol_errors_exact_count():
    """Dokładnie |positions| symboli różni się od oryginału."""


@pytest.mark.skip(reason="TODO: Etap 4")
def test_reproducibility_with_seed():
    """Ten sam seed random.Random daje identyczny wynik."""
