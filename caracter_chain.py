import validator as v


def identify(files_manager, c, line, symbol_table):
    error = False
    caracteres = c
    while True:
        c = files_manager.read_char()
        if not c:
            break
        if c == '\n':
            error = True
            files_manager.go_back()
            break
        if c == '\"' and caracteres[-1] != '\\':
            caracteres += c
            break
        else:
            caracteres += c
            error = check_chain(c, error)
    if error:
        symbol_table.add_token('CMF', caracteres, line)
    else:
        symbol_table.add_token('CAD', caracteres, line)


def check_chain(c, error):
    if not v.is_char(c) and not c.isdigit() and not ord(c) == 32 and not ord(c) == 33 and not (35 <= ord(c) <= 126):
        return True
    else:
        return error
