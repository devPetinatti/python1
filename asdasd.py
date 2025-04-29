
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operacao = input("Escolha a operação (+, -, *, /): ")

if operacao == '+':
    resultado = num1 + num2
    print("Resultado:", resultado)
elif operacao == '-':
    resultado = num1 - num2
    print("Resultado:", resultado)
elif operacao == '*':
    resultado = num1 * num2
    print("Resultado:", resultado)
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
        print("Resultado:", resultado)
    else:
        print("Erro: divisão por zero não é permitida.")
else:
    print("Operação inválida.")
