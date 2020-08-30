# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.messagebox as mbox
class ProgramImc:
    def __init__(self):
        self.opciones = ["Ingresar persona","Buscar persona","Listar IMC"]
        self.main = tk.Tk()
        self.Config()
        
        self.main.mainloop()
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
        winChild.geometry("500x300")
        winChild.resizable(0,0)
        winChild.title(self.opciones[index])    
        winChild.protocol('WM_DELETE_WINDOW',lambda: (self.main.deiconify(),winChild.destroy()))
        if(index == 0):
            self.Opcion1(winChild)
        if(index == 1):
            self.Opcion2(winChild)
        if(index == 2):
            self.Opcion3(winChild)
    def SimbolosEnRut(self,rut):
        rut = [ord(item) for item in rut]
        estado = True
        for item in rut:
            if ((item > 44 and item < 47) or (item>47 and item <58)): estado = True
            else:
                estado = False
                break
        return estado
    def ValidacionRut(self,rut):
        estate = True
        estados = []
        for index in range(len(rut)-1):
            if(ord(rut[index])>0 and ord(rut[index])<45):
                estados.append(True)
            elif(ord(rut[index])>45 and ord(rut[index])<48):
                estados.append(True)
            elif(ord(rut[index])>57 and ord(rut[index])<128):
                estados.append(True)
            else:
                estados.append(False)
        if (ord(rut[len(rut)-1]) == 75 or ord(rut[len(rut)-1]) == 107 or (ord(rut[len(rut)-1])>47 and ord(rut[len(rut)-1])<58 ) and (len(rut)>7 and len(rut)<13) ):
            estados.append(False)
        else:
            estados.append(True)
        #print(estados)
        if (estados.count(True)>0):
            estate = True
            mbox.showerror("Rut inválido","El RUT ingresado no es válido")
        else:
            estate = False
        if rut.count(".")>2:
            estate = True
        if rut.count("-")>1:
            estate = True
        return estate,rut
    def ValidacionFecha(self,fecha):
        estado = False
        if len(fecha)== 10 or len(fecha)== 9:
            fecha = fecha.split("/")
            if(int(fecha[0])>0 and int(fecha[0])<32):
                if(int(fecha[1])>0 and int(fecha[1])<13):
                    if(int(fecha[2])>0 and int(fecha[2])<2020):
                        estado = False
                    else:
                        estado = True
                        #mbox.showerror("Fecha inválida","La fecha ingresada no es válida")
                else:
                    estado = True
                    #mbox.showerror("Fecha inválida","La fecha ingresada no es válida")

            else:
                estado = True
                #mbox.showerror("Fecha inválida","La fecha ingresada no es válida")
        return estado

    def ValidacionNombre(self,nombre):
        estados = [nombre.find(str(i)) for i in range(10)]
        for number in estados:
            if number>-1:
                #mbox.showerror("Nombre inválido","El nombre ingresado no es válido")
                return True
        return False
    def BuscarUsuario(self,searchRUT, ventana):
        estado,_ = self.ValidacionRut(searchRUT)
        datos = []
        dicc = {}
        print(estado)
        if estado == True:
            pass
        else:
            data = open("users.txt","r")
            for item in data:
                item = item.strip("\n").split(",")
                for x in item:
                    x = x.split(":")
                    dicc[x[0]] = x[1]
                datos.append(dicc)
                dicc = {}
            data.close()
            print(datos)

    def Upload1(self, datos,ventana):
        estados = [False, False, False,False,False]
        #TRUE si hay errores
        estados[0] = self.ValidacionNombre(datos[0]) 
        estados[1],rut = self.ValidacionRut(datos[1])
        estados[3] = self.ValidacionFecha(datos[3])
        if datos[2] == "":
            estados[2] = True
        if datos[4] == "":
            estados[4] = True
        if estados.count(True) == 0:
            nombre = "Nombre: "+datos[0]+"\n"
            rut = "RUT: "+rut+"\n"
            sexo = "Sexo: "+datos[2]+"\n"
            fecha = "Fecha de Nacimiento: "+datos[3]+"\n"
            estadoDeportivo = "Estado deportivo: "+datos[4]+"\n"
            pregunta = "\n\n\t¿Los datos ingresados son correctos?\t\t\t\tsi acepta, los datos serán guardados,\t\nen caso contrario, deberá editar los datos nuevamente."
            frase = nombre+rut+sexo+fecha+estadoDeportivo+pregunta
            opc = mbox.askquestion("Confirmación de datos", frase,icon='warning')
            if opc == "yes":
                mbox.showinfo("Confirmación","Los datos ingresados fueron guardados correctamente!")
                data = open("users.txt","a")
                aux = ["nombre:"+datos[0],"rut:"+datos[1],"sexo:"+datos[2],"nacimiento:"+datos[3],"estadoDeportivo:"+datos[4]]
                aux = ",".join(aux)            
                data.write(aux+"\n")
                ventana.destroy()
                self.main.deiconify()
                
        else:
            mbox.showerror("Datos erroneos","Los datos ingresados son erroneos o faltantes, favor revisar y editar los datos")

    def Opcion1(self, ventana):
        c = 1
        color = "#eae7d7"
        data = ["Nombre","RUT","Sexo","Fecha de\n nacimiento","Estado deportivo"]
        examples = ["(Nombre y apellido)","Ingrese su rut sin puntos ni guion"," "," DD/MM/AAAA"," "]
        entryDatos = [tk.StringVar() for i in range(len(data))]
        entryDatos = entryDatos[:]
        for i in range(len(data)):
            if(i!=2 and i!=4):
                tk.Label(ventana,bg = color,text ='%s\n'%(data[i])).grid(row = (i+1),column = c)
                tk.Entry(ventana,bd = 3,textvariable = entryDatos[i]).grid(row = (i+1),column = c+1)
                tk.Label(ventana,bg = color,text ='%s\n'%(examples[i])).grid(row = (i+1),column = c+2)
                tk.Label(ventana,bg = color,text = "").grid(row = (i+2),column = c+2)
            else:
                tk.Label(ventana,bg = color,text ='%s\n'%(data[i])).grid(row = (i+1),column = c)
                tk.Radiobutton(ventana, bg = color , text = "Femenino",variable = entryDatos[2], value = "Femenino").place(x = 90, y = 75)
                tk.Radiobutton(ventana, bg = color , text = "Masculino",variable = entryDatos[2], value = "Masculino").place(x = 180, y = 75)
            if(i==4):
                tk.Label(ventana,bg = color,text ='%s\n'%(data[i])).grid(row = (i+1),column = c)
                tk.Radiobutton(ventana, bg = color , text = "Atleta",variable = entryDatos[4], value = "Atleta").place(x = 110, y = 155)
                tk.Radiobutton(ventana, bg = color , text = "Persona normal",variable = entryDatos[4], value = "P Normal").place(x = 200, y = 155)

        tk.Label(ventana,bg = color,text = "").grid(row = (len(data))+1,column = 2)
        tk.Button(ventana,bg = "#f77f00",text = "Confirmar", command = lambda: self.Upload1([item.get() for item in entryDatos],ventana)).grid(row = len(data)+2, column = 2)
    def Opcion2(self, ventana):
        color = "#eae7d7"
        searchRUT = tk.StringVar()
        tk.Label(ventana,bg = color,text ="\n\n\tIngresar Rut del\n\tusuario a buscar").grid(row = 2,column = 1)
        tk.Label(ventana,bg = color,text ="\tRUT: ").grid(row = 3,column = 1)
        tk.Entry(ventana,bd = 3,textvariable = searchRUT).grid(row = 3,column = 2)
        tk.Button(ventana,bg = "#f77f00",text = "Confirmar", command = lambda:self.BuscarUsuario(searchRUT.get(), ventana)).grid(row = 4, column = 2)
    def Opcion3(self,ventana):
        print("NO RECUERDO QUE IBA ACÁ (opción 3)")

imc = ProgramImc()