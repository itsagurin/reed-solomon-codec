"""Etap 5: wykresy z plików CSV w results/ (zapis PNG do results/).

Uruchomienie (z katalogu głównego):  python simulations/plot_results.py
"""


def plot_symbol_errors() -> None:
    """Skuteczność korekcji w funkcji liczby błędnych symboli (1..t+1)."""
    raise NotImplementedError


def plot_bsc() -> None:
    """BER przed vs. po dekodowaniu RS oraz FER w funkcji p_b (skala logarytmiczna)."""
    raise NotImplementedError


def plot_burst() -> None:
    """FER i średnia liczba retransmisji w funkcji długości wiązki L."""
    raise NotImplementedError


def main() -> None:
    plot_symbol_errors()
    plot_bsc()
    plot_burst()


if __name__ == "__main__":
    main()
