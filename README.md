# Koder i dekoder kodu Reeda-Solomona RS(255, 223)

Projekt z przedmiotu *Niezawodność i diagnostyka układów cyfrowych 2*.
Własna implementacja kodera i dekodera kodu RS nad GF(2^8) (bez gotowych bibliotek RS),
wraz z symulatorem kanału i protokołem Hybrid ARQ typu I (Stop-and-Wait).

## Parametry kodu

| Parametr            | Wartość                         |
|---------------------|---------------------------------|
| Rozmiar symbolu `m` | 8 bitów                         |
| Wielomian pierwotny | x^8 + x^4 + x^3 + x^2 + 1 (0x11D) |
| Długość bloku `n`   | 255                             |
| Długość danych `k`  | 223                             |
| Parzystość `2t`     | 32 symbole                      |
| Zdolność korekcji `t` | 16 symboli                    |

Ramka (255 B): nagłówek 4 B + payload 219 B + parzystość 32 B.

## Konwencje

- Wielomiany są listami współczynników, **najwyższa potęga na początku** listy.
- Pierwiastki wielomianu generującego: alfa^0 ... alfa^(2t-1).
- Słowo kodowe jest systematyczne: `[dane (223) | parzystość (32)]`.

## Struktura projektu

```
src/rs_codec/        pakiet z implementacją
  config.py          stałe parametrów kodu i ramki
  gf28_math.py       Etap 1: arytmetyka GF(2^8), tablice LUT, wielomiany
  rs_encoder.py      Etap 2: wielomian generujący G(x), koder systematyczny
  frame_builder.py   Etap 2: budowa i parsowanie ramki 255 B
  rs_decoder.py      Etap 3: syndromy, Berlekamp-Massey, Chien, Forney
  channel_sim.py     Etap 4: kanał BSC i błędy wiązkowe
  arq_protocol.py    Etap 4: Stop-and-Wait HARQ-I (nadajnik, odbiornik)
  metrics.py         Etap 5: BER, FER/PER, średnia liczba retransmisji
tests/               testy jednostkowe i end-to-end (pytest)
simulations/         skrypty badań symulacyjnych i wykresów
results/             wyniki symulacji (CSV, wykresy)
report/              sprawozdanie końcowe
```

## Uruchomienie

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest
```

## Status

Etap 0: szkielet projektu (sygnatury funkcji i komentarze), bez implementacji.
