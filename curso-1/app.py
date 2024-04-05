import os

restaurantes = []

def exibir_nome():
  print("""
░█████╗░██╗░░██╗██╗███╗░░██╗░█████╗░██╗░░██╗██╗██╗░░░░░░█████╗░
██╔══██╗██║░░██║██║████╗░██║██╔══██╗██║░░██║██║██║░░░░░██╔══██╗
██║░░╚═╝███████║██║██╔██╗██║██║░░╚═╝███████║██║██║░░░░░███████║
██║░░██╗██╔══██║██║██║╚████║██║░░██╗██╔══██║██║██║░░░░░██╔══██║
╚█████╔╝██║░░██║██║██║░╚███║╚█████╔╝██║░░██║██║███████╗██║░░██║
░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝╚═╝╚══════╝╚═╝░░╚═╝

██████╗░███████╗░██████╗████████╗░█████╗░██╗░░░██╗██████╗░░█████╗░███╗░░██╗████████╗███████╗░██████╗
██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗██║░░░██║██╔══██╗██╔══██╗████╗░██║╚══██╔══╝██╔════╝██╔════╝
██████╔╝█████╗░░╚█████╗░░░░██║░░░███████║██║░░░██║██████╔╝███████║██╔██╗██║░░░██║░░░█████╗░░╚█████╗░
██╔══██╗██╔══╝░░░╚═══██╗░░░██║░░░██╔══██║██║░░░██║██╔══██╗██╔══██║██║╚████║░░░██║░░░██╔══╝░░░╚═══██╗
██║░░██║███████╗██████╔╝░░░██║░░░██║░░██║╚██████╔╝██║░░██║██║░░██║██║░╚███║░░░██║░░░███████╗██████╔╝
╚═╝░░╚═╝╚══════╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═════╝░
        """)

def exibir_opcoes():
    print("1. Cadastrar restaurante.")
    print("2. Listar restaurantes")
    print("3. Ativar restaurante")
    print("4. Sair\n")
    
def voltar_ao_menu_principal():
    input("Digite uma tecla para voltar ao menu principal\n")
    print()
    main()

def imprimir_subtitulo(texto):
    print(texto)
    

def cadastrar_restaurantes():
    imprimir_subtitulo("Cadastrando novo resturante\n")
    os.system('cls')
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar:\n")
    restaurantes.append(nome_do_restaurante)
    print(f"Restaurante {nome_do_restaurante} cadastrado com sucesso")
    voltar_ao_menu_principal()
    
def listar_restaurantes():
    os.system('cls')
    imprimir_subtitulo('Listando novos restaurantes')
    for nomes in restaurantes:
        print(nomes)
    voltar_ao_menu_principal()

def opcao_invalida():
    imprimir_subtitulo('opção invalida!')
    voltar_ao_menu_principal()



def escolher_opcoes():
    try:
        opcao_escolhida = int(input("Escolha uma opção\n"))
        print(f'Você escolheu a opção {opcao_escolhida}')
        
        match opcao_escolhida:
            case 1:
                cadastrar_restaurantes()
            case 2:
                listar_restaurantes()
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
    imprimir_subtitulo("Saindo do app")


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
