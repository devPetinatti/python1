produto = input("Digite o nome do produto: ")
valor = float(input("Digite o valor: "))

if valor < 10:
    lucro = 0.70

elif valor < 30:
    lucro = 0.50

elif valor < 50:
    lucro = 0.40

else:
    lucro = 0.30

venda = valor * (1+ lucro)

print(f"Produto: {produto}")
print(f"Valor da compra: R$ {valor:.2f}")
print(f"Lucro aplicado: {int(lucro * 100)}%")
print(f"Valor da venda: R$ {venda:.2f}")