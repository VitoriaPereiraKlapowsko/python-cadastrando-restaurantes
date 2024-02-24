import os

restaurantes = ['Pizza', 'Sushi']

def exibir_nome_do_programa():
    print('''
██████████████████████████████████████████████████████████████████████████
█─▄▄▄▄██▀▄─██▄─▄─▀█─▄▄─█▄─▄▄▀███▄─▄▄─█▄─▀─▄█▄─▄▄─█▄─▄▄▀█▄─▄▄─█─▄▄▄▄█─▄▄▄▄█
█▄▄▄▄─██─▀─███─▄─▀█─██─██─▄─▄████─▄█▀██▀─▀███─▄▄▄██─▄─▄██─▄█▀█▄▄▄▄─█▄▄▄▄─█
▀▄▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▀▄▄▀▀▀▄▄▄▄▄▀▄▄█▄▄▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀
      ''') #Usei o https://fsymbols.com/generators/

def exibir_opcoes():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurantes')
    print('3. Ativar Restaurante')
    print('4. Sair')
    
def finalizar_app(): #ao inves de usar function eu coloco def
    exibir_subtitulo('Finalizando o App')

def voltar_ao_menu_principal():
    input('Digite uma tecla para voltar ao menu ')
    main()
    
def opcao_invalida():
    print('Opção Inválida!!!\n')
    voltar_ao_menu_principal()
    
def exibir_subtitulo(texto):
    os.system('cls') #importei a biblioteca OS para poder limpar o terminal após terminar de executar o programa
    print(texto)
    print()
       
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    restaurantes.append(nome_do_restaurante) #colocando os restaurantes cadastrados dentro da lista
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!!')
    voltar_ao_menu_principal()
    
def listar_restaurantes():
    exibir_subtitulo('Lista de novos restaurantes')
    
    for restaurante in restaurantes:
        print(f'{restaurante}')

    voltar_ao_menu_principal()
    
def escolher_opcoes():
    try: #vai servir para caso a pessoa tenha digitado uma letra ao invés de um número, ai ele tenta fazer isso se não ele pega a opção inválida
        opcao_escolhida = int(input('Escolha uma opção: ')) #Para a pessoa pode escrever e cursor ficar piscandinho, usa snake_case
        #opcao_escolhida = int(opcao_escolhida) pode ser feita assim, no caso estou transformando uma string em um inteiro
        #print('Você escolheu a opção', opcao_escolhida) #Interpolação
        #print(f'Você escolheu a opção {opcao_escolhida}')  ela se faz assim

        if opcao_escolhida == 1 : #Subistituir (){} por : e tirar os ()
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2 : #Elif é um else if
            listar_restaurantes()
        elif opcao_escolhida == 3 : 
            print('Ativar Restaurante')
        elif opcao_escolhida == 4 : 
            finalizar_app()
        else : 
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()
    
if __name__ == '__main__':  #Aqui só estou declarando o meu Main e sim ele tem este padrão para ser declarado...
    main()