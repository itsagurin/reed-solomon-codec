"""Testy Etapu 1: arytmetyka GF(2^8)."""

import pytest


@pytest.mark.skip(reason="TODO: Etap 1")
def test_tables_are_consistent():
    """EXP[LOG[x]] == x dla x = 1..255; EXP[0] == 1; alfa generuje wszystkie 255 niezerowych elementów."""


@pytest.mark.skip(reason="TODO: Etap 1")
def test_add_is_xor():
    """gf_add(a, b) == a ^ b; a + a == 0."""


@pytest.mark.skip(reason="TODO: Etap 1")
def test_mul_div_inverse():
    """a * inv(a) == 1; (a * b) / b == a; mnożenie przez 0 daje 0; porównanie z mnożeniem 'wolnym' (shift-and-xor)."""


@pytest.mark.skip(reason="TODO: Etap 1")
def test_mul_commutative_associative_distributive():
    """Własności ciała na losowych trójkach elementów."""


@pytest.mark.skip(reason="TODO: Etap 1")
def test_pow():
    """alfa^255 == 1; gf_pow(a, -1) == gf_inv(a)."""


@pytest.mark.skip(reason="TODO: Etap 1")
def test_poly_ops():
    """poly_mul / poly_eval / poly_divmod: (p*q) / q == p z resztą 0; poly_eval zgodne z ręcznym obliczeniem."""
