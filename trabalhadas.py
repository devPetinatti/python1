def calcular_salario():
    turno = input("Digite o seu turno de trabalho (N para Noturno, e D para Diurno): ").strip().upper()
    horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
    
    if turno == 'N':
        valor_hora = 45.00
    else:
        valor_hora = 37.50
    
    salario = horas_trabalhadas * valor_hora
    
    print(f"O valor do salário é: R$ {salario:.2f}")

calcular_salario()