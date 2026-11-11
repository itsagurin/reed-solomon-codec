"""Etap 5: metryki efektywności kodu i protokołu.

  * BER przed i po dekodowaniu RS,
  * FER / PER (odsetek ramek niepoprawnie odebranych),
  * średnia liczba retransmisji ARQ na jedną pomyślnie dostarczoną ramkę.
"""

from rs_codec.arq_protocol import ArqStats


def ber(sent: bytes, received: bytes) -> float:
    """Bitowa stopa błędów dla pary (wysłane, odebrane): błędne bity / wszystkie bity."""
    raise NotImplementedError


def fer(num_failed_frames: int, num_frames: int) -> float:
    """Stopa błędów ramek (PER): ramki niepoprawne / wszystkie ramki."""
    raise NotImplementedError


def avg_retransmissions(stats: ArqStats) -> float:
    """Średnia liczba retransmisji przypadająca na jedną dostarczoną ramkę."""
    raise NotImplementedError
