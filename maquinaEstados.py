import re
import filesManager

filesManager.abrir_arquivo('input\\teste.txt')

while True:
    c = filesManager.ler_char()
    if not c:
        break
    if c == '\"':
        while True:
            c += filesManager.ler_char()
            if c[-1] == '\"':
                if c[len(c) - 2] != '\\':
                    break
        match = re.search(r"^\"([a-z]|[A-Z]|[0-9]|[\s]|[\x20-\x21]|[\x23-\x7e]|(\\\"))*\"$", c)
        if not match:
            print('erro léxico')
        else:
            print(c)

filesManager.fechar_arquivo()
