"""Testy Etapu 5: end-to-end (ramka -> kanał -> dekoder -> payload) i metryki."""

import pytest


@pytest.mark.skip(reason="TODO: Etap 5")
def test_full_pipeline_recovers_payload():
    """build_frame -> kanał z <= t błędami -> decode -> parse_frame zwraca oryginalny payload."""


@pytest.mark.skip(reason="TODO: Etap 5")
def test_metrics_ber_fer():
    """ber / fer na małych, ręcznie policzonych przykładach."""


@pytest.mark.skip(reason="TODO: Etap 5")
def test_avg_retransmissions_formula():
    """avg_retransmissions == retransmisje / dostarczone ramki dla przykładowych ArqStats."""
