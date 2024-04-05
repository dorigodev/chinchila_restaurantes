#5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

numero_do_usuario = int(input("Digite um número\n"))

for i in range(1, 11):
    print(f'{i} * {numero_do_usuario} = {i * numero_do_usuario}')