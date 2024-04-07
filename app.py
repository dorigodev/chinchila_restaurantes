import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Petis','categoria':'Hambuguer','ativo':True}]

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
    print("3. Alternar estados do e restaurante")
    print("4. Sair\n")
    
def voltar_ao_menu_principal():
    input("Digite uma tecla para voltar ao menu principal\n")
    print()
    main()

def imprimir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto) + 4)
    print(linha)
    print(texto)
    print(linha)
    print()
    

def cadastrar_restaurantes():
    imprimir_subtitulo("Cadastrando novo restaurante\n")
    os.system('cls' if os.name == 'nt' else 'clear')  # Melhoria para funcionar em todos os sistemas operacionais
    nome_do_restaurante = input("Digite o nome do restaurante que deseja cadastrar:\n")
    categoria_do_restaurante = input(f'Digite a categoria do restaurante {nome_do_restaurante}:\n')
    dados_do_retaurante = {'nome': nome_do_restaurante, 'categoria': categoria_do_restaurante, 'ativo': False}  # Correção aqui
    restaurantes.append(dados_do_retaurante)
    print(restaurantes)
    print(f"Restaurante {nome_do_restaurante} cadastrado com sucesso")
    voltar_ao_menu_principal()
    
    voltar_ao_menu_principal()
    
def listar_restaurantes():
    imprimir_subtitulo('Listando novos restaurantes')
    print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
    for nomes in restaurantes:
        nome_do_restaurante = nomes['nome']
        categoria_do_restaurante = nomes['categoria']
        status_do_restaurante = 'ativado' if nomes['ativo'] else 'desativado'
        print(f' - {nome_do_restaurante.ljust(20)} | {categoria_do_restaurante.ljust(20)} | {status_do_restaurante}')
        
    voltar_ao_menu_principal()

def opcao_invalida():
    imprimir_subtitulo('opção invalida!')
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    imprimir_subtitulo("Alternando estado do Restaurante")
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
            
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
            
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
                alternar_estado_restaurante()
            case 4:
                finalizar_app()
            case _:
                opcao_invalida()
    except:
        #erro está aqui
            opcao_invalida()


''' oi né'''
def finalizar_app():
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
