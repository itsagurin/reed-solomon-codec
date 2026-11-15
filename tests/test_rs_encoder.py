"""Testy Etapu 2: enkoder Reeda-Solomona."""

import random

import pytest

from rs_codec.config import K, N, NSYM
from rs_codec.gf28_math import gf_pow, poly_divmod, poly_eval, poly_mul
from rs_codec.rs_encoder import compute_parity, encode, generator_poly


def test_generator_small_known():
    """nsym=2: G(x) = (x + 1)(x + 2) = x^2 + 3x + 2."""
    assert generator_poly(2) == [1, 3, 2]


def test_generator_degree_and_roots():
    """G ma stopień nsym, jest moniczny i zeruje się w alfa^0 .. alfa^(nsym-1)."""
    g = generator_poly()
    assert len(g) == NSYM + 1
    assert g[0] == 1
    for i in range(NSYM):
        assert poly_eval(g, gf_pow(2, i)) == 0
    assert poly_eval(g, gf_pow(2, NSYM)) != 0     # alfa^nsym nie jest pierwiastkiem


def test_generator_returns_copy():
    """Modyfikacja wyniku nie psuje cache'u."""
    g = generator_poly()
    g[0] = 99
    assert generator_poly()[0] == 1


def test_known_vector_qr_style():
    """Wektor referencyjny (nsym=10, prim 0x11D, pierwszy pierwiastek alfa^0)."""
    msg = [0x40, 0xD2, 0x75, 0x47, 0x76, 0x17, 0x32, 0x06,
           0x27, 0x26, 0x96, 0xC6, 0xC6, 0x96, 0x70, 0xEC]
    expected_parity = [0xBC, 0x2A, 0x90, 0x13, 0x6B, 0xAF, 0xEF, 0xFD, 0x4B, 0xE0]
    assert compute_parity(msg, nsym=10) == expected_parity
    assert encode(msg, nsym=10) == msg + expected_parity


def test_systematic_and_length():
    """Słowo kodowe = dane + parzystość, długość n = 255 dla k = 223."""
    rng = random.Random(10)
    msg = [rng.randrange(256) for _ in range(K)]
    cw = encode(msg)
    assert len(cw) == N
    assert cw[:K] == msg
    assert cw[K:] == compute_parity(msg)
    assert len(cw[K:]) == NSYM


def test_codeword_is_valid():
    """Poprawne słowo kodowe: C(alfa^i) = 0 (syndromy zerowe) i G | C."""
    rng = random.Random(11)
    g = generator_poly()
    for _ in range(20):
        msg = [rng.randrange(256) for _ in range(K)]
        cw = encode(msg)
        for i in range(NSYM):
            assert poly_eval(cw, gf_pow(2, i)) == 0
        _, rem = poly_divmod(cw, g)
        assert rem == [0] * NSYM


def test_linearity():
    """Kod liniowy: encode(a ^ b) == encode(a) ^ encode(b)."""
    rng = random.Random(12)
    a = [rng.randrange(256) for _ in range(K)]
    b = [rng.randrange(256) for _ in range(K)]
    ab = [x ^ y for x, y in zip(a, b)]
    assert encode(ab) == [x ^ y for x, y in zip(encode(a), encode(b))]


def test_zero_message_and_bytes_input():
    """Same zera -> same zera; bytes i lista dają ten sam wynik."""
    assert encode([0] * K) == [0] * N
    rng = random.Random(13)
    raw = bytes(rng.randrange(256) for _ in range(K))
    assert encode(raw) == encode(list(raw))


def test_shortened_code():
    """Krótsza wiadomość też działa (kod skrócony), np. nagłówek + payload mniejszy niż K."""
    msg = list(range(1, 51))
    cw = encode(msg)
    assert len(cw) == 50 + NSYM
    for i in range(NSYM):
        assert poly_eval(cw, gf_pow(2, i)) == 0


def test_min_distance():
    """Zmiana jednego symbolu danych zmienia co najmniej nsym symboli parzystości (MDS: d = nsym + 1)."""
    rng = random.Random(14)
    msg = [rng.randrange(256) for _ in range(K)]
    base = encode(msg)
    for pos in (0, 100, K - 1):
        other = list(msg)
        other[pos] ^= rng.randrange(1, 256)
        diff = sum(x != y for x, y in zip(base, encode(other)))
        assert diff >= NSYM + 1


def test_invalid_input():
    with pytest.raises(ValueError):
        encode([])
    with pytest.raises(ValueError):
        encode([0] * (N - NSYM + 1))        # za długa
    with pytest.raises(ValueError):
        encode([0, 1, 256])                 # symbol poza GF(2^8)
    with pytest.raises(ValueError):
        encode([0, 1, -1])
    with pytest.raises(ValueError):
        generator_poly(0)