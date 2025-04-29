soma_altura_mulheres = 0
soma_altura_homens = 0
cont_mulheres = 0
cont_homens = 0

print("Digite os dados das pessoas. Para encerrar, digite 'fim' no campo de sexo.")

while True:
    sexo = input("Sexo (M/F): ").strip().lower()
    
    if sexo == 'fim':
        break

    if sexo != 'm' and sexo != 'f':
        print("Sexo inválido. Digite 'M' para masculino ou 'F' para feminino.")
        continue

    try:
        altura = float(input("Altura (em metros): "))
    except ValueError:
        print("Altura inválida. Tente novamente.")
        continue

    if sexo == 'f':
        soma_altura_mulheres += altura
        cont_mulheres += 1
    elif sexo == 'm':
        soma_altura_homens += altura
        cont_homens += 1

if cont_mulheres > 0:
    media_mulheres = soma_altura_mulheres / cont_mulheres
    print(f"\nAltura média das mulheres: {media_mulheres:.2f} m")
else:
    print("\nNenhuma mulher informada.")

if cont_homens > 0:
    media_homens = soma_altura_homens / cont_homens
    print(f"Altura média dos homens: {media_homens:.2f} m")
else:
    print("Nenhum homem informado.")
