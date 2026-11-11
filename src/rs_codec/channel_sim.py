"""Etap 4: symulator kanału transmisyjnego.

Dwa niezależne modele degradacji sygnału:
  * błędy niezależne - binarny kanał symetryczny BSC (każdy bit odwracany z prawdop. p_b),
  * błędy wiązkowe - ciągły fragment L bitów przekłamany w losowym miejscu ramki.

Wszystkie funkcje przyjmują generator `rng` (random.Random) dla powtarzalności eksperymentów.
"""

import random


def bsc_channel(data: bytes, p_b: float, rng: random.Random) -> bytes:
    """BSC: odwraca każdy bit `data` niezależnie z prawdopodobieństwem p_b."""
    raise NotImplementedError


def burst_channel(data: bytes, burst_len_bits: int, rng: random.Random) -> bytes:
    """Wiązka: odwraca `burst_len_bits` kolejnych bitów, począwszy od losowej pozycji bitowej."""
    raise NotImplementedError


def gilbert_elliott_channel(data: bytes, p_gb: float, p_bg: float,
                            p_err_good: float, p_err_bad: float,
                            rng: random.Random) -> bytes:
    """(Opcjonalnie) model Gilberta-Elliotta: dwa stany (dobry/zły) o różnych p_err."""
    raise NotImplementedError


def inject_symbol_errors(data: bytes, positions: list[int], rng: random.Random) -> bytes:
    """Podmienia wskazane symbole (bajty) na losowe, różne od oryginału wartości.

    Służy do testów kontrolnych: dokładnie e błędnych symboli (1..t, t+1).
    """
    raise NotImplementedError


def count_bit_errors(sent: bytes, received: bytes) -> int:
    """Liczba różniących się bitów (odległość Hamminga) - do BER."""
    raise NotImplementedError


def count_symbol_errors(sent: bytes, received: bytes) -> int:
    """Liczba różniących się symboli (bajtów)."""
    raise NotImplementedError
