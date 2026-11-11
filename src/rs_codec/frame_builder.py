"""Etap 2: budowa i parsowanie ramki transmisyjnej (255 B).

Układ ramki:
    bajty 0-3     nagłówek (preambuła synchronizacyjna + numer sekwencyjny Seq_No)
    bajty 4-222   payload (219 B)
    bajty 223-254 parzystość RS (32 B)

Nagłówek + payload tworzą wiadomość o długości K = 223 symboli podawaną do kodera.
"""

from dataclasses import dataclass


@dataclass
class Frame:
    """Rozpakowana ramka."""
    seq_no: int
    payload: bytes
    parity: bytes


def make_header(seq_no: int) -> bytes:
    """Buduje 4-bajtowy nagłówek: preambuła + Seq_No (zawijany do dostępnej liczby bitów)."""
    raise NotImplementedError


def parse_header(header: bytes) -> int:
    """Odczytuje Seq_No z nagłówka; zgłasza ValueError, gdy preambuła jest niepoprawna."""
    raise NotImplementedError


def build_frame(seq_no: int, payload: bytes) -> bytes:
    """Składa ramkę: nagłówek + payload (dopełniony zerami do 219 B) + parzystość z rs_encoder.encode().

    Zwraca dokładnie N = 255 bajtów.
    """
    raise NotImplementedError


def parse_frame(frame: bytes) -> Frame:
    """Dzieli 255-bajtową ramkę (po dekodowaniu RS) na seq_no, payload i parzystość."""
    raise NotImplementedError
