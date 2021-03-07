import validator as v


def identify(files_manager, c, line, symbol_table):
    word = c
    error = False
    if not v.is_char(c):
        error = True
    while True:
        c = files_manager.read_char()
        if not c:
            print('Fim de arquivo identificador')
            break
        if v.is_delimiter(c) or v.is_logic_operator(c) or v.is_arithmetic_operator(c) or v.is_relacional_operator(
                c) or c == ' ' or c == '\n':
            files_manager.go_back()
            break
        else:
            word += c
        error = check_indentifier(c, error)
    if error:
        symbol_table.add_lexeme('SIB', word, line)
    else:
        if is_keyword(word):
            symbol_table.add_lexeme('PRE', word, line)
        else:
            symbol_table.add_lexeme('IDE', word, line)


def check_indentifier(c, error):
    if not c.isdigit() and not v.is_char(c) and not c == '_':
        return True
    else:
        return error


def is_keyword(word):
    keywords = ['var', 'const', 'typedef', 'struct', 'extends', 'procedure', 'function', 'start',
                'return', 'if', 'else', 'then', 'while', 'read', 'print', 'int', 'real', 'boolean',
                'string', 'true', 'false', 'global', 'local']
    return word in keywords
