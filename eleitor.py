idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Você é não eleitor, ainda não pode votar!")

elif 18 <= idade <= 65:
    print("Você é um eleitor obrigatório!")

else:
    print("Você é um eleitor facultativo.")