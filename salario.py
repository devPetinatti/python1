def verificar_saldo():
    conta1 = float(input("Digite o valor da primeira conta: R$ "))
    conta2 = float(input("Digite o valor da segunda conta: R$ "))
    conta3 = float(input("Digite o valor da terceira conta: R$ "))
    salario = float(input("Digite o valor do seu salário: R$ "))
    
    total_contas = conta1 + conta2 + conta3
    
    if salario >= total_contas:
        saldo_restante = salario - total_contas
        print(f"Todas as contas foram pagas! Saldo restante: R$ {saldo_restante:.2f}")
    else:
        print("Salário insuficiente!")

verificar_saldo()