from tkinter import*
from tkinter import filedialog
from tkinter import messagebox
import os

class CABinCreateur :
    def __init__(self):
        #Fenetre
        self.__screen = Tk()
        self.__screen.title("Createur Binaire")
        self.__screen.maxsize(500,500)
        self.__screen.minsize(500,500)
        self.__screen.configure(bg="white")
        #Var
        self.__emplacementLLM = str
        self.__nameFile = str
        self.__bashFile = str
        self.__varChoixFile = StringVar(self.__screen)
        self.__listChoixfile=["startChatBot.sh","startOneRequette.sh"]
        #Cretion des carder
        self.__main = Frame(self.__screen,bg="white",width=450,height=450)
        self.__helpFrame = Frame(self.__screen,bg="white",width=450,height=450)
        self.__choixFrame = Frame(self.__screen,bg="red",width=450,height=450)
        #Creation de bouton
        btnSelection = Button(self.__main,text="Selectionner l'emplacement\ndu script de lancement",bg="white",command=self.__selectedFile)
        btnCreate = Button(self.__main,text="Cree le fichier",bg="white",command=self.__choixFile)
        btnHelp = Button(self.__main,text="Aide",bg="white",command=self.__showHelp)
        btnRetourMain = Button(self.__helpFrame,text="Retour a l'acceuil",bg="white",command=self.__showMain)
        btnValiderChoix = Button(self.__choixFrame,text="Valider",bg="white",command=self.validerChoix)
        #entry
        self.__entryNameBinaire = Entry(self.__choixFrame,bd=2,font=("arial","15"))
        #Option menu
        menuChoixFile = OptionMenu(self.__choixFrame,self.__varChoixFile,*self.__listChoixfile)
        #Label
        labelhelp = Label(self.__helpFrame, justify="left",text="Mettez-vous en root aller dans\nle dossier ou ete generer le binnaire\net copier le fichier avec\nla commande 'cp' dans le \nrepertoire /bin",bg="white",fg="black",font=("arial","15"))
        #Calcule emplacement
        largeurMain = self.__main.winfo_reqwidth()
        hauteurMain = self.__main.winfo_reqheight()  
        largeurHelp = self.__helpFrame.winfo_reqwidth()
        hauteurHelp = self.__helpFrame.winfo_reqheight() 
        largeurChoix = self.__choixFrame.winfo_reqwidth()
        hauteurChoix = self.__choixFrame.winfo_reqheight()
        #Affichage
        self.__main.place(relx=0.5,rely=0.5,anchor="center")
        btnSelection.place(x=(largeurMain-btnSelection.winfo_reqwidth())//2,y=20)
        btnCreate.place(x=(largeurMain-btnCreate.winfo_reqwidth())//2,y=120)
        btnHelp.place(x=(largeurMain-btnHelp.winfo_reqwidth())//2,y=220)
        labelhelp.place(x=0,y=0)
        btnRetourMain.place(x=(largeurHelp-btnRetourMain.winfo_reqwidth()),y=(hauteurHelp-btnRetourMain.winfo_reqheight()))
        btnValiderChoix.place(x=((largeurChoix-btnValiderChoix.winfo_reqwidth())//2),y=(hauteurChoix-btnValiderChoix.winfo_reqheight()))
        self.__entryNameBinaire.place(x=((largeurChoix-self.__entryNameBinaire.winfo_reqwidth())//2),y=120)
        menuChoixFile.place(x=((largeurChoix-menuChoixFile.winfo_reqwidth())//2),y=220)
    
    def __showMain(self):
        self.__main.place(relx=0.5,rely=0.5,anchor="center")
        self.__helpFrame.place_forget()
        self.__choixFrame.place_forget()

    def __showHelp(self):
        self.__main.place_forget()
        self.__helpFrame.place(relx=0.5,rely=0.5,anchor="center")
        self.__choixFrame.place_forget()

    def show(self):
        self.__screen.mainloop()

    def __selectedFile(self):
        file = filedialog.askdirectory()
        if file :
            self.__emplacementLLM = file
            messagebox.showinfo("Emplacement","L'emplacement a bien ete enregistrer")
        else :
            messagebox.showerror("Erreur","Aucun repertoire selectionner")

    def validerChoix(self):
        self.__bashFile = self.__varChoixFile.get()
        self.__nameFile = self.__entryNameBinaire.get()
        self.__createFile()
    
    def __createFile(self):
        emplacement = filedialog.askdirectory()
        if emplacement:
            if self.__bashFile and self.__nameFile :
                # Nom du fichier à créer
                nom_fichier = os.path.join(emplacement, self.__nameFile)
                # Écrire deux lignes dans le fichier
                contenu = "#!/bin/bash\ncd "+self.__emplacementLLM+"\n./"+self.__bashFile
                # Écrire dans le fichier
                try:
                    with open(nom_fichier, "w") as fichier:
                        fichier.write(contenu)
                        self.__showHelp()
                        messagebox.showinfo("Reussite","Le fichier a bien ete cree")
                except Exception as e:
                    messagebox.showerror("Erreur","Le fichier n'a pas ete cree")
            else :
                messagebox.showerror("Erreur","Un des parametre et vide")
        else:
            messagebox.showerror("Erreur","Aucun repertoire selectionner")
            
    def __choixFile(self):
        self.__choixFrame.place(relx=0.5,rely=0.5,anchor="center")
        self.__main.place_forget()
        self.__helpFrame.place_forget()
        

    



CABinCreateur().show()