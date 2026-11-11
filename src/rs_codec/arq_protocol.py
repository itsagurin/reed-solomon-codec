"""Etap 4: Hybrid ARQ typu I (FEC RS + Stop-and-Wait ARQ).

Przebieg dla jednej ramki:
  nadajnik: build_frame -> kanał -> odbiornik: decode RS
     * sukces (S_i = 0 lub e <= t)  -> ACK z numerem ramki, payload zaakceptowany,
     * błąd niekorygowalny          -> NACK, nadajnik retransmituje tę samą ramkę
       (również po przekroczeniu timeoutu - w symulacji: utracona odpowiedź).
"""

from __future__ import annotations

import random
from collections.abc import Callable
from dataclasses import dataclass


@dataclass
class ArqStats:
    """Statystyki z przebiegu symulacji ARQ."""
    frames_sent: int = 0          # liczba wszystkich transmisji (z retransmisjami)
    frames_delivered: int = 0     # liczba ramek dostarczonych poprawnie
    frames_dropped: int = 0       # ramki porzucone po przekroczeniu max_retries
    retransmissions: int = 0      # łączna liczba retransmisji
    undetected_errors: int = 0    # zaakceptowane ramki z błędnym payloadem (błędna korekcja)


class Sender:
    """Nadajnik Stop-and-Wait: numeruje ramki, trzyma ostatnią ramkę do retransmisji."""

    def next_frame(self, payload: bytes) -> bytes:
        """Buduje nową ramkę DATA z kolejnym Seq_No."""
        raise NotImplementedError

    def retransmit(self) -> bytes:
        """Zwraca ponownie tę samą ramkę (po NACK lub przekroczeniu limitu czasu)."""
        raise NotImplementedError


class Receiver:
    """Odbiornik: dekoduje RS i decyduje o ACK / NACK."""

    def receive(self, received_frame: bytes) -> tuple[bool, int | None, bytes | None]:
        """Zwraca (ack, seq_no, payload). ack=False -> NACK, wtedy seq_no/payload mogą być None."""
        raise NotImplementedError


def run_stop_and_wait(payloads: list[bytes],
                      channel_fn: Callable[[bytes, random.Random], bytes],
                      rng: random.Random,
                      max_retries: int = 10) -> ArqStats:
    """Symuluje wysłanie wszystkich `payloads` protokołem Stop-and-Wait przez kanał `channel_fn`.

    Zwraca ArqStats; na tej podstawie metrics.py liczy średnią liczbę retransmisji na ramkę.
    """
    raise NotImplementedError
