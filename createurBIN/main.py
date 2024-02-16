from tkinter import*

class CABinCreateur :
    def __init__(self):
        self.__screen = Tk()
        self.__screen.title("Createur Binaire")
        self.__screen.maxsize(500,500)
        self.__screen.minsize(500,500)
        self.__screen.configure(bg="white")
        

    def show(self):
        self.__screen.mainloop()


CABinCreateur().show()