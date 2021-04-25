import validator as v

# Classe utilizada para as verificações e manipulações necessárias do analisador léxico no que tange o uso de operadores
# relacionais.


def identify(files_manager, c, line, symbol_table):
    # Método utilizado para verificar efetivamente se o char que foi recebido por parâmetro realmente constitui um
    # operador relacional.
    operator = c
    error = False  # Flag de erro usada para verificar se a construção do operador relacional está correta.
    while True:    # Loop utilizado para fazer a leitura do operador, respeitando seus delimitadores.
        c = files_manager.read_char()
        if not c:  # Caso estejamos no fim do arquivo, devemos encerrar a leitura.
            break
        if v.is_delimiter_special(c) or v.is_char(c) or c == ' ' or c == '\n' or c.isdigit() or c == '"':
            # Caso encontremos um delimitador, uma letra, um espaço em branco, uma quebra de linha, um dígito
            # ou aspas, devemos finalizar a leitura do lexema, dar um passo para trás e classificar o que foi
            # lido.
            files_manager.go_back()
            break
        else:      # Caso nenhum delimitador de leitura tenha sido encontrado, adicionamos o char lido ao operador
            operator += c
    error = check_relation(operator, error)  # Verifica se o operador relacional lido está formado corretamente
    if error:      # Adiciona na tabela de símbolos um token indicando a presença de um operador mal formado
        symbol_table.add_token('OpMF', operator, line)
    else:          # Adiciona na tabela de símbolos um token indicando a presença de um operador relacional
        symbol_table.add_token('REL', operator, line)
    return error


def check_relation(op, error):
    # Método utilizado para checar se a string lida se encaixa em algum dos operadores relacionais listados abaixo e
    # retornar a conclusão dessa verificação
    if not op == '<' and not op == '<=' and not op == '!=' and not op == '>' and not op == '>=' and not op == '=' and \
            not op == '==':
        return True
    else:
        return error
