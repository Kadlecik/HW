def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Testování funkce
num1 = 48
num2 = 18
print(f"Největší společný dělitel {num1} a {num2} je {gcd(num1, num2)}")

print()


#krávy a bývi
import random

# Funkce pro generování tajného čísla
def generovat_cislo():
    return str(random.randint(1000, 9999))

# Funkce pro výpočet býků a krav
def byci_a_kravy(tajne, hadani):
    byci = sum(1 for t, h in zip(tajne, hadani) if t == h)
    kravy = sum(min(tajne.count(c), hadani.count(c)) for c in set(hadani)) - byci
    return byci, kravy

# Hlavní funkce hry
def hra(tajne, pokusy=0):
    hadani = input("Zadejte svůj odhad: ")
    pokusy += 1
    byci, kravy = byci_a_kravy(tajne, hadani)
    print(f"Býci: {byci}, Krávy: {kravy}")
    if byci == 4:
        print(f"Gratuluji! Uhádli jste číslo na {pokusy} pokusů.")
    else:
        hra(tajne, pokusy)

# Spuštění hry
if __name__ == "__main__":
    tajne_cislo = generovat_cislo()
    print("Vítejte ve hře Býci a Krávy!")
    hra(tajne_cislo)

