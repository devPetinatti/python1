positivos = 0
negativos = 0
menor = None

print("Digite valores reais (digite 0 para encerrar):")

while True:
    valor = float(input("Digite um valor: "))
    
    if valor == 0:
        break  
    
    if valor > 0:
        positivos += 1
    elif valor < 0:
        negativos += 1

    if (menor is None) or (valor < menor):
        menor = valor


print("\nQuantidade de valores positivos:", positivos)
print("Quantidade de valores negativos:", negativos)
if menor is not None:
    print("O menor valor digitado foi:", menor)
else:
    print("Nenhum valor foi digitado.")
