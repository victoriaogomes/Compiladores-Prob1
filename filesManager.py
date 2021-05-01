from os import listdir, mkdir
from os.path import isfile, join
import re
import os

previousPos = 0


# filesManager tem o conjunto de métodos para fazer diversas manipulações nos arquivos de entrada e saída.


def read_char():  # Lê um caractere por vez.
    global previousPos  # Torna a posição anterior uma variável.
    previousPos = file.tell()  # Pega posição atual.
    return file.read(1)  # Retorna um caractere lido.


def open_file(path):  # Abre o arquivo dado no caminho.
    global file  # Torna o arquivo File global.
    file = open(path, 'r+')  # Abre o arquivo no caminho passado.


def close_file():  # Fecha o arquivo depois do uso.
    file.close()


def write(mensagem, path):  # Escreve em arquivos passados.
    with open(path, 'w+') as archive:  # Abre arquivo para escrita.
        archive.write(mensagem)  # Escreve a mensagem.


def return_lines(path):  # Retorna um vetor com as linhas da arquivo.
    with open(path, 'r+') as archive:  # Abre o arquivo para leitura.
        return archive.readlines()  # Retorna todas as linhas de um arquivo em uma lista.


def list_files(path):  # Lista todos os arquivos de um diretório.
    files = [f for f in listdir(path) if isfile(join(path, f))]  # Retorna uma lista dos arquivos naquele caminho.
    return files  # Retorna a linha.


def go_back():  # Retorna o cursor do arquivo em uma posição.
    file.seek(previousPos)


def write_symbol_table(message, filename):  # Usado para escrever a tabela no arquivo de saída.
    temp = re.compile("([a-zA-Z]+)([0-9]+)")  # Separa o nome do arquivo de entrada do número para
    res = temp.match(filename).groups()  # que o arquivo de saída tenha numero correspondente.
    outfile = 'output\\saida' + res[1] + '.txt'  # Concatena caminho com o número e extensão do arquivo.
    write(message, outfile)  # Escreve no arquivo de saída.


def clean_folder(folder):  # Apaga um diretório para tirar arquivos restantes de execuções anteriores.
    folderFiles = list_files(folder)  # Pega a lista de arquivos do diretório passado.
    for arq in folderFiles:  # For para remover arquivos um a um.
        os.remove(folder + '\\' + arq)


def init_program():
    if not os.path.isdir('auxiliar_files'):
        os.mkdir('auxiliar_files')
