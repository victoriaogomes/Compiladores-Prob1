import validator as v
# Classe identifica e manipula estruturas do time cadeia de caracteres.


def identify(files_manager, c, line, symbol_table):      # Recebe gerenciador de arquivos, caractere, a linha e a tabela
    error = False                                        # Flag de erro na cadeia de caracteres.
    caracteres = c                                       # Variável que vai receber toda a cadeia de caracteres.
    while True:
        c = files_manager.read_char()                    # Lê o próximo caractere.
        if not c:                                        # Verifica se está no final do arquivo.
            break                                        # Quebra o loop while.
        if c == '\n':                                    # Verifica se leu uma quebra de linha.
            error = True                                 # Levanta erro por não ter fechado a cadeia.
            files_manager.go_back()                      # Volta em um espaço o cursor.
            break                                        # Quebra o loop while.
        if c == '\"' and caracteres[-1] != '\\':         # Verifica se foi uma " sem / anterior.
            caracteres += c                              # Se sim ele adiciona as aspas na cadeia...
            break                                        # ...E encerra o loop.
        else:                                            # Caso seja um caractere qualquer.
            caracteres += c                              # Concatena na cadeia.
            error = check_chain(c, error)                # Verifica se c pode ser aceito nas cadeias da linguagem.
    if error:                                            # Se a flag de erro for verdadeira.
        symbol_table.add_token('CMF', caracteres, line)  # Add na tabe como caractere mal formado.
    else:                                                # Caso a flag não tenha alertado erro.
        symbol_table.add_token('CAD', caracteres, line)  # Add na tabela como cadeia de caracteres.


def check_chain(c, error):                               # Verifica se o caractere é aceito na cadeia da linguagem.
    if not v.is_char(c) and not c.isdigit() and not ord(c) == 32 and not ord(c) == 33 and not (35 <= ord(c) <= 126):
        return True                                      # Levanta flag de erro caso não seja um caractere nesse grupo.
    else:
        return error                                     # Caso contrário não mexe no valor da variável.
