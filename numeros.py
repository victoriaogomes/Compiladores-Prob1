import re

import filesManager

def identificar(files_manager, c):
    12bruno3.45
    numero = c
    ponto = 0
    while True:
        d = files_manager.ler_char()
        if not d:
            break
        elif d == '.':
            if ponto == 0:
                numero += d
                ponto = 1
            else:
                break
        elif re.serch(r"[0-9]", d):
            palavra += d
        else:
            files_manager.voltar_cursor()
            break
    match = re.serch(r"(\d)+(.\d+)?", numero)
    if not match:
        print('Erro Léxico')
        # Add tabela como erro
    else:
        print("Numero encontrado:", numero)
        # Add tabela como número

