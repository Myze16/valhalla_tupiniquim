import random
from tkinter import *
import tkinter
import os
from PIL import Image, ImageTk

pastaApp=os.path.dirname(__file__)

def abrir_pontos():
    pontos = Toplevel()
    pontos.title('Distribuição de pontos')
    pontos.geometry("340x480")
    pontos.resizable(False,False)

def abrir_mago():
    mago = Toplevel()
    mago.title('Mago')
    mago.geometry("640x180")
    mago.resizable(False,False)

    Container = Frame(mago)
    Container["pady"] = 20
    Container.pack()

    imagem = PhotoImage(file="images/mago.png")
    imagem = Image.open("images/mago.png")
    test = ImageTk.PhotoImage(imagem)

    mago = tkinter.Label(mago, image=test)
    mago.image = test
    mago.place(x=10, y=10)
    

    pontos = Button(Container)
    pontos["text"] = "Distribua seus pontos!"
    pontos["font"] = ("Calibri", "14")
    pontos["width"] = 20
    pontos["height"] = 2
    pontos["command"] = abrir_pontos
    pontos.pack()


def abrir_barbaro():
    barbaro = Toplevel()
    barbaro.title('Bárbaro')
    barbaro.geometry("640x180")
    barbaro.resizable(False,False)

    Container = Frame(barbaro)
    Container["pady"] = 20
    Container.pack()

    imagem = PhotoImage(file="images/barbaro.png")
    imagem = Image.open("images/barbaro.png")
    test = ImageTk.PhotoImage(imagem)

    barbaro = tkinter.Label(barbaro, image=test)
    barbaro.image = test
    barbaro.place(x=10, y=10)
    

    pontos = Button(Container)
    pontos["text"] = "Distribua seus pontos!"
    pontos["font"] = ("Calibri", "14")
    pontos["width"] = 20
    pontos["height"] = 2
    pontos["command"] = abrir_pontos
    pontos.pack()

class Application:
    def __init__(self, master=None):
        self.fontePadrao = ("Arial", "10")
        self.primeiroContainer = Frame(master)
        self.primeiroContainer["pady"] = 10
        self.primeiroContainer.pack()

        self.quartoContainer = Frame(master)
        self.quartoContainer["pady"] = 20
        self.quartoContainer.pack()

        self.titulo = Label(self.primeiroContainer, text="Escolha sua classe!")
        self.titulo["font"] = ("Arial", "18", "bold")
        self.titulo.pack()

        self.barbaro = Button(self.quartoContainer)
        self.barbaro["text"] = "Bárbaro"
        self.barbaro["font"] = ("Calibri", "14")
        self.barbaro["width"] = 16
        self.barbaro["height"] = 2
        self.barbaro["command"] = abrir_barbaro
        self.barbaro.pack()

        self.mago = Button(self.quartoContainer)
        self.mago["text"] = "Mago"
        self.mago["font"] = ("Calibri", "14")
        self.mago["width"] = 16
        self.mago["height"] = 2
        self.mago["command"] = abrir_mago
        self.mago.pack()

        self.ladrao = Button(self.quartoContainer)
        self.ladrao["text"] = "Ladino"
        self.ladrao["font"] = ("Calibri", "14")
        self.ladrao["width"] = 16
        self.ladrao["height"] = 2
        self.ladrao.pack()

        self.elfo = Button(self.quartoContainer)
        self.elfo["text"] = "Elfo"
        self.elfo["font"] = ("Calibri", "14")
        self.elfo["width"] = 16
        self.elfo["height"] = 2
        self.elfo.pack()

        self.clerigo = Button(self.quartoContainer)
        self.clerigo["text"] = "Clérigo"
        self.clerigo["font"] = ("Calibri", "14")
        self.clerigo["width"] = 16
        self.clerigo["height"] = 2
        self.clerigo.pack()


#Classe Heroi com os atributos pedidos
#A classe pode ser: Bárbaro, Mago, Ladrão, Elfo ou Clérigo
#O atributo VIDA começará sempre em 100
class Heroi:
    def __init__(self, nome, classe, forca, destreza, constituicao, inteligencia, carisma):
        self.nome = nome
        self.classe = classe
        self.forca = forca
        self.destreza = destreza
        self.constituicao = constituicao
        self.inteligencia = inteligencia
        self.carisma = carisma
        self.vida = 100

#Método ATACA
#Recebe o nome do inimigo(alvo.nome)
#Ataque = random entre 1 e 6
#Regras de ataque:
#Menor ou igual à 2 = DANO 0
#Maior que 2 e menor ou igual à 5 = DANO 2
#Igual à 6 = DANO 4

    def ataca(self, alvo, ataque, dano):
        ataque.randint(1,6)
        if ataque <= 2:
            dano.alvo = 0
        elif ataque > 2 <= 5:
            dano.alvo = 2
        else:
            dano.alvo = 4
        alvo.dano(dano)
        mensagem = f"{self.nome} atacou {alvo.nome} causando {dano: .2f} de dano!"
        self.mensagem(mensagem)

    def dano(alvo, dano):
        # alvo vai ser um objeto
        if (alvo.vida - dano) < 0:
            alvo.vida = 0
            print(f'Inimigo {alvo.nome} abatido')
        else:
            alvo.vida = alvo.vida - dano
    
    def dano(alvo, dano,):
        dano = alvo.vida - dano
    
    def reconstituir(self, alvo, reconstitui, cura):
        reconstitui.randint(1,6)
        if reconstitui <= 2:
            cura.alvo = 0
        elif reconstitui > 2 <= 5:
            cura.alvo = 2
        else:
            cura.alvo = 4
        cura.alvo(cura)
        mensagem = f"O alvo {alvo.nome} reconstituiu sua vida em {cura.alvo} pontos!"
        self.mensagem(mensagem)

    def dano(alvo, dano, vida):
        dano = alvo.vida - dano
    
    def cura(self, alvo, cura):
        cura = alvo.vida + cura

root = Tk()
Application(root)
root.mainloop()
root.geometry("640x480")
root.resizable(False,False)
root.title("Classes")