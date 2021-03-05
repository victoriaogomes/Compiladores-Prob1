import filesManager
import caracter_chain
import validator as v
import identifiers
import numbers
import arithmetic_operators

lista_arquivos = filesManager.list_files('input')


def identify_lexemes():
    while True:
        c = filesManager.read_char()
        if not c:
            print('Fim de arquivo main')
            break
        if c == '\"':
            print('--- Entrou na identificação de cadeia de caracteres')
            caracter_chain.identify(filesManager, c)
        elif v.is_char(c):
            print('--- Entrou na identificação de identificador')
            identifiers.identify(filesManager, c)
        elif c.isdigit():
            print('--- Entrou na identificação de número')
            numbers.identify(filesManager, c)
        elif c == '+' or c == '-' or c == '*' or c == '/':
            print('--- Entrou na identificação de operador aritmético')
            arithmetic_operators.identify(filesManager, c)
        elif c == '!':
            d = filesManager.read_char()
            filesManager.go_back()
            if d == '=':
                # Vai pra operador relacional
            else:
                # Vai pra operador lógico
        elif c == '&' or c == '|':
            # Vai pra operador lógico
        elif c == '=' or c == '>' or c == '>':
            # Vai pra operador relacional
        elif c == ';' or c == ',' or c == '(' or c == ')' or c == '[' or c == ']' or c == '{' or c == '}' or c == '.':
            # Vai para delimitador


def clear_comments(arquivo):
    mensagem = ''
    while True:
        c = filesManager.read_char()
        if not c:
            break
        if c == '/':
            c = filesManager.read_char()
            if c == '/':
                while c != '\n':
                    c = filesManager.read_char()
            elif c == '*':
                c = filesManager.read_char()
                d = filesManager.read_char()
                while c != '*' and d != '/':
                    c = d
                    d = filesManager.read_char()
                    if not d:
                        print('error final inesperado')
                        break
            else:
                mensagem += c
        else:
            mensagem += c
    filesManager.write(mensagem, 'auxiliar_files\\' + arquivo)


for arquivo in lista_arquivos:
    filesManager.open_file('input\\' + arquivo)
    clear_comments(arquivo)

lista_arquivos = filesManager.list_files('auxiliar_files')

for arquivo in lista_arquivos:
    filesManager.open_file('auxiliar_files\\' + arquivo)
    identify_lexemes()
