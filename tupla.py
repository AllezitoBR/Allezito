tupla = (15, 25, 35, 45, 55) #criar tupla

lista = list(tupla) #alterar tupla para lista

lista.append(65) #adicionando um número
lista.append(75) #adicionando segundo número

lista.pop(0) #remover o primeiro

lista.pop() #remover o ultimo

primeiro_dado = lista[0] #print do primeiro item da lista

quantidade_dados = len(lista) #print da quantidade de itens na lista

#Criando um dicionário com Nome, Idade, Profissão
dicionario = { 
    "Nome": "Alexandre",
    "Idade": 33,
    "Profissão": "Analista de QA"
} 

valor_chave_nome = dicionario["Nome"] #imprimindo valor da chave "nome" do dicionário

print(primeiro_dado, quantidade_dados, valor_chave_nome)