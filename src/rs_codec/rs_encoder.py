"""Etap 2: koder systematyczny kodu Reeda-Solomona.

Słowo kodowe: C(x) = M(x) * x^(2t) + R(x),  R(x) = (M(x) * x^(2t)) mod G(x),
czyli [dane (K symboli) | parzystość (2t symboli)].
"""

from __future__ import annotations

from rs_codec.config import NSYM


def generator_poly(nsym: int = NSYM) -> list[int]:
    """Wielomian generujący G(x) = prod_{i=0}^{nsym-1} (x - alfa^i), stopnia `nsym`.

    Wynik można zbuforować - nie zależy od danych.
    """
    raise NotImplementedError


def compute_parity(message: list[int], nsym: int = NSYM) -> list[int]:
    """Oblicza `nsym` symboli parzystości jako resztę z dzielenia M(x)*x^nsym przez G(x)."""
    raise NotImplementedError


def encode(message: list[int] | bytes, nsym: int = NSYM) -> list[int]:
    """Koduje wiadomość (K symboli) do słowa kodowego długości K + nsym.

    Zwraca message + parzystość (kod systematyczny).
    """
    raise NotImplementedError
