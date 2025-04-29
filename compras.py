def calcular_valor_compra():
    valor_compra = float(input("Digite o valor da compra: R$ "))
    
    if valor_compra > 200:
        desconto = valor_compra * 0.20
        valor_final = valor_compra - desconto
        print(f"Você recebeu um desconto de 20%! Valor final da compra: R$ {valor_final:.2f}")
    else:
        print(f"Sem desconto. Valor final da compra: R$ {valor_compra:.2f}")

calcular_valor_compra()
