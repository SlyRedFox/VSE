import math

def evklid(e, φ):
    data = [e, φ]
    a, b = max(data), min(data)
    q, r, x, y = "-", "-", "-", "-"
    x2, x1, y2, y1 = 1, 0, 0, 1
    print(f"q={q}, r={r}, x={x}, y={y}, a={a}, b={b}, x2={x2}, x1={x1}, y2={y2}, y1={y1} ")
    while b != 0:
        q, r = (a // b), (a % b)
        x = (x2 - q * x1)
        y = (y2 - q * y1)
        a, b, x2, y2, x1, y1 = b, r, x1, y1, x, y
        print(f"q={q}, r={r}, x={x}, y={y}, a={a}, b={b}, x2={x2}, x1={x1}, y2={y2}, y1={y1} ")
    d = y2
    return d

print(f"Гененеция ключей ")
def gen_key(p, q):
    print(f"    1) Выбор простых чисел: p = {p}, q = {q} ")
    n = p * q
    print(f"    2) Вычисление n путем произведения p на q:")
    print(f"𝑛 = 𝑝•𝑞 = {p} * {q} = {n}")
    φ = (p-1)*(q-1)
    print(f"    3) Вычисления функции Эйлера от n:")
    print(f"φ(𝑛) = (𝑝 − 1)•(𝑞 − 1) = {p-1}•{q-1} = {φ} ")
    print(f"    4)Выбор целого простого числа числа e, которое взаимно простое φ(n):")
    e = 149 # меняем по таблице простых чисел
    print(f"e = {e}" )
    print(f"    5)Найти экспоненту расшифрования d, удовлетворяющею условию e•d≡ 1(mod φ(n) )")
    print(      f"          Расширенный алгоритм Евклида")
    d = evklid(e, φ)
    print()
    print(f"d = e^(-1) mod (𝑛) = {e}^(-1) mod {φ} = {d}")
    print("###")
    print(f"Переписывать не надо. print(pow({e}, -1, {φ})) = {pow(e, -1, φ)}")
    print("###")
    print()
    data_key = {"open_key": (e, n), "close_key": (d, n)}
    print(f"    6)Генерация ключей")
    print(f"Публичный ключ  = (e,n) = ({e}, {n})")
    print(f"Частный ключ = (d,n) = ({d}, {n})")
    return data_key


print()
def encryption(data_key,work ):
    e = data_key["open_key"][0]
    n = data_key["open_key"][1]
    data_work = []
    for i in range(len(work)):
        letter = bin(ord(work[i]))[2:]
        letter = letter.zfill(8)
        print(f" {work[i]} = в аски коды {ord(work[i])} = в бинарном виде {letter} ")
        data_work.append(letter)
    print(" | ".join(data_work))
    len_block = (math.floor(math.log(n, 2)))
    print(f"Длина блока = ⌊𝑙𝑜𝑔 2𝑛⌋ = ⌊𝑙𝑜𝑔 {n}⌋ = {len_block}")
    data_work = "".join(data_work)
    if len(data_work)%len_block != 0:
        coint = len_block - len(data_work)%len_block # ????????????????7
        print(coint)
        data_work = "0"*coint + data_work
    print(f'      {data_work}')
    data = []
    coint = 1
    for i in range(len(data_work),0, -len_block):
        number = data_work[i - len_block:i]
        num = int(number, 2)
        print(f"        m{coint} = {number} = {num}")
        data.append(num)
        coint += 1
    print(f"             𝑐𝑖 = 𝑚𝑖 ^𝑒 𝑚𝑜𝑑 𝑛 ")
    data_work = []
    coint = 1
    print(f"Длина блока = ⌊𝑙𝑜𝑔 2𝑛⌋ + 1 = ⌊𝑙𝑜𝑔 {n}⌋ = {len_block + 1}")
    for m in data:
        num = pow(m,e,n)
        number = bin(num)[2:].zfill(len_block+1)
        data_work.append(number)
        print(f"c{coint} = {m}^{e} mod {n} = {number} ")
        coint += 1
    print(f'        {" | ".join(data_work)}')
    print(f'         {"".join(data_work)}')
def main():
    work = "Home"
    p, q = 271, 307 # меняем по таблице простых чисел
    data_key = gen_key(p, q)
    print()
    print(f"Зашифрование")
    encryption(data_key, work)
main()