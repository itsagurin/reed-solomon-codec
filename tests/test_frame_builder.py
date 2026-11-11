"""Testy Etapu 2: ramka transmisyjna."""

import pytest


@pytest.mark.skip(reason="TODO: Etap 2")
def test_frame_length_is_255():
    """build_frame zwraca dokładnie 255 bajtów (4 + 219 + 32)."""


@pytest.mark.skip(reason="TODO: Etap 2")
def test_build_parse_roundtrip():
    """parse_frame(build_frame(seq, payload)) zwraca ten sam seq_no i payload."""


@pytest.mark.skip(reason="TODO: Etap 2")
def test_header_preamble_validation():
    """parse_header zgłasza ValueError przy błędnej preambule."""


@pytest.mark.skip(reason="TODO: Etap 2")
def test_payload_padding_and_overflow():
    """Krótszy payload jest dopełniany zerami; dłuższy niż 219 B zgłasza ValueError."""
