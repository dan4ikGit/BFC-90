import re, random, math, hashlib
class encode:
    def __init__(self, text):
        sizes = [10, 10, 10, 10, 3]
        digits_0_9 = list(range(10))
        digits_0_2 = list(range(3))
        key_digits = []
        for size in sizes:
            if size == 3:
                block = random.sample(digits_0_2, size)
            else:
                block = random.sample(digits_0_9, size)
            key_digits.extend(block)
        key = "".join(str(d) for d in key_digits)
        ct = re.sub(r'[^A-Za-z0-9\s.,!?\-\']', '', text)
        ct = re.sub(r'\s+', ' ', ct).strip()
        idx = {
            "a": int(key[0])+10,
            "b": int(key[1])+10,
            "c": int(key[2])+10,
            "d": int(key[3])+10,
            "e": int(key[4])+10,
            "f": int(key[5])+10,
            "g": int(key[6])+10,
            "h": int(key[7])+10,
            "i": int(key[8])+10,
            "j": int(key[9])+10,
            "k": int(key[10])+20,
            "l": int(key[11])+20,
            "m": int(key[12])+20,
            "n": int(key[13])+20,
            "o": int(key[14])+20,
            "p": int(key[15])+20,
            "q": int(key[16])+20,
            "r": int(key[17])+20,
            "s": int(key[18])+20,
            "t": int(key[19])+20,
            "u": int(key[20])+30,
            "v": int(key[21])+30,
            "w": int(key[22])+30,
            "x": int(key[23])+30,
            "y": int(key[24])+30,
            "z": int(key[25])+30,
            "0": int(key[26])+30,
            "1": int(key[27])+30,
            "2": int(key[28])+30,
            "3": int(key[29])+30,
            "4": int(key[30])+40,
            "5": int(key[31])+40,
            "6": int(key[32])+40,
            "7": int(key[33])+40,
            "8": int(key[34])+40,
            "9": int(key[35])+40,
            " ": int(key[36])+40,
            "!": int(key[37])+40,
            "?": int(key[38])+40,
            ".": int(key[39])+40,
            ",": int(key[40])+50,
            "'": int(key[41])+50,
            "-": int(key[42])+50
        }
        kqs = sum(int(n) for n in str(abs(int(key))))
        if kqs >= 10:
            while kqs >= 10:
                kqs = sum(int(n) for n in str(abs(kqs)))
        s = "".join(f"{idx[mch.lower()]:02d}" for mch in ct)
        random.seed(key)
        syms = list("!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~")
        syms += ["§","±","µ","¶","¿","×","÷","¤","¢","£","¥","©","®","™","•","‰","†","‡","∞","≠","≈","≤","≥"]
        mrkc = [c for c in syms]
        mrk = random.choice(mrkc)
        symsc = [c for c in syms if c != mrk]
        def best_factor(n):
            factors = [(a, n // a) for a in range(1, int(n**0.5) + 1) if n % a == 0]
            return max(factors, key=lambda x: x[0])
        bf_pgm = []
        n = []
        for i, ch in enumerate(s):
            n.append(str(ch))
            val = ord(ch)
            a, b = best_factor(val)
            bf = []
            mode = int(key[i % len(key)]) % 5
            if mode == 0:
                bf += ["+"] * a
                bf += ["["]
                bf += [">"] + ["+"] * b + ["<", "-"]
                bf += ["]"]
            elif mode == 1:
                bf += ["+"] * b
                bf += ["["]
                bf += ["<"] + ["+"] * a + [">", "-"]
                bf += ["]"]
            elif mode == 2:
                bf += ["+"] * val
            elif mode == 3:
                bf += ["+"] * (a)
                bf += ["["]
                bf += [">"] + ["+"] * (b // 2) + ["<", "-"]
                bf += ["]"]
                bf += ["+"] * (b % 2)
            elif mode == 4:
                bf += ["+"] * (a // 2)
                bf += ["["]
                bf += [">"] + ["+"] * (b) + ["<", "-"]
                bf += ["]"]
                bf += ["+"] * 2 + ["-"] * 2 
                bf += ["-"] * (2 + (a % 2))
            bf_pgm.append("".join(bf))
            bf_pgm.append(">" * 2)
        bf_full = "".join(bf_pgm)
        def crt(i, l):
            t = ""
            for j in range(l):
                k = int(key[(i + j) % len(key)])
                mix = (i * 1315423911) ^ (j * 2654435761) ^ (k * 97531)
                ip = abs(mix) % len(symsc)
                t += symsc[ip]
            return t
        bal = {
            ">": 1,
            "<": 2,
            "+": 3,
            "-": 4,
            ".": 5,
            "[": 6,
            "]": 7
        }
        ap = [48,59,50,51,52,53,54,55,56,57]
        k0 = key_digits[0]
        if math.isqrt(k0)**2 == k0:
            raw_val = ap[k0] + k0
        else:
            raw_val = ap[10 - k0] - k0
        ts = []
        for pos, ch in enumerate(bf_full):
            bl = bal[ch]
            o = int(key[pos % len(key)]) % 3
            length = bl + o
            t = crt(pos, length)
            ts.append(t)
        tk_full = mrk.join(ts)
        sym = "?" if raw_val % 3 == 0 else ("." if raw_val % 2 == 0 else "!")
        raw_pidx = raw_val % (len(tk_full) + 1)
        pidx = (raw_pidx // 2) * 2
        cl = list(tk_full)
        cl.insert(pidx, sym)
        self.code = "".join(cl)
        self.key = key
        self.bf_pgm = "".join(bf_pgm)
    def __str__(self):
        return f"{self.key}\n{self.code}"

class decode:
    def __init__(self, text, key):
        idx = {
            int(key[0])+10: "a",
            int(key[1])+10: "b",
            int(key[2])+10: "c",
            int(key[3])+10: "d",
            int(key[4])+10: "e",
            int(key[5])+10:"f",
            int(key[6])+10: "g",
            int(key[7])+10: "h",
            int(key[8])+10: "i",
            int(key[9])+10: "j",
            int(key[10])+20: "k",
            int(key[11])+20: "l",
            int(key[12])+20: "m",
            int(key[13])+20: "n",
            int(key[14])+20: "o",
            int(key[15])+20: "p",
            int(key[16])+20: "q",
            int(key[17])+20: "r",
            int(key[18])+20: "s",
            int(key[19])+20: "t",
            int(key[20])+30: "u",
            int(key[21])+30: "v",
            int(key[22])+30: "w",
            int(key[23])+30: "x",
            int(key[24])+30: "y",
            int(key[25])+30: "z",
            int(key[26])+30: "0",
            int(key[27])+30: "1",
            int(key[28])+30: "2",
            int(key[29])+30: "3",
            int(key[30])+40: "4",
            int(key[31])+40: "5",
            int(key[32])+40: "6",
            int(key[33])+40: "7",
            int(key[34])+40: "8",
            int(key[35])+40: "9",
            int(key[36])+40: " ",
            int(key[37])+40: "!",
            int(key[38])+40: "?",
            int(key[39])+40: ".",
            int(key[40])+50: ",",
            int(key[41])+50: "'",
            int(key[42])+50: "-"
        }
        key_digits = [int(d) for d in key]
        ap = [48,59,50,51,52,53,54,55,56,57]
        k0 = key_digits[0]
        if math.isqrt(k0)**2 == k0:
            raw_val = ap[k0] + k0
        else:
            raw_val = ap[10 - k0] - k0
        raw_pidx = raw_val % len(text)
        pidx = (raw_pidx // 2) * 2
        ktext = text[:pidx] + text[pidx+1:]
        syms = list("!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~")
        syms += ["§","±","µ","¶","¿","×","÷","¤","¢","£","¥","©","®","™","•","‰","†","‡","∞","≠","≈","≤","≥"]
        random.seed(key)
        mrkc = [c for c in syms]
        mrk = random.choice(mrkc)
        ts = ktext.split(mrk)
        def crt(i, l):
            t = ""
            for j in range(l):
                k = int(key[(i + j) % len(key)])
                mix = (i * 1315423911) ^ (j * 2654435761) ^ (k * 97531)
                ip = abs(mix) % len(syms)
                t += syms[ip]
            return t
        ibal = {
            1: ">",
            2: "<",
            3: "+",
            4: "-",
            5: ".",
            6: "[",
            7: "]"
        }
        bf = []
        for pos, t in enumerate(ts):
            if t == "":
                continue
            length = len(t)
            o = int(key[pos % len(key)]) % 3
            base = length - o
            ch = ibal[base]
            bf.append(ch)
        bftext = "".join(bf)
        blocks = bftext.split(">>")
        def cls(blk, i, s):
            count = 0
            while i < len(blk) and blk[i] == s:
                count += 1
                i += 1
            return count, i
        def dcb(blk, m):
            i = 0
            if m == 0:
                a, i = cls(blk, i, "+")
                i += 2
                b, i = cls(blk, i, "+")
                i += 3
                val = a * b
            elif m == 1:
                b, i = cls(blk, i, "+")
                i += 2
                a, i = cls(blk, i, "+")
                i += 3
                val = a * b
            elif m == 2:
                val, i = cls(blk, i, "+")
            elif m == 3:
                a, i = cls(blk, i, "+")
                i += 2 
                b0, i = cls(blk, i, "+")
                i += 3
                r, i = cls(blk, i, "+")
                b = b0 * 2 + r
                val = a * b
            elif m == 4:
                a0, i = cls(blk, i, "+")
                i += 2
                b, i = cls(blk, i, "+")
                i += 3
                i += 4
                r, i = cls(blk, i, "-")
                a = 2 * a0 + r - 2
                val = a * b
            return val
        n_chars = []
        for pos, blk in enumerate(blocks):
            if not blk:
                continue
            mode = int(key[pos % len(key)]) % 5
            val = dcb(blk, mode)
            n_chars.append(chr(val))
        n = "".join(n_chars)
        pairs = re.findall(r"\d{2}", n)
        self.code = "".join(idx[int(p)] for p in pairs)
    def __str__(self):
        return self.code
