"""Testy Etapu 4: protokół Stop-and-Wait HARQ-I."""

import pytest


@pytest.mark.skip(reason="TODO: Etap 4")
def test_clean_channel_no_retransmissions():
    """Kanał idealny: wszystkie ramki dostarczone, 0 retransmisji."""


@pytest.mark.skip(reason="TODO: Etap 4")
def test_correctable_errors_no_retransmissions():
    """Błędy <= t: FEC je koryguje, odbiornik odsyła ACK bez retransmisji."""


@pytest.mark.skip(reason="TODO: Etap 4")
def test_uncorrectable_errors_trigger_nack_and_retransmission():
    """Pierwsza transmisja z e > t -> NACK -> retransmisja tej samej ramki (ten sam Seq_No)."""


@pytest.mark.skip(reason="TODO: Etap 4")
def test_max_retries_drops_frame():
    """Kanał zawsze uszkadzający ponad t symboli -> ramka porzucona po max_retries."""
