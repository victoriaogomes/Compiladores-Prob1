import validator as v


def identify(files_manager, c):
    operator = c
    error = False
    while True:
        c = files_manager.read_char()
        if not c:
            break
        if v.is_delimiter_special(c) or v.is_char(c) or c == ' ' or c == '\n':
            files_manager.go_back()
            break
        else:
            operator += c
    error = check_relation(operator, error)
    if error:
        # TODO: Colocar na tabela de erros
        print('Erro léxico no operador relacional:', operator)
    else:
        # TODO: Colocar na tabela de simbolos
        print('Operador relacional lido corretamente:', operator)


def check_relation(op, error):
    if not op == '<' and op == '<=' and op == '!=' and op == '>' and op == '>=' and op == '=' and op == '==':
        return True
    else:
        return error
