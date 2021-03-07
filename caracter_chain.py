import validator as v


def identify(files_manager, c, line, symbol_table):
    error = False
    caracteres = c
    while True:
        c = files_manager.read_char()
        if not c:
            break
        if c == '\"' and caracteres[-1] != '\\':
            caracteres += c
            break
        else:
            caracteres += c
            error = check_chain(c, error)
    if error:
        # TODO: Adicionar erro léxico na identificação de caracteres
        symbol_table.add_lexeme('CMF', caracteres, line)
    else:
        # TODO: Adicionar cadeia de caracteres na tabela de símbolos
        symbol_table.add_lexeme('CAD', caracteres, line)


def check_chain(c, error):
    if not v.is_char(c) and not c.isdigit() and not ord(c) == 32 and not ord(c) == 33 and not (35 <= ord(c) <= 126):
        return True
    else:
        return error
