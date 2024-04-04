import os

def exibir_nome():
  print("Restaurante Top")

def exibir_opcoes():
    print("1. Cadastrar restaurante.")
    print("2. Listar restaurantes")
    print("3. Ativar restaurante")
    print("4. Sair\n")

def opcao_invalida():
    print('opção invalidade!')
    input('Digite uma tecla para voltar ao menu principal')
    main()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input("Escolha uma opção\n"))
        print(f'Você escolheu a opção {opcao_escolhida}')
        
        match opcao_escolhida:
            case 1:
                print('Cadastrando restauerante')
            case 2:
                print("Listando restaurantes")
            case 3:
                print("Ativando Restaurante")
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        opcao_invalida()


''' oi né'''
def finalizar_app():
    os.system('cls')
    print("Saindo do app")


''' if (opcao_escolhida == 1):
    print('Cadastrando restauerante')
elif(opcao_escolhida == 2):
    print("Listando restaurantes")
elif (opcao_escolhida == 3):
    print("Ativando Restaurante")
else:
    print("Saindo do app")
  '''  
def main():
    os.system('cls')
    exibir_nome()
    exibir_opcoes()
    escolher_opcoes()
    
if __name__ == '__main__':
    main()
