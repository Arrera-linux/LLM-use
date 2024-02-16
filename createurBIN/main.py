from tkinter import*

class CABinCreateur :
    def __init__(self):
        self.__screen = Tk()
        self.__screen.title("Createur Binaire")
        self.__screen.maxsize(500,500)
        self.__screen.minsize(500,500)
        self.__screen.configure(bg="white")
        #Cretion des carder
        self.__main = Frame(self.__screen,bg="white",width=450,height=450)
        self.__helpFrame = Frame(self.__screen,bg="white",width=450,height=450)
        #Creation de bouton
        btnSelection = Button(self.__main,text="Selectionner l'emplacement\ndu script de lancement",bg="white")
        btnCreate = Button(self.__main,text="Cree le fichier",bg="white")
        btnHelp = Button(self.__main,text="Aide",bg="white",command=self.__showHelp)
        btnRetourMain = Button(self.__helpFrame,text="Retour a l'acceuil",bg="white",command=self.__showMain)
        #Label
        labelhelp = Label(self.__helpFrame, justify="left",text="Mettez-vous en root aller dans\nle dossier ou ete generer le binnaire\net coiper le fichier avec\nla commande 'cp' dans le \nrepertoire /bin",bg="white",fg="black",font=("arial","15"))
        #Calcule emplacement
        largeurMain = self.__main.winfo_reqwidth()
        hauteurMain = self.__main.winfo_reqheight()  
        largeurHelp = self.__helpFrame.winfo_reqwidth()
        hauteurHelp = self.__helpFrame.winfo_reqheight() 
        #Affichage
        self.__main.place(relx=0.5,rely=0.5,anchor="center")
        btnSelection.place(x=(largeurMain-btnSelection.winfo_reqwidth())//2,y=20)
        btnCreate.place(x=(largeurMain-btnCreate.winfo_reqwidth())//2,y=120)
        btnHelp.place(x=(largeurMain-btnHelp.winfo_reqwidth())//2,y=220)
        labelhelp.place(x=0,y=0)
        btnRetourMain.place(x=(largeurHelp-btnRetourMain.winfo_reqwidth()),y=(hauteurHelp-btnRetourMain.winfo_reqheight()))
    
    def __showMain(self):
        self.__main.place(relx=0.5,rely=0.5,anchor="center")
        self.__helpFrame.place_forget()

    def __showHelp(self):
        self.__main.place_forget()
        self.__helpFrame.place(relx=0.5,rely=0.5,anchor="center")

    def show(self):
        self.__screen.mainloop()


CABinCreateur().show()