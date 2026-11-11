"""Etap 5: badania symulacyjne end-to-end. Wyniki zapisywane do results/*.csv.

Uruchomienie (z katalogu głównego):  python simulations/run_experiments.py
"""

import random

# Parametry z specyfikacji projektu.
BSC_P_B_VALUES = [1e-4, 3e-4, 1e-3, 3e-3, 1e-2, 3e-2, 1e-1]   # p_b z przedziału [1e-4, 1e-1]
BURST_LENGTHS_BITS = [8, 16, 32, 64, 128]                     # długości wiązek L
FRAMES_PER_POINT = 1000                                       # liczba ramek na punkt pomiarowy
SEED = 12345                                                  # powtarzalność eksperymentów


def experiment_symbol_errors(rng: random.Random) -> None:
    """Test kontrolny: dokładnie e = 1..t+1 błędnych symboli -> odsetek udanych korekcji.

    Wynik: results/symbol_errors.csv
    """
    raise NotImplementedError


def experiment_bsc(rng: random.Random) -> None:
    """Błędy niezależne (BSC): dla każdego p_b liczy BER przed/po RS, FER, śr. liczbę retransmisji.

    Wynik: results/bsc.csv
    """
    raise NotImplementedError


def experiment_burst(rng: random.Random) -> None:
    """Błędy wiązkowe: dla każdego L liczy FER po RS, śr. liczbę retransmisji ARQ.

    Wynik: results/burst.csv
    """
    raise NotImplementedError


def main() -> None:
    """Uruchamia wszystkie eksperymenty z jednym wspólnym generatorem losowym."""
    rng = random.Random(SEED)
    experiment_symbol_errors(rng)
    experiment_bsc(rng)
    experiment_burst(rng)


if __name__ == "__main__":
    main()
