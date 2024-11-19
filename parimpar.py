def escolher_time(numero_matricula):
    if numero_matricula % 2 == 0:
        print("VOCÊ ESTÁ NO TIME AZUL")
    else:
        print("VOCÊ ESTÁ NO TIME AMARELO")


numero = int(input("Digite o número de matrícula: "))
escolher_time(numero)
