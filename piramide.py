h = float(input("Digite a altura do tronco da pirâmide: "))
bm = float(input("Digite o valor da base menor da pirâmide: "))
bM = float(input("Digite o valor da base maior da pirâmide: "))

volume = (h / 3) * (bM**2 + bm**2 + (bM * bm))

print("O valor do volume é: ", volume)