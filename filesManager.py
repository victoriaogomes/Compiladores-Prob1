from os import listdir
from os.path import isfile, join
import re
import os

previousPos = 0


def read_char():
    global previousPos
    previousPos = file.tell()
    return file.read(1)


def open_file(path):
    global file
    file = open(path, 'r+')


def close_file():
    file.close()
    print('Arquivo fechado!')


def write(mensagem, path):
    with open(path, 'w+') as archive:
        archive.write(mensagem)


def return_lines(path):  # Retorna um vetor com as linhas da arquivo
    with open(path, 'r+') as archive:
        return archive.readlines()


def list_files(path):  # Caminho do diretório que será analisado
    files = [f for f in listdir(path) if isfile(join(path, f))]  # Não faço idéia do que ele está fazendo aqui
    print(files)  # Printa os arquivos no diretório que foi passado
    print('O diretório possui:', len(files), 'arquivos')  # len() retorn o tamanho do array
    print('#############################')
    return files


def go_back():
    file.seek(previousPos)


def write_symbol_table(message, filename):
    temp = re.compile("([a-zA-Z]+)([0-9]+)")
    res = temp.match(filename).groups()
    outfile = 'output\\saida' + res[1] + '.txt'
    write(message, outfile)


def clean_folder(folder):
    folderFiles = list_files(folder)
    for arq in folderFiles:
        os.remove(folder + '\\' + arq)
