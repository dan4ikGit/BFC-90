BFC‑90 is an experimental encryption method that transforms input text into a much longer, symbol‑based ciphertext.
Unlike common encryption algorithms, BFC‑90 massively increases the message length. Depending on the use case, this can be seen as either an advantage or a disadvantage.
The key space is designed to provide approximately 90 bits of entropy.
Because this encoder is experimental, I cannot guarantee its structural security or correctness.
It also removes characters that cannot be mapped reliably, which may lead to information loss.
For these reasons, BFC‑90 should not be used for sensitive or security‑critical data.
The goal of this project is to explore unconventional encryption concepts and eventually improve the method through feedback and experimentation.
If you distribute modified versions of this software, please include a clear note that your work is based on or inspired by BFC‑90.

How it works:
The input text is cleaned by removing unsupported characters.
Each remaining character is mapped to a numerical index based on a key‑dependent table.
These numbers are converted into a Brainfuck‑like program.
The Brainfuck symbols are replaced by variable‑length tokens derived from the key.
A deliberately inserted "wrong" symbol disrupts part of the structure to make analysis harder.
The final output is a long, symbol‑heavy ciphertext.

Usage example (Python):
from bfc90 import encode, decode
e = encode("Hello World")
print(e.key)
print(e.code)
d = decode(e.code, e.key)
print(d)

Disclaimer:
BFC‑90 is not a trustworthy or proven encryption method.
It is a research experiment, and I appreciate anyone who contributes to improving it.

Warning:  
This encoder increases the message length extremely — do not underestimate the output size.
