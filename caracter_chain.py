import validator as v


def identify(files_manager, c):
    print('Verificando a craseado:', ord('à'))
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
        print('Erro na identificação de cadeia de caracteres:', caracteres)
    else:
        # TODO: Adicionar cadeia de caracteres na tabela de símbolos
        print('Cadeia de caracteres lida corretamente:', caracteres)


def check_chain(c, error):
    if not v.is_char(c) and not c.isdigit() and not ord(c) == 32 and not ord(c) == 33 and not (35 <= ord(c) <= 126):
        return True
    else:
        return error
