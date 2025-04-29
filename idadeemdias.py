def calcular_idade_em_dias():

    anos = int(input("Digite sua idade em anos: "))
    meses = int(input("Digite os meses adicionais: "))
    dias = int(input("Digite os dias adicionais: "))

    DIAS_POR_ANO = 365
    DIAS_POR_MES = 30
    
    idade_em_dias = (anos * DIAS_POR_ANO) + (meses * DIAS_POR_MES) + dias

    print(f"Sua idade expressa apenas em dias é: {idade_em_dias} dias")

calcular_idade_em_dias()
                            
