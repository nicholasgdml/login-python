# login-python

Sistema de login feito 100% em Python, utilizando bibliotecas nativas. Com uma simples "interface" de terminal.

[![Sistema de login Python - @nicholasgdml](https://res.cloudinary.com/marcomontalbano/image/upload/v1645479448/video_to_markdown/images/youtube--bK3hKsxACtk-c05b58ac6eb4c4700831b2b3070cd403.jpg)](https://youtu.be/bK3hKsxACtk "Sistema de login Python - @nicholasgdml")

## Recursos
## "Banco de Dados"
- Todos os dados de usuário e senha serão salvos no arquivo "registros.txt"(Futuramente pretendo implementar um banco de dados).
## "Interface" Terminal
- Calcula a largura do terminal e ajusta linhas e centraliza fontes(salva a medida no momento que o terminal roda a aplicação, as linhas não se redimensionam automaticamente).
- Ao selecionar opções inválidas a aplicação retorna uma mensagem de erro.
- Ultiliza a biblioteca "getpass" para esconder as senhas digitadas.

### Login

- Avisa caso o usuário digitado seja inexistente.
- Avisa caso senha esteja incorreta.

### Registro
- Não permite a criação de usuários repetidos.
- Função para confirmar o registro.
- Tem uma confirmação de senhas, para o usuário não criar um registro com senha errada.



