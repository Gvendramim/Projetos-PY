import os
import json
from colorama import Fore, Style, init # type: ignore

init(autoreset=True)

ARQUIVO_RESTAURANTES = 'restaurantes.json'

def carregar_restaurantes():
    if os.path.exists(ARQUIVO_RESTAURANTES):
        with open(ARQUIVO_RESTAURANTES, 'r') as arquivo:
            return json.load(arquivo)
    return []

def salvar_restaurantes():
    with open(ARQUIVO_RESTAURANTES, 'w') as arquivo:
        json.dump(restaurantes, arquivo, indent=4)

restaurantes = carregar_restaurantes()

def exibir_nome():
    print(Fore.CYAN + Style.BRIGHT + 'Sabor Express\n')

def exibir_opcao():
    print('1. Cadastrar Restaurantes')
    print('2. Listar Restaurantes')
    print('3. Alterar Estado do Restaurante')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo('Finalizando App...')
    print(Fore.GREEN + 'Até logo!')

def pausar():
    input(Fore.YELLOW + '\nPressione Enter para continuar...')

def opcao_invalida():
    print(Fore.RED + 'Opção inválida!\n')
    pausar()

def exibir_subtitulo(texto):
    os.system('cls' if os.name == 'nt' else 'clear')
    linha = '*' * len(texto)
    print(Fore.MAGENTA + linha)
    print(Fore.MAGENTA + texto)
    print(Fore.MAGENTA + linha)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')

    if any(r['nome'].lower() == nome_do_restaurante.lower() for r in restaurantes):
        print(Fore.RED + 'Esse restaurante já está cadastrado!')
        return pausar()
    
    categoria = input(f'Digite a categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome': nome_do_restaurante, 'categoria': categoria, 'ativo': False}
    restaurantes.append(dados_do_restaurante)
    salvar_restaurantes()
    print(Fore.GREEN + f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    pausar()

def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes')

    print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
    print('-' * 60)
    for restaurante in sorted(restaurantes, key=lambda r: r['nome'].lower()):
        nome = restaurante['nome']
        categoria = restaurante['categoria']
        status = Fore.GREEN + 'Ativado' if restaurante['ativo'] else Fore.RED + 'Desativado'
        print(f"{nome.ljust(22)} | {categoria.ljust(20)} | {status}")
    
    pausar()

def alternar_estado_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante.lower() == restaurante['nome'].lower():
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            salvar_restaurantes()
            status = 'ativado' if restaurante['ativo'] else 'desativado'
            print(Fore.GREEN + f'O restaurante {restaurante["nome"]} foi {status} com sucesso.')
            break

    if not restaurante_encontrado:
        print(Fore.RED + 'O restaurante não foi encontrado.')

    pausar()

def escolher_opcao():
    try:
        opcao = int(input('Escolha uma opção: '))
        if opcao == 1:
            cadastrar_novo_restaurante()
        elif opcao == 2:
            listar_restaurantes()
        elif opcao == 3:
            alternar_estado_restaurante()
        elif opcao == 4:
            finalizar_app()
            return False
        else:
            opcao_invalida()
    except ValueError:
        print(Fore.RED + 'Você deve digitar um número válido.')
        pausar()
    return True

def main():
    continuar = True
    while continuar:
        os.system('cls' if os.name == 'nt' else 'clear')
        exibir_nome()
        exibir_opcao()
        continuar = escolher_opcao()

if __name__ == '__main__':
    main()
