import os

#restaurantes = ['Pizza', 'Sushi'] aqui era uma lista
restaurantes = [{'nome':'Praça', 'categoria':'Japonesa', 'ativo':False}, #aqui estou usando o conceito de dicionário
                {'nome':'Pizza Suprema', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}] 

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
    print('3. Alternar estado do Restaurante')
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
    linha = '*' * (len(texto)) #len serve para pegar o tamanho e também * multiplicar pela quantidade de elementos que nós temos
    print(linha)
    print(texto)
    print(linha)
    print()
       
def cadastrar_novo_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restairante{nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False} #Regra de negócio em deixar como False
    #restaurantes.append(nome_do_restaurante) #colocando os restaurantes cadastrados dentro da lista
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado com sucesso!!')
    voltar_ao_menu_principal()
    
def listar_restaurantes():
    exibir_subtitulo('Lista de novos restaurantes')
    
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome'] #pegando as informações colocado lá no dicionário de restaurantes
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'-> {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}') #.ljust(20) serve para colocar um espaçamento entre os itens

    voltar_ao_menu_principal()

def alternar_estado_do_restaurante():
    exibir_subtitulo('Alternando o estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo'] #este not vai servir para inverter o valor, ou seja caso o valor seja como False ele obrigatóriamente vai se tornar um True e se ele for um False ele obrigatoriamente vai se tornar um True
            mensagem = f'O restautante {nome_restaurante} foi ativado com sucesso!!!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso' #Conceito de ternário onde coloquei duas possiveis situações uma para caso seja um True e outra caso seja um False
            print(mensagem)
            
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado')
    
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
            alternar_estado_do_restaurante()
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