import validator as v


def identify(files_manager, c, line, symbol_table):
    operator = c
    error = False
    while True:
        c = files_manager.read_char()
        if not c:
            break
        if v.is_delimiter_special(c) or v.is_char(c) or c == ' ' or c == '\n' or c.isdigit() or c == '"':
            files_manager.go_back()
            break
        else:
            operator += c
    error = check_relation(operator, error)
    if error:
        symbol_table.add_lexeme('OpMF', operator, line)
    else:
        symbol_table.add_lexeme('REL', operator, line)


def check_relation(op, error):
    if not op == '<' and not op == '<=' and not op == '!=' and not op == '>' and not op == '>=' and not op == '=' and \
            not op == '==':
        return True
    else:
        return error
