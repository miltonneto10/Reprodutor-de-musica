#importações
from tkinter import*

from PIL import Image, ImageTk

import pygame
from pygame import mixer

import os

#cores
cor0 = "#f0f3f5" #cinza
cor1 = "#feffff" #branco
cor2 = "#3fb5a3" #verde
cor3 = "#2e2d2c" #preto
cor4 = "#403d3d" #preto
cor5 = "#4a88e8" #azul

#criando janela
janela = Tk ()
janela.title ("")
janela.geometry('352x255')
janela.configure(background=cor1)
janela.resizable(width=FALSE, height=FALSE)

#frames
frame_esquerda = Frame(janela, width=150, height=150, bg=cor3)
frame_esquerda.grid(row=0, column=0, pady=1, padx=1, sticky=NSEW)

frame_direita = Frame(janela, width=250, height=150, bg=cor3)
frame_direita.grid(row=0, column=1, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=404, height=100, bg=cor3)
frame_baixo.grid(row=1, column=0, columnspan=3, pady=1, padx=0, sticky=NSEW)

#configurando o frame esquerda
img_1 = Image.open('musica.png')
img_1 = img_1.resize((130,130))
img_1 = ImageTk.PhotoImage(img_1)

l_logo = Label(frame_esquerda, height=130, image=img_1, compound=LEFT, padx=0, anchor='nw', font=('ivy 16 bold'), bg=cor3, fg=cor3)
l_logo.place(x=14, y=15)


#criando funções

#função de iniciar música
def play_musica():
    rodando = listbox.get(ACTIVE)
    l_rodando['text'] = rodando
    mixer.music.load(rodando)
    mixer.music.play()

#função de pausar música
def pausar_musica():
    mixer.music.pause()

#funão de continuar música
def continuar_musica():
    mixer.music.unpause()

#função de parar música
def parar_musica():
    mixer.music.stop()

#função próxima música
def proxima_musica():
    tocando = l_rodando['text']
    index = musicas.index(tocando)
    novo_index = index + 1
    tocando = musicas[novo_index]
    mixer.music.load(tocando)
    mixer.music.play()

    #deletando os elementos na playlist
    listbox.delete(0,END)

    mostrar()

    listbox.select_set(novo_index)
    listbox.config(selectmode=SINGLE)
    l_rodando['text'] = tocando

#função música anterior
def anterior_musica():
    tocando = l_rodando['text']
    index = musicas.index(tocando)
    novo_index = index - 1
    tocando = musicas[novo_index]
    mixer.music.load(tocando)
    mixer.music.play()

    #deletando os elementos na playlist
    listbox.delete(0,END)

    mostrar()

    listbox.select_set(novo_index)
    listbox.config(selectmode=SINGLE)
    l_rodando['text'] = tocando

#configurando o frame direita

lista =['joão', 'futi', 'muanda','joão', 'futi', 'muanda','joão', 'futi', 'muanda','joão', 'futi', 'muanda','joão', 'futi', 'muanda']


listbox = Listbox(frame_direita, width=22, height=10, selectmode=SINGLE, font=('arial 9 bold'), bg=cor3, fg=cor1)
listbox.grid(row=0, column=0)

s = Scrollbar(frame_direita)
s.grid(row=0, column=1, sticky=NSEW)

listbox.config(yscrollcommand=s.set)
s.config(command=listbox.yview)


#confiurando frame baixo

l_rodando = Label(frame_baixo, text='Escolha uma Música da Lista', width=44, justify=LEFT, anchor='nw', font=('ivy 10 bold'), bg=cor1, fg=cor4)
l_rodando.place(x=0, y=1)


img_2 = Image.open('2.png')
img_2 = img_2.resize((30,30))
img_2 = ImageTk.PhotoImage(img_2)
b_anterior = Button(frame_baixo,command=anterior_musica, width=40, height=40, image=img_2, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=cor3, fg=cor1)
b_anterior.place(x=38, y=35)

img_3 = Image.open('3.png')
img_3 = img_3.resize((30,30))
img_3 = ImageTk.PhotoImage(img_3)
b_play = Button(frame_baixo,command=play_musica, width=40, height=40, image=img_3, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=cor3, fg=cor1)
b_play.place(x=84, y=35)

img_4 = Image.open('4.png')
img_4 = img_4.resize((30,30))
img_4 = ImageTk.PhotoImage(img_4)
b_proxima = Button(frame_baixo,command=proxima_musica, width=40, height=40, image=img_4, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=cor3, fg=cor1)
b_proxima.place(x=130, y=35)

img_5 = Image.open('5.png')
img_5 = img_5.resize((30,30))
img_5 = ImageTk.PhotoImage(img_5)
b_pausar = Button(frame_baixo, command=pausar_musica, width=40, height=40, image=img_5, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=cor3, fg=cor1)
b_pausar.place(x=176, y=35)

img_6 = Image.open('6.png')
img_6 = img_6.resize((30,30))
img_6 = ImageTk.PhotoImage(img_6)
b_continuar = Button(frame_baixo, command=continuar_musica, width=40, height=40, image=img_6, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=cor3, fg=cor1)
b_continuar.place(x=222, y=35)

img_7 = Image.open('7.png')
img_7 = img_7.resize((30,30))
img_7 = ImageTk.PhotoImage(img_7)
b_stop = Button(frame_baixo, width=40, command=parar_musica, height=40, image=img_7, font=('ivy 10 bold'), relief=RAISED, overrelief=RIDGE, bg=cor3, fg=cor1)
b_stop.place(x=268, y=35)


os.chdir(r'C:\Users\User\Music\Músicas')
musicas = os.listdir()


def mostrar():
    for i in musicas:
        listbox.insert(END,i)

mostrar()

mixer.init() #inicializando o mixer

janela.mainloop ()