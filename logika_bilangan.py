import math

def cek_prima(n):
    if n <= 1:
        return False
    for i in range(2, int(math.isqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def cek_paritas(x):
    if x % 2 == 0:
        return "Bilangan Genap"
    else:
        return "Bilangan Ganjil"
