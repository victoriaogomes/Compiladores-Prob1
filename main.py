from tkinter import *

# Criando a janela principal do programa
window = Tk()

# Criando uma função para lidar com cliques no botão
def myClick():
    label = Label(window, text = "Hello " + entry.get())
    label.pack()

######### Criando widgets do tipo entry (são inputs, para o usuário digitar)
#   width muda a largura do campo de input
#   bg muda a cor de fundo do campo de input
#   fg muda a cor do texto que será digitado no input
#   borderwidth muda a largura da borda do botão
#   método .get() em uma entry obtém o texto digitado
#   método .insert() utilizado para colocar um texto padrão dentro do input
entry = Entry (window, width = 50)
entry.pack()
entry.insert(0, "Enter your name")

######### Criando um widget do tipo label
# label = Label(window, text = "Hello World!")
# label2 = Label(window, text = "My name is Victoria Gomes")

######### Criando um widget do tipo button
#   state no button para indicar o estado dele no momento (ex: desabilitado)
#   padx no botão aumenta sua largura
#   pady no botão aumenta seu comprimento
#   command indica o nome da função que será chamada quando o botão for clicado (não colocar parênteses, apenas o nome da função)
#   fg muda a cor do texto do botão (foreground) - usar nome da cor ou hexadecimal
#   bg muda a cor do fundo do botão (background) - usar nome da cor ou hexadecimal
button1 = Button(window, text = "Enter your name", command = myClick, fg = "blue", bg = "white")

######### Adicionando o label criado na nossa janela
#label.pack()
#label.grid(row = 0, column = 0)
#label2.grid(row = 1, column = 5)
button1.pack()

# Loop principal da janela
window.mainloop()
