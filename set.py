valor = {1,1,2,3,"python"}
conjunto = valor

print(valor)

#fruta
lista = ["banana", "pera", "maça", "laranja"]

def add_fruta(a,b):
    lista.append(a)
    lista.append(b)
    print(lista)

add_fruta("limão", "camarão")

def del_ul_fruta():
    lista.pop()
    print(lista)

del_ul_fruta()


def del_fruta(a):
    lista.remove(a)
    print(lista)

del_fruta("pera")

for frutas in lista:
    print(f"Os elementos contidos na lista são: {frutas}")

#texto
var_txt = "texto"
for letras in var_txt:
    print(letras)

#dicionário
dicionario = {"nome": "Caique", "idade": 22}

for chave in dicionario:
    print(f"As chaves neste dicionário são: {chave}")

for w in dicionario.values():
    print(f"Os valores neste dicionário são: {w}")

#itens
for chave,valor in dicionario.items():
    print(dicionario["idade"])
    print(dicionario["nome"])
    print(f"chave: {chave}, valor: {valor}")

