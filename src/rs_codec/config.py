"""Stałe parametry kodu RS i struktury ramki.

Jedno miejsce prawdy: wszystkie pozostałe moduły importują wartości stąd,
żeby zmiana parametrów (np. test z mniejszym kodem) nie wymagała edycji wielu plików.
"""

# --- Ciało Galois GF(2^m) ---
M = 8                      # rozmiar symbolu w bitach
PRIM_POLY = 0x11D          # x^8 + x^4 + x^3 + x^2 + 1 (standard CCSDS / DVB)
FIELD_SIZE = 2 ** M        # liczba elementów ciała (256)

# --- Parametry kodu RS(n, k) ---
N = FIELD_SIZE - 1         # długość bloku w symbolach (255)
K = 223                    # liczba symboli informacyjnych
NSYM = N - K               # liczba symboli parzystości = 2t (32)
T = NSYM // 2              # zdolność korekcji w symbolach (16)
FCR = 0                    # pierwszy pierwiastek wielomianu generującego: alfa^FCR

# --- Struktura ramki transmisyjnej (łącznie N bajtów) ---
HEADER_LEN = 4             # nagłówek: preambuła synchronizacyjna + identyfikator pakietu
PAYLOAD_LEN = K - HEADER_LEN   # 219 bajtów właściwych danych
PARITY_LEN = NSYM          # 32 bajty parzystości RS

# Preambuła (pierwsze bajty nagłówka); Seq_No zajmuje pozostałe bajty nagłówka.
SYNC_PREAMBLE = b"\xA5\x5A"
