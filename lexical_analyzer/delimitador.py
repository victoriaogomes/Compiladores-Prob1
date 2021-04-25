# Por delimitador serem caractres isolados que não formam cadeias, essa classe não precisa fazer a identificação
# Caso receba um caractere que seja delimitador, a main chama esse método somente para adicionar o lexema na tabela.


def add_table(line, lexeme, symbol_table):       # Recebe a linha atual, o delimitador e instância da tabela de simnolos
    symbol_table.add_token('DEL', lexeme, line)  # Add na tabela como delimitador e com lexema e linha passado.

