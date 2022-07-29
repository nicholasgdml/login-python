from time import sleep
import os
import platform
from getpass import getpass


def limpar_Terminal():
    """Função que limpa o terminal
        Utiliza a biblioteca 'os' para identificar o SO do usuário,
        para assim executar o comando clear/cls"""
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    

def linha(simbolo='='):
    """Faz um print de uma linha feita de qualquer símbolo(padrão '=') que se encaixa perfeitamente no Terminal."""
    global largura_terminal
    largura_terminal, altura_terminal = os.get_terminal_size()
    print(simbolo * int(largura_terminal))
    

def cabecalho(frase):
    """Função apenas estética que limpa o terminal, cria um cabeçalho com linhas e centraliza a frase automaticamente:
    ex:
     =========================================
                    Olá, Mundo!!
     =========================================
    """
    limpar_Terminal()
    linha()
    tam_palavra = len(frase)
    espaco = (largura_terminal - tam_palavra - 2) / 2
    print(' '*int(espaco), frase, ' '*int(espaco))
    linha()
    
    
def erro(frase):
    """Funçao estética que retorna um cabeçalho com a frase na cor vermelha"""
    limpar_Terminal()
    linha()
    tam_palavra = len(frase)
    espaco = (largura_terminal - tam_palavra - 3) / 2
    print('\033[1;31m '*int(espaco), frase, ' '*int(espaco), '\033[0;0m')
    linha()
    sleep(3)


def Login():
    """Função que executa o Login
        Ele lê o arquivo registro.txt e analisa nome por nome/senha por senha, e pode retornar erro caso user/senha estejam incorretos ou até se o user existe o não"""
    global login
    while True:
        cabecalho('Login')
        registros = open('registros.txt', 'r')
        login = str(input('Usuário: ')).strip()
        if UsuarioExitente() == True:
            senha = getpass('Senha: ')
            conta = f'{login}:{senha}' + '\n'
            if conta in registros.readlines():
                cabecalho('LOGIN CORRETO!!')
                sleep(3)
                cabecalho('VOLTANDO AO INICIO...')
                sleep(3)
                break
            else:
                erro('SENHA INCORRETA!!!')
                if confirmar('Deseja tentar novamente?') == False:
                    break
        else:
            erro('Usuário Inexistente! Tente Novamente')
            if confirmar('Deseja tentar novamente?') == False:
                break   

        
def Registro():
    """Função que executa o Registro
    Ela cria o user e senha no arquivo registros.txt(no formato 'user:senha', consegue analisar se o usuário ja foi cadastrado e também tem uma confirmação de senha para o usuário não criar um login errado"""
    global login
    registros = open('registros.txt', 'a')
    while True:
        cabecalho('Registro')
        login = str(input('Digite um novo login: ')).strip()
        if UsuarioExitente() == False:
            senha = getpass('Digite uma nova senha: ')
            confirmar_senha = getpass('Digite novamente a senha: ')
            if senha == confirmar_senha:
                if confirmar('Confirmar registro?') == True:
                    registros.write(f'{login}:{senha}\n')
                    registros.close()
                    cabecalho('Cadastro concluído!!')
                    sleep(3)
                    break
                else:
                    if confirmar('Deseja tentar novamente?') == False:
                        break
            else:
                erro('Senhas não conferem, tente-novamente!!')
                if confirmar('Deseja tentar novamente?') == False:
                    break
        else:
            erro('Usuario ja cadastrado!!')
            if confirmar('Deseja tentar novamente?') == False:
                break
        
        
def UsuarioExitente():
    """Análisa todos os users e análisa se aquele user foi utilizado, retornando True ou False"""
    usuario_existente = None
    validar_registro = open('registros.txt', 'r')
    for user in validar_registro:
        temp = user.split(':')          
        if login == temp[0]:
            usuario_existente = True
            break
        else: 
            usuario_existente = False
    if usuario_existente:
        return True
    return False
        
        
def confirmar(txt='Tem Certeza?'):
    """Função que com um menu simples de sim ou não, que retorna True ou False"""
    while True:
        cabecalho(txt)
        print('[01]. SIM')
        print('[02]. NAO')
        linha()
        try:
            opcao = int(input('> '))
        except ValueError:
            erro('Digite uma opção válida')
        if opcao == 1:
            return True
        elif opcao == 2:
            return False
        else:
            erro('Digite uma opçao valida!!')
            
    
while True:            
    cabecalho('BEM-VINDO')
    print('[1]. Login')
    print('[2]. Registro')
    print('[3]. Sair')
    linha()
    opcao = str(input('Digite uma opção: '))
    if opcao.isnumeric():
        opcao = opcao.replace('0', '')
        if opcao == '1':
            Login()
        elif opcao == '2':
            Registro()
        elif opcao == '3':
            if confirmar('Deseja sair??') == True:
                break
        else:
            erro('Digite uma opçao valida!!')
    else:
        erro('Digite uma opçao valida!!')
