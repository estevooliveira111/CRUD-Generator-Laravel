from DataBase import DataBase
from Shell import Shell
from tkinter import *
import re

class Application:
    
    def __init__(self, master=None):
        self.fontBase = ("Montserrat", "12")

        self.FirstContainer = Frame(master)
        self.FirstContainer["pady"] = 10
        self.FirstContainer.pack()

        self.SecondContainer = Frame(master)
        self.SecondContainer["pady"] = 30
        self.SecondContainer.pack()

        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()
    
        self.titulo = Label(self.FirstContainer, text="Painel Laravel")
        self.titulo["font"] = ("Montserrat", "30", "bold")
        self.titulo.pack()

        self.labelTitle= Label(self.FirstContainer, text="Qual nome do seu projeto?", font=self.fontBase, pady=20)
        self.labelTitle.pack(side=LEFT)

        self.inputTitle = Entry(self.FirstContainer, width=25)
        self.inputTitle.pack(side=RIGHT)

        self.i=IntVar()
        self.check = Checkbutton(self.SecondContainer, text='Iniciar Com GITHUB', variable=self.i)
        self.check.pack()

        self.gerar = Button(self.SecondContainer, font=self.fontBase)
        self.gerar["text"] = "Gerar Aplicação"
        self.gerar["width"] = 12
        self.gerar["command"] = self.CreateProject
        self.gerar.pack()


        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()
        self.labelTitle= Label(self.FirstContainer, text="Qual nome do seu projeto?", font=self.fontBase, pady=20)

    def CreateProject(self):

        database = DataBase()
        database.CreatDatabase(self.inputTitle.get().lower())
        self.lblmsg["text"] = "Banco de Dados Criado"

        title = re.sub(r"[^a-zA-Z0-9]","", self.inputTitle.get())
        shell = Shell()
        shell.StartLaravel(title, False)
        self.lblmsg["text"] = "Projeto Criado"

root = Tk()
Application(root)
root.geometry("700x350")
root.title('Painel Laravel')

root.mainloop()
