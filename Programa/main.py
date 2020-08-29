# -*- coding: utf-8 -*-
import tkinter as tk
class ProgramImc:
    def __init__(self):
        self.data = open("data","+w")
        self.opciones = ["Ingresar persona","Buscar persona","Listar IMC"]
        self.main = tk.Tk()
        self.Config()
        
        self.main.mainloop()
        self.data.close()
    def Config(self):
        self.main.title("Bienvenido a la calculadora IMC")
        self.main.geometry("600x300")
        self.main.configure(bg = '#EAE2B7')
        tk.Label(bg ="#EAE2B7", text = "Desarrollado por Javier Cabrera y Maximiliano Ibáñez").place(x = 300, y = 280)
        self.main.resizable(0,0)
        self.BotonesPrincipales()
    def BotonesPrincipales(self):
        h = 5
        w = 20
        color = "#FCBF49"
        opciones = ["Ingresar persona","Buscar persona","Listar IMC"]
        tk.Button(self.main, text = opciones[0] ,command = lambda: self.Ventana(0) ,bg = color, height = h, width = w).place(x = 20, y = 50)
        tk.Button(self.main, text = opciones[1] ,command = lambda: self.Ventana(1)  ,bg = color, height = h, width = w).place(x = 220, y = 50)
        tk.Button(self.main, text = opciones[2] ,command = lambda: self.Ventana(2)  ,bg = color, height = h, width = w    ).place(x = 420 , y = 50)
        

    def Ventana(self,index):
        self.main.iconify()
        winChild = tk.Toplevel(self.main)
        winChild.configure(bg = "#eae7d7")
        winChild.geometry("400x200")
        winChild.resizable(0,0)
        winChild.title(self.opciones[index])    
        winChild.protocol('WM_DELETE_WINDOW',lambda: (self.main.deiconify(),winChild.destroy()))

imc = ProgramImc()