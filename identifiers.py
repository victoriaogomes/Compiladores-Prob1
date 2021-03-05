import validator as v


def mensagemErro(numero):
    print('\nErro na léxico no caractere de numero:', numero)


def identify(files_manager, c):
    word = c
    error = False
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
        # TODO: adicionar erro léxico de identificador na tabela de simbolos
        print("Erro no token:", word)
    else:
        if is_keyword(word):
            # TODO: adicionar palavra reservada lida corretamente na tabela de simbolos
            print('Palavra reservada lida corretamente:', word)
        else:
            # TODO: adicionar identificador lido corretamente na tabela de simbolos
            print('Identificador lido corretamente:', word)


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
