#1 - Crie um dicionário representando 
# informações sobre uma pessoa, como nome, idade e cidade.

pessoa = {'nome': 'Murilo', 'idade': 20, 'cidade': 'São Paulo'}

#2 - Utilizando o dicionário criado no item 1:
#Modifique o valor de um dos itens no dicionário (por exemplo, atualize a idade da pessoa);
#Adicione um campo de profissão para essa pessoa;
#Remova um item do dicionário.

pessoa['idade'] = '21'
pessoa['profissao'] = 'Programador'
del pessoa['cidade']
print(pessoa)

#3 - Uma possível abordagem para criar um dicionário que apresente 
# os números de 1 a 5 e seus respectivos quadrados é a seguinte:
quadrado ={x: x**2 for x in range(1, 6)}
print(quadrado)

#4 - Crie um dicionário e verifique se uma chave específica 
# existe dentro desse dicionário.

if 'nome' in pessoa:
    print("Essa pessoa tem nome")
else:
    print("esse pessoa não tem nome")


frase = "Python se tornou uma das linguagens de programação mais populares do mundo nos últimos anos."
contagem_palavras = {}
palavras = frase.split()
for palavra in palavras:
    contagem_palavras[palavra] = contagem_palavras.get(palavra, 0) + 1
print(contagem_palavras)
