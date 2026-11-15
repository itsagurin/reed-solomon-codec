"""Etap 2: koder systematyczny kodu Reeda-Solomona.

Słowo kodowe: C(x) = M(x) * x^(2t) + R(x),  R(x) = (M(x) * x^(2t)) mod G(x),
czyli [dane (K symboli) | parzystość (2t symboli)].

Konwencja (jak w gf28_math): wielomian to lista współczynników, NAJWYŻSZA potęga
na początku listy. Pierwszy pierwiastek generatora to alfa^0, alfa = 2.
"""

from __future__ import annotations

from rs_codec.config import FIELD_SIZE, NSYM
from rs_codec.gf28_math import gf_pow, poly_divmod, poly_mul

_MAX_BLOCK = FIELD_SIZE - 1   # 255 = maksymalna długość słowa kodowego (n = 2^m - 1)
_ALPHA = 2                    # element pierwotny ciała

# Cache wielomianów generujących: G(x) nie zależy od danych, tylko od nsym.
_GENERATOR_CACHE: dict[int, tuple[int, ...]] = {}


def _check_nsym(nsym: int) -> None:
    if not 1 <= nsym < _MAX_BLOCK:
        raise ValueError(f"nsym musi być w zakresie 1..{_MAX_BLOCK - 1}, podano {nsym}")


def generator_poly(nsym: int = NSYM) -> list[int]:
    """Wielomian generujący G(x) = prod_{i=0}^{nsym-1} (x - alfa^i), stopnia `nsym`.

    Wynik można zbuforować - nie zależy od danych.
    """
    _check_nsym(nsym)
    cached = _GENERATOR_CACHE.get(nsym)
    if cached is None:
        g = [1]
        for i in range(nsym):
            # W GF(2^8) odejmowanie = dodawanie, więc (x - alfa^i) = (x + alfa^i).
            g = poly_mul(g, [1, gf_pow(_ALPHA, i)])
        cached = _GENERATOR_CACHE[nsym] = tuple(g)
    return list(cached)   # kopia, żeby wywołujący nie zepsuł cache'u


def _validate_message(message: list[int] | bytes, nsym: int) -> list[int]:
    msg = list(message)
    if not msg:
        raise ValueError("wiadomość nie może być pusta")
    if len(msg) + nsym > _MAX_BLOCK:
        raise ValueError(
            f"wiadomość za długa: {len(msg)} + {nsym} symboli parzystości "
            f"przekracza długość bloku {_MAX_BLOCK}"
        )
    if any(not isinstance(s, int) or not 0 <= s < FIELD_SIZE for s in msg):
        raise ValueError(f"symbole wiadomości muszą być liczbami całkowitymi 0..{FIELD_SIZE - 1}")
    return msg


def compute_parity(message: list[int], nsym: int = NSYM) -> list[int]:
    """Oblicza `nsym` symboli parzystości jako resztę z dzielenia M(x)*x^nsym przez G(x)."""
    _check_nsym(nsym)
    msg = _validate_message(message, nsym)
    shifted = msg + [0] * nsym                    # M(x) * x^nsym
    _, remainder = poly_divmod(shifted, generator_poly(nsym))
    return remainder                              # dokładnie nsym symboli (z wiodącymi zerami)


def encode(message: list[int] | bytes, nsym: int = NSYM) -> list[int]:
    """Koduje wiadomość (K symboli) do słowa kodowego długości K + nsym.

    Zwraca message + parzystość (kod systematyczny).
    """
    msg = _validate_message(message, nsym)
    return msg + compute_parity(msg, nsym)