import filesManager
import caracter_chain
import identifiers
import number
import arithmetic_operators
import relational_operators
import logic_operators
import delimitador
import symbol_table as table

line = 0

print('################## Welcome to Unicorn.io ###################')
lista_arquivos = filesManager.list_files('input')
filesManager.clean_folder('output')


def identify_lexemes(arquivo, symbol_table):
    global line
    line = 1
    while True:
        c = filesManager.read_char()
        if not c:
            print('Fim de arquivo main')
            break
        if c == '\n':
            line = line + 1
        elif c == '\"':
            print('--- Entrou na identificação de cadeia de caracteres')
            caracter_chain.identify(filesManager, c, line, symbol_table)
        elif c.isdigit():
            print('--- Entrou na identificação de número')
            number.identify(filesManager, c, line, symbol_table)
        elif c == '+' or c == '-' or c == '*' or c == '/':
            print('--- Entrou na identificação de operador aritmético')
            arithmetic_operators.identify(filesManager, c, line, symbol_table)
        elif c == '!':
            d = filesManager.read_char()
            filesManager.go_back()
            if d == '=':
                relational_operators.identify(filesManager, c, line, symbol_table)
                # Vai pra operador relacional
            else:
                logic_operators.identify(filesManager, c, line, symbol_table)
                # Vai pra operador lógico
        elif c == '&' or c == '|':
            logic_operators.identify(filesManager, c, line, symbol_table)
            # Vai pra operador lógico
        elif c == '=' or c == '>' or c == '<':
            relational_operators.identify(filesManager, c, line, symbol_table)
            # Vai pra operador relacional
        elif c == ';' or c == ',' or c == '(' or c == ')' or c == '[' or c == ']' or c == '{' or c == '}' or c == '.':
            delimitador.add_table(line, c, symbol_table)
            # Vai para delimitador
        # elif v.is_char(c) or c == '_':
        elif not c == ' ' and not c == '\t':
            print('--- Entrou na identificação de identificador')
            identifiers.identify(filesManager, c, line, symbol_table)
    filesManager.write_symbol_table(symbol_table.get_token(), arquivo)


def clear_comments(file, symbol_table):
    line = 1
    mensagem = ''
    while True:
        c = filesManager.read_char()
        if not c:
            break
        if c == '\n':
            line += 1
        if c == '/':
            c = filesManager.read_char()
            if c == '/':
                while True:
                    if c == '\n':
                        filesManager.go_back()
                        break
                    if not c:
                        break
                    c = filesManager.read_char()
                line += 1
            elif c == '*':
                comentario_line = line
                c = filesManager.read_char()
                d = filesManager.read_char()
                while c != '*' and d != '/':
                    if c == '\n':
                        mensagem += '\n'
                        line += 1
                    c = d
                    d = filesManager.read_char()
                    if not d:
                        symbol_table.add_lexeme('CoMF', 'Fim de arquivo inesperado', comentario_line)
                        break
            else:
                mensagem += c
        else:
            mensagem += c
    filesManager.write(mensagem, 'auxiliar_files\\' + file)


count = 0
tableList = []
for arquivo in lista_arquivos:
    filesManager.open_file('input\\' + arquivo)
    tableList.append(table.SymbolTable())
    clear_comments(arquivo, tableList[count])
    count += 1

lista_arquivos = filesManager.list_files('auxiliar_files')

count = 0
for arquivo in lista_arquivos:
    filesManager.open_file('auxiliar_files\\' + arquivo)
    identify_lexemes(arquivo, tableList[count])
    count += 1
