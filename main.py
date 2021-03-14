import filesManager
import caracter_chain
import identifiers
import number
import arithmetic_operators
import relational_operators
import logic_operators
import delimitador
import symbol_table as table

# Classe principal do projeto, utilizada para verificar a lista de arquivos presente no folder input, abrir cada um
# deles, remover seus comentários, analisá-los lexicamente, obtendo seus tokens correspondentes e, em seguida, armaze-
# nar o resultado nessa análise em um arquivo correspondente no folder output


print('################## Welcome to Unicorn.io ###################')
lista_arquivos = filesManager.list_files('input')  # Obtém a lista dos arquivos presentes no diretório input
filesManager.clean_folder('output')                # Remove todos os arquivos presentes no folder output


def identify_lexemes(arquivo, symbol_table):       # Método que identifica os lexemas presentes no arquivo recebido
    line = 1
    while True:                                    # Loop utilizado para ler o arquivo, caractere por caractere
        c = filesManager.read_char()
        if not c:                                  # Caso encontremos o fim do arquivo, saímos do loop de leitura
            break
        if c == '\n':                              # Caso encontremos uma quebra de linha, incrementamos o contador line
            line = line + 1
        elif c == '\"':
            # --- Identificação de cadeia de caracteres, iniciada caso o último char lido sejam aspas
            caracter_chain.identify(filesManager, c, line, symbol_table)
        elif c.isdigit():
            # --- Identificação de número, iniciada caso o último char lido seja um dígito
            number.identify(filesManager, c, line, symbol_table)
        elif c == '+' or c == '-' or c == '*' or c == '/':
            # --- Identificação de operador aritmético, iniciada caso o último char lido seja algum dos listados acima
            arithmetic_operators.identify(filesManager, c, line, symbol_table)
        elif c == '!':                             # Caso o último char lido seja uma !
            d = filesManager.read_char()           # Lemos o char seguinte
            filesManager.go_back()                 # Damos um passo para trás com a cabeça de leitura
            if d == '=':                           # Caso esse char lido na sequência seja um =
                # Identificação de operador relacional, iniciada após a leitura de um ! seguido de um =
                relational_operators.identify(filesManager, c, line, symbol_table)
            else:
                # Identificação de operador lógico, iniciada após a leitura de um ! seguido de qualquer outra coisa
                logic_operators.identify(filesManager, c, line, symbol_table)
        elif c == '&' or c == '|':
            # Identificação de operador lógico, iniciada caso o último char lido seja algum dos listados acima
            logic_operators.identify(filesManager, c, line, symbol_table)
        elif c == '=' or c == '>' or c == '<':
            # Identificação de operador relacional, iniciada caso o último char lido seja algum dos listados acima
            relational_operators.identify(filesManager, c, line, symbol_table)
        elif c == ';' or c == ',' or c == '(' or c == ')' or c == '[' or c == ']' or c == '{' or c == '}' or c == '.':
            # Identificação de delimitador, iniciada caso o último char lido seja algum dos listados acima
            delimitador.add_table(line, c, symbol_table)
        elif not c == ' ' and not c == '\t':
            # Identificação de identificador, palavra reservada ou qualquer outro lexema que não atenda aos padrões de-
            # finidos pela linguagem que está sendo compilada
            identifiers.identify(filesManager, c, line, symbol_table)
    # Após finalizar a identificação de todos os lexemas presente no arquivo, os tokens levantados são escritos no ar-
    # quivo de saída
    filesManager.write_symbol_table(symbol_table.get_tokens(), arquivo)


def clear_comments(file, symbol_table):            # Método utilizado para remover os comentários presentes nos arquivos
    line = 1
    mensagem = ''                                  # Mensagem que será escrita no arquivo auxiliar para extrair tokens
    while True:                                    # Loop utilizado para ler o arquivo, caractere por caractere
        c = filesManager.read_char()
        if not c:                                  # Caso encontremos o fim do arquivo, saímos do loop de leitura
            break
        if c == '\n':                              # Caso encontremos uma quebra de linha, incrementamos o contador line
            line += 1
        if c == '/':                               # Caso encontremos uma /, começamos a buscar por outra ou um *
            acd = c
            c = filesManager.read_char()
            if c == '/':                           # Caso o caractere seguinte seja /, temos um comentário de linha
                while True:                        # Continuamos lendo o arquivo até encontrarmos o fim dele ou um \n
                    if c == '\n':
                        filesManager.go_back()
                        break
                    if not c:
                        break
                    c = filesManager.read_char()
            elif c == '*':                         # Caso o caractere seguinte seja *, temos um comentário de bloco
                comentario_line = line             # Salvamos a linha onde o comentário de bloco começa
                c = filesManager.read_char()
                d = filesManager.read_char()
                while c != '*' and d != '/':       # Continuamos lendo o arquivo até encontrarmos o fim dele ou um */
                    if c == '\n':
                        mensagem += '\n'
                        line += 1
                    c = d
                    d = filesManager.read_char()
                    if not d:                      # Caso encontremos o fim do arquivo antes do */, indicamos um erro
                        symbol_table.add_token('CoMF', 'Fim de arquivo inesperado', comentario_line)
                        break
            else:
                if acd == '/':
                    mensagem += acd
                mensagem += c
        else:
            mensagem += c
    # Ao finalizar a remoção dos comentários desnecessários, reescrevemos o arquivo "limpo" em um arquivo auxiliar para
    # posterior análise dos seus lexemas
    filesManager.write(mensagem, 'auxiliar_files\\' + file)


tableList = []                               # Vetor que contém a tabela de símbolos de cada um dos arquivos analisados
for i in range(len(lista_arquivos)):         # Para cada arquivo presente no folder input, removemos seus comentários
    filesManager.open_file('input\\' + lista_arquivos[i])
    tableList.append(table.SymbolTable())
    clear_comments(lista_arquivos[i], tableList[i])
    filesManager.close_file()

lista_arquivos = filesManager.list_files('auxiliar_files')

for i in range(len(lista_arquivos)):         # Para cada arquivo presente no folder auxiliar_files, obtemos seus tokens
    filesManager.open_file('auxiliar_files\\' + lista_arquivos[i])
    identify_lexemes(lista_arquivos[i], tableList[i])
    filesManager.close_file()

filesManager.clean_folder('auxiliar_files')  # Limpa o folder com arquivos auxiliares que foram criados para a análise
