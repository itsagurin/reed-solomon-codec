"""Etap 1: arytmetyka ciała Galois GF(2^8).

Odpowiada za:
  * generację tablic logarytmów / antylogarytmów (LUT) z wielomianu pierwotnego,
  * podstawowe operacje na elementach ciała (dodawanie = XOR, mnożenie, dzielenie, potęgowanie),
  * operacje na wielomianach o współczynnikach z GF(2^8).

Konwencja: wielomian to lista współczynników, NAJWYŻSZA potęga na początku listy,
np. x^2 + 3x + 5  ->  [1, 3, 5].
"""

from __future__ import annotations

from rs_codec.config import FIELD_SIZE, PRIM_POLY

# Tablice wypełniane przez build_tables() (wywołanie na poziomie modułu).
EXP: list[int] = []
LOG: list[int] = []

_ORDER = FIELD_SIZE - 1


def build_tables(prim_poly: int = PRIM_POLY) -> None:
    """Generuje tablice EXP i LOG na podstawie wielomianu pierwotnego `prim_poly`."""
    EXP[:] = [0] * (2 * _ORDER + 2)
    LOG[:] = [0] * FIELD_SIZE

    x = 1
    for i in range(_ORDER):
        EXP[i] = x
        LOG[x] = i
        x <<= 1
        if x & FIELD_SIZE:
            x ^= prim_poly

    if x != 1:
        raise ValueError(f"Wielomian {prim_poly:#x} nie jest pierwotny")

    for i in range(_ORDER, 2 * _ORDER + 2):
        EXP[i] = EXP[i - _ORDER]


# Operacje na elementach ciała

def gf_add(a: int, b: int) -> int:
    """Dodawanie (i odejmowanie) w GF(2^8) - zwykły XOR."""
    return a ^ b


def gf_mul(a: int, b: int) -> int:
    """Mnożenie przez tablice LUT: alfa^(log a + log b); zwraca 0, gdy a lub b to 0."""
    if a == 0 or b == 0:
        return 0
    return EXP[LOG[a] + LOG[b]]       # suma logarytmów <= 508, mieści się w tablicy EXP


def gf_div(a: int, b: int) -> int:
    """Dzielenie a / b przez tablice LUT; zgłasza ZeroDivisionError dla b == 0."""
    if b == 0:
        raise ZeroDivisionError("dzielenie przez 0 w GF(2^8)")
    if a == 0:
        return 0
    return EXP[LOG[a] - LOG[b] + _ORDER]   # + 255, żeby indeks nie był ujemny


def gf_pow(a: int, power: int) -> int:
    """Potęgowanie a^power (power może być ujemne)."""
    if a == 0:
        if power == 0:
            return 1                  # umowa: 0^0 = 1
        if power < 0:
            raise ZeroDivisionError("0 do ujemnej potęgi w GF(2^8)")
        return 0
    return EXP[(LOG[a] * power) % _ORDER]


def gf_inv(a: int) -> int:
    """Odwrotność multiplikatywna elementu a (a != 0)."""
    if a == 0:
        raise ZeroDivisionError("0 nie ma odwrotności w GF(2^8)")
    return EXP[_ORDER - LOG[a]]


# Operacje na wielomianach nad GF(2^8)

def poly_add(p: list[int], q: list[int]) -> list[int]:
    """Suma wielomianów (XOR współczynników, wyrównanie do najniższych potęg).

    Zerowe współczynniki wiodące NIE są obcinane (długość wyniku = max(len(p), len(q))).
    """
    n = max(len(p), len(q))
    result = [0] * n
    for i, c in enumerate(p):
        result[i + n - len(p)] ^= c
    for i, c in enumerate(q):
        result[i + n - len(q)] ^= c
    return result


def poly_scale(p: list[int], scalar: int) -> list[int]:
    """Mnożenie wielomianu przez stałą z GF(2^8)."""
    return [gf_mul(c, scalar) for c in p]


def poly_mul(p: list[int], q: list[int]) -> list[int]:
    """Iloczyn dwóch wielomianów (splot ze współczynnikami mnożonymi w GF)."""
    if not p or not q:
        return []
    result = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            result[i + j] ^= gf_mul(a, b)
    return result


def poly_eval(p: list[int], x: int) -> int:
    """Wartość wielomianu p w punkcie x (schemat Hornera)."""
    y = 0
    for c in p:
        y = gf_mul(y, x) ^ c
    return y


def poly_divmod(dividend: list[int], divisor: list[int]) -> tuple[list[int], list[int]]:
    """Dzielenie wielomianów; zwraca (iloraz, reszta). Dzielnik musi mieć niezerowy współczynnik wiodący.

    Reszta ma zawsze dokładnie len(divisor) - 1 współczynników (wiodące zera zostają),
    dzięki czemu koder dostaje stałą liczbę symboli parzystości.
    """
    if not divisor or divisor[0] == 0:
        raise ZeroDivisionError("dzielnik musi mieć niezerowy współczynnik wiodący")

    rem_len = len(divisor) - 1
    if len(dividend) < len(divisor):
        return [0], [0] * (rem_len - len(dividend)) + list(dividend)

    out = list(dividend)
    quotient_len = len(dividend) - rem_len
    for i in range(quotient_len):
        coef = gf_div(out[i], divisor[0])
        out[i] = coef
        if coef:
            for j in range(1, len(divisor)):
                out[i + j] ^= gf_mul(divisor[j], coef)

    return out[:quotient_len], out[quotient_len:]


# Tablice budujemy raz przy imporcie modułu.
build_tables()
