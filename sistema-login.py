from time import sleep
import os
from unicodedata import numeric


## Altura e largura terminal
largura_terminal, altura_terminal = os.get_terminal_size()

def limpar_Terminal():
    os.system('clear')
    

def linha(simbulo='='):
    print(simbulo * int(largura_terminal))
    
    
def cabecalho(palavra):
    limpar_Terminal()
    linha()
    tam_palavra = len(palavra)
    espaco = (largura_terminal - tam_palavra - 2) / 2
    print(' '*int(espaco), palavra, ' '*int(espaco))
    linha()


def Login():
    cabecalho('Login')
    while True:
        registros = open('registros.txt', 'r')
        login = str(input('Usuario: ')).strip()
        senha = str(input('Senha: ')).strip()
        conta = f'{login}:{senha}' + '\n'
        if conta in registros.readlines():
            cabecalho('Login Válido')
            
            break
        else:
            print('Login Incorreto!!')
            


def Registro():
    cabecalho('Registro')
    while True:
        registros = open('registros.txt', 'a')
        login = str(input('Digite um novo login: ')).strip()
        senha = str(input('Digite uma nova senha: ')).strip()
        registros.write(f'{login}:{senha}\n')
        registros.close()


def confirmar(txt='Tem Certeza?'):
    while True:
        cabecalho('Tem certeza')
        print('[01]. SIM')
        print('[02]. NAO')
        linha()
        opcao = str(input('> '))
        if opcao is numeric:
            if opcao == 1:
                return True
            else:
                break
        else:
            cabecalho('Digite uma opçao valida!!')
            
    
while True:            
    cabecalho('BEM-VINDO')
    print('[01]. Login')
    print('[02]. Registro')
    print('[03]. Sair')
    linha()
    opcao = str(input('Digite uma opção: '))
    if opcao is numeric:
        if opcao == 1:
            Login()
        if opcao == 2:
            Registro()
        if opcao == 3:
            break
        