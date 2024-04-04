num = int(input("digite um número: "))

if (num%2==0):
    print(f"{num} é par")
else:
    print(f"{num} é impar")

idade = int(input("Qual sua idade: "))

if (idade<=12):
    print("Você é criança")
elif (idade >= 13) & (idade <= 18):
    print("você é adolecente")
elif (idade > 18):
    print("você é adulto")

nome_de_usuario_inserido = input("Digite um nome de Usuário\n")
senha_do_usuario_inserido = input("Digite uma senha\n")

nome_de_usuario = "Ruffus"
senha = "Pituco22"

if nome_de_usuario_inserido == nome_de_usuario_inserido and senha_do_usuario_inserido == senha:
    print(f"Bem vindo {nome_de_usuario}")
else:
    print("Usuário Inválido")
    
x = float(input('informe o x\n'))
y = float(input('informe o y\n'))


if x>0 and y>0:
    print("Primeiro Quadrante")
elif x<0 and y>0:
    print("Segundo Quadrante")
elif x<0 and x<0:
    print("Terceiro Quadrante")
elif x<0 and y<0:
    print("Quarto Quadrante")
else:
    print("Marco Zero")