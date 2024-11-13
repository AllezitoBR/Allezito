nome = input("Qual o nome do Aluno: ")

nota1 = float(input("Qual a sua nota: "))
nota2 = float(input("Qual a sua nota: "))
nota3 = float(input("Qual a sua nota: "))
nota4 = float(input("Qual a sua nota: "))

media = nota1 + nota2 + nota3 + nota4
media_final = media / 4

print("Olá, " , nome, "Sua média é: " , media_final , "pontos")