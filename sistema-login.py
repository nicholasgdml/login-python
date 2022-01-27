from ast import Try
from time import sleep
import os
import platform


## Altura e largura terminal
largura_terminal, altura_terminal = os.get_terminal_size()

# Declarando variaveis para funçoes
login = ''

def limpar_Terminal():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    

def linha(simbulo='='):
    print(simbulo * int(largura_terminal))
    
    
def cabecalho(frase):
    limpar_Terminal()
    linha()
    tam_palavra = len(frase)
    espaco = (largura_terminal - tam_palavra - 2) / 2
    print(' '*int(espaco), frase, ' '*int(espaco))
    linha()
    
    
def erro(frase):
    limpar_Terminal()
    linha()
    tam_palavra = len(frase)
    espaco = (largura_terminal - tam_palavra - 3) / 2
    print('\033[1;31m '*int(espaco), frase, ' '*int(espaco), '\033[0;0m')
    linha()
    sleep(3)
    


def Login():
    while True:
        cabecalho('Login')
        registros = open('registros.txt', 'r')
        login = str(input('Usuario: ')).strip()
        if UsuarioExitente() == True:
            senha = str(input('Senha: ')).strip()
            conta = f'{login}:{senha}' + '\n'
            if conta in registros.readlines():
                cabecalho('LOGIN CORRETO!!')
                break
            else:
                erro('SENHA INCORRETA!!!')
                if confirmar('Deseja tentar novamente?') == False:
                    break
        else:
            erro('Usuario Inexistente! Tente Novamente')
            if confirmar('Deseja tentar novamente?') == False:
                break   


def UsuarioExitente():
    usuario_existente = ''
    validar_registro = open('registros.txt', 'r')
    for user in validar_registro:
        temp = user.split(':')          
        if login == temp[0]:
            usuario_existente = True
            break
        else: 
            usuario_existente = False
    if usuario_existente == False:
        return False
    elif usuario_existente == True:
        return True
    
        
        
        
def Registro():
    registros = open('registros.txt', 'a')
    while True:
        cabecalho('Registro')
        login = str(input('Digite um novo login: ')).strip()
        if UsuarioExitente() == False:
            senha = str(input('Digite uma nova senha: ')).strip()
            if confirmar('Confirmar registro?') == True:
                registros.write(f'{login}:{senha}\n')
                registros.close()
                cabecalho('Cadastro concluido!!')
                sleep(3)
                break
            else:
                if confirmar('Deseja continuar o registro?') == False:
                    break
        else:
            erro('Usuario ja cadastrado!!')
            if confirmar('Deseja tentar novamente?') == False:
                break
        
        

        
def confirmar(txt='Tem Certeza?'):
    while True:
        cabecalho(txt)
        print('[01]. SIM')
        print('[02]. NAO')
        linha()
        try:
            opcao = int(input('> '))
        except:
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
