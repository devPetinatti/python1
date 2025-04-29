import math

# Entrada de dados
a = int(input("Digite o valor de a: "))
b = int(input("Digite o valor de b: "))
c = int(input("Digite o valor de c: "))

if a == 0:
    print("Não é equação do segundo grau.")
else:
    delta = b**2 - 4*a*c
    print("Delta =", delta)

    if delta < 0:
        print("Não há raízes reais.")
    else:
        raiz_delta = math.sqrt(delta)
        x1 = (-b + raiz_delta) / (2*a)
        x2 = (-b - raiz_delta) / (2*a)

        if delta == 0:
            print(f"Há uma raiz real: x = {x1}")
        else:
            print(f"Duas raízes reais:")
            print(f"x1 = {x1}")
            print(f"x2 = {x2}")
