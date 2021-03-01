import re


def identificar(files_manager, c):
    cadeia_caracteres = c
    while True:
        d = files_manager.ler_char()
        if not d:
            break
        else:
            cadeia_caracteres += d
        if cadeia_caracteres[-1] == '\"':
            if cadeia_caracteres[len(cadeia_caracteres) - 2] != '\\':
                break
    match = re.search(r"^\"(\w|[\s]|[\x20-\x21]|[\x23-\x7e]|(\\\"))*\"$", cadeia_caracteres)
    if not match:
        print('erro léxico')
    else:
        print(cadeia_caracteres)
