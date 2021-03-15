import validator as v
# Classe para idenficação e manipulação de operadores logicos.


def identify(files_manager, c, line, symbol_table):
    operator = c                                             # Recebe o operador da main.
    error = False                                            # Cria a flag de erro.
    while True:
        c = files_manager.read_char()                        # Lê o próximo caractere.
        if not c:                                            # Verifica se já está no fim do arquivo.
            break                                            # Se sim, quebra o loop
        if v.is_delimiter_special(c) or v.is_char(c) or c == ' ' or c == '\n' or c.isdigit():
            files_manager.go_back()                          # Se c não estiver dentro dos critérios de parada, cursor
            break                                            # volta uma posição no arquivo e quebra o loop.
        else:                                                # Caso contrário.
            operator += c                                    # Concatena o char no operador.
    error = check_logic(operator, error)                     # Verifica se há um erro no operador.
    if error:                                                # Se houver.
        symbol_table.add_token('OpMF', operator, line)       # Add na tabela como operador mal formado.
    else:                                                    # Caso contrário.
        symbol_table.add_token('LOG', operator, line)        # Add na tabela como operador lógico.


def check_logic(op, error):                                  # Verifica se o operador lógico foi construído certo.
    if not op == '&&' and not op == '||' and not op == '!':  # Se não estiver dentro do conjunto aceito.
        return True                                          # Flag de erro recebe true.
    else:
        return error                                         # Caso contrário, mantem o valor da flag.
