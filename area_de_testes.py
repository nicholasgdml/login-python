'''opcao = int(input(''))
if opcao == 1:
    #! REGISTRO
    print('registrar')
    registros = open('registros.txt', 'a')

    login = str(input('Digite um novo login: ')).strip()
    senha = str(input('Digite uma nova senha: ')).strip()

    registros.write(f'{login}:{senha}\n')
    registros.close()
    
else:
    #! LOGIN
    while True:
        registros = open('registros.txt', 'r')
        login = str(input('Usuario: ')).strip()
        senha = str(input('Senha: ')).strip()
        conta = f'{login}:{senha}' + '\n'
        if conta in registros.readlines():
            print('Login Concluído!!')
            break
        else:
            print('Login Incorreto!!')      '''
            
print(len('                                           BEM-VINDO                                            '))     
