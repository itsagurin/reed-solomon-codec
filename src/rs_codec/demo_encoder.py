"""Demo enkodera RS(255, 223): koduje przykładową ramkę i pokazuje wynik w hex."""

from rs_codec.config import K, NSYM
from rs_codec.gf28_math import gf_pow, poly_eval
from rs_codec.rs_encoder import encode, generator_poly


def hexdump(data, width=16):
    for i in range(0, len(data), width):
        chunk = data[i:i + width]
        print(f"{i:3d}: " + " ".join(f"{b:02X}" for b in chunk))


def syndromes(word):
    return [poly_eval(word, gf_pow(2, i)) for i in range(NSYM)]


header = [0x1A, 0xCF, 0xFC, 0x1D]                         # 4 B: przykładowa preambuła
text = b"Ala ma kota, a kot ma Ale. Hello Reed-Solomon!"
payload = list(text) + [0] * (219 - len(text))            # 219 B: tekst dopełniony zerami
message = header + payload                                # 223 B = K

print(f"Wielomian generujący G(x) ({NSYM + 1} współczynników):")
hexdump(generator_poly())

codeword = encode(message)
print(f"\nSłowo kodowe: {len(codeword)} B (dane {K} B + parzystość {NSYM} B)")
print("\nDane (nagłówek + payload):")
hexdump(codeword[:K])
print("\nParzystość (ostatnie 32 B ramki):")
hexdump(codeword[K:])

print("\nSyndromy poprawnego słowa: wszystkie zero?", all(s == 0 for s in syndromes(codeword)))

corrupted = list(codeword)
corrupted[10] ^= 0xFF                                     # psujemy jeden bajt
print("Syndromy po uszkodzeniu bajtu 10: wszystkie zero?", all(s == 0 for s in syndromes(corrupted)))