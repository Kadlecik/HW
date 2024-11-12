def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Testování funkce
num1 = 48
num2 = 18
print(f"Největší společný dělitel {num1} a {num2} je {gcd(num1, num2)}")
