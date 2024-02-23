import os

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
    os.system('cls') #importei a biblioteca OS para poder limpar o terminal após terminar de executar o programa
    print('Finalizando o App\n')

def opcao_invalida():
    print('Opção Inválida!!!\n')
    input('Digite uma tecla para voltar ao menu principal')
    main()

def escolher_opcoes():
    try: #vai servir para caso a pessoa tenha digitado uma letra ao invés de um número, ai ele tenta fazer isso se não ele pega a opção inválida
        opcao_escolhida = int(input('Escolha uma opção: ')) #Para a pessoa pode escrever e cursor ficar piscandinho, usa snake_case
        #opcao_escolhida = int(opcao_escolhida) pode ser feita assim, no caso estou transformando uma string em um inteiro
        #print('Você escolheu a opção', opcao_escolhida) #Interpolação
        #print(f'Você escolheu a opção {opcao_escolhida}')  ela se faz assim

        if opcao_escolhida == 1 : #Subistituir (){} por : e tirar os ()
            print('Cadastrar Restaurante')
        elif opcao_escolhida == 2 : #Elif é um else if
            print('Listar Restaurantes')
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
    
if __name__ == '__main__':
    main()