"""Testy Etapu 1: arytmetyka GF(2^8)."""

import random

import pytest

from rs_codec.config import PRIM_POLY
from rs_codec.gf28_math import (
    EXP, LOG,
    gf_add, gf_mul, gf_div, gf_pow, gf_inv,
    poly_add, poly_scale, poly_mul, poly_eval, poly_divmod,
)


def slow_mul(a: int, b: int) -> int:
    """Mnożenie 'wolne' (shift-and-xor), niezależne od tablic - wzorzec do porównań."""
    result = 0
    while b:
        if b & 1:
            result ^= a
        a <<= 1
        if a & 0x100:
            a ^= PRIM_POLY
        b >>= 1
    return result


def test_tables_are_consistent():
    """EXP[LOG[x]] == x dla x = 1..255; EXP[0] == 1; alfa generuje wszystkie 255 niezerowych elementów."""
    assert EXP[0] == 1
    assert EXP[1] == 2
    assert EXP[8] == 0x1D                       # 2^8 = 256 -> XOR z 0x11D = 29
    for x in range(1, 256):
        assert EXP[LOG[x]] == x
    assert sorted(EXP[:255]) == list(range(1, 256))   # każdy niezerowy element dokładnie raz
    assert EXP[255] == 1                        # okres 255
    assert all(EXP[i] == EXP[i % 255] for i in range(len(EXP)))


def test_add_is_xor():
    """gf_add(a, b) == a ^ b; a + a == 0."""
    rng = random.Random(1)
    for _ in range(200):
        a, b = rng.randrange(256), rng.randrange(256)
        assert gf_add(a, b) == a ^ b
        assert gf_add(a, a) == 0


def test_mul_div_inverse():
    """a * inv(a) == 1; (a * b) / b == a; mnożenie przez 0 daje 0; porównanie z mnożeniem 'wolnym' (shift-and-xor)."""
    for a in range(256):
        assert gf_mul(a, 0) == 0 and gf_mul(0, a) == 0
        assert gf_mul(a, 1) == a
        for b in range(256):
            assert gf_mul(a, b) == slow_mul(a, b)
    for a in range(1, 256):
        assert gf_mul(a, gf_inv(a)) == 1
        for b in range(1, 256):
            assert gf_div(gf_mul(a, b), b) == a
    assert gf_mul(3, 7) == 9
    assert gf_mul(2, 128) == 29
    assert gf_div(0, 5) == 0
    with pytest.raises(ZeroDivisionError):
        gf_div(5, 0)
    with pytest.raises(ZeroDivisionError):
        gf_inv(0)


def test_mul_commutative_associative_distributive():
    """Własności ciała na losowych trójkach elementów."""
    rng = random.Random(2)
    for _ in range(1000):
        a, b, c = rng.randrange(256), rng.randrange(256), rng.randrange(256)
        assert gf_mul(a, b) == gf_mul(b, a)
        assert gf_mul(gf_mul(a, b), c) == gf_mul(a, gf_mul(b, c))
        assert gf_mul(a, gf_add(b, c)) == gf_add(gf_mul(a, b), gf_mul(a, c))


def test_pow():
    """alfa^255 == 1; gf_pow(a, -1) == gf_inv(a)."""
    assert gf_pow(2, 255) == 1
    assert gf_pow(2, 8) == 29
    for a in range(1, 256):
        assert gf_pow(a, -1) == gf_inv(a)
        assert gf_pow(a, 0) == 1
        assert gf_pow(a, 2) == gf_mul(a, a)
    assert gf_pow(0, 0) == 1
    assert gf_pow(0, 5) == 0
    with pytest.raises(ZeroDivisionError):
        gf_pow(0, -1)


def test_poly_ops():
    """poly_mul / poly_eval / poly_divmod: (p*q) / q == p z resztą 0; poly_eval zgodne z ręcznym obliczeniem."""
    # Przykłady ręczne (te same, co w objaśnieniu).
    assert poly_add([1, 3, 5], [2, 4]) == [1, 1, 1]
    assert poly_scale([1, 3, 5], 2) == [2, 6, 10]
    assert poly_mul([1, 1], [1, 2]) == [1, 3, 2]          # (x+1)(x+2) = x^2 + 3x + 2
    assert poly_eval([1, 3, 5], 2) == 7                   # 4 ^ 6 ^ 5
    assert poly_divmod([1, 0, 0], [1, 1]) == ([1, 1], [1])  # x^2 = (x+1)(x+1) + 1

    rng = random.Random(3)
    for _ in range(100):
        p = [rng.randrange(256) for _ in range(rng.randrange(1, 12))]
        q = [rng.randrange(1, 256)] + [rng.randrange(256) for _ in range(rng.randrange(0, 8))]
        quotient, remainder = poly_divmod(poly_mul(p, q), q)
        assert quotient == p
        assert remainder == [0] * (len(q) - 1)

        # dzielenie z resztą: dividend == iloraz * dzielnik + reszta
        dividend = [rng.randrange(256) for _ in range(rng.randrange(1, 20))]
        quotient, remainder = poly_divmod(dividend, q)
        assert len(remainder) == len(q) - 1
        back = poly_add(poly_mul(quotient, q), remainder)
        assert back[-len(dividend):] == dividend

        # eval jest zgodny z mnożeniem i dodawaniem: (p*q)(x) = p(x) * q(x)
        x = rng.randrange(256)
        assert poly_eval(poly_mul(p, q), x) == gf_mul(poly_eval(p, x), poly_eval(q, x))
        assert poly_eval(poly_add(p, q), x) == poly_eval(p, x) ^ poly_eval(q, x)

    with pytest.raises(ZeroDivisionError):
        poly_divmod([1, 2, 3], [0, 1])
