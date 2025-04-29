
for numero in range(0, 101, 2):
    print(numero)


for i in range(1, 51):
    print(i)

for i in range(52, 101, 2):
    print(i)



n = int(input("Digite um número inteiro e positivo: "))


if n > 0:
    soma = 0
    for i in range(1, n + 1):
        soma += 1 / i
    print(f"A soma S = {soma}")
else:
    print("Por favor, digite um número inteiro **positivo**.")

