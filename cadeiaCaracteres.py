import re


def identificar(files_manager):
    while True:
        c = files_manager.ler_char()
        if not c:
            break
        if c == '\"':
            while True:
                c += files_manager.ler_char()
                if c[-1] == '\"':
                    if c[len(c) - 2] != '\\':
                        break
            match = re.search(r"^\"(\w|[\s]|[\x20-\x21]|[\x23-\x7e]|(\\\"))*\"$", c)
            if not match:
                print('erro léxico')
            else:
                print(c)
