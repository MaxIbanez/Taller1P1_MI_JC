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
        if len(rut)==0:
            return estate,rut
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
            #mbox.showerror("Rut inválido","El RUT ingresado no es válido")
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
                else:
                    
                    estado = True

            else:
                
                estado = True
        return estado

    def ValidacionNombre(self,nombre):
        estados = [nombre.find(str(i)) for i in range(10)]
        for number in estados:
            if number>-1:
                #mbox.showerror("Nombre inválido","El nombre ingresado no es válido")
                return True
        return False
    def ValidacionPeso(self,peso):
        estado = False
        aux = peso
        if peso.count(",") == 1:
            peso = peso.split(",")
            peso = ".".join(peso)
            estado = False
            aux = peso
        elif (peso.count(".") == 1):
            estado = False
            aux = peso
        elif peso.count(",")>1 or peso.count(".")>1:
            estado = True
            aux = peso
        return estado,aux

    def ValidacionAltura(self,altura):
        estado = False
        aux = altura
        if altura.count(",") == 1:
            altura = altura.split(",")
            altura = ".".join(altura)
            aux = altura
        elif (altura.count(".") == 1):
            aux = altura
        elif altura.count(",")>1 or altura.count(".")>1:
            estado = True
            aux = altura
        return estado,aux

    def CalculoIMC(self,datos):
        peso = float(datos[0])
        altura = float(datos[1])/100
        imc = peso/(altura**2)
        return imc

    def InterfaceBuscar(self,ventana,dicc):
        fecha = tk.StringVar()
        peso = tk.StringVar()
        altura = tk.StringVar()
        color = "#eae7d7"
        tk.Label(ventana,bg = color,text = " ").grid(row = 5,column = 1)
        tk.Label(ventana,bg = color,text = "Fecha cuando se pesó:").grid(row = 6,column = 1)
        tk.Entry(ventana,bd = 4,textvariable = fecha).grid(row = 6,column = 2)
        tk.Label(ventana,bg = color,text = "DD/MM/AAAA").grid(row = 6,column = 3)
        #========================================================================
        tk.Label(ventana,bg = color,text = "Peso (kilos):").grid(row = 7,column = 1)
        tk.Entry(ventana,bd = 4,textvariable = peso).grid(row = 7,column = 2)
        tk.Label(ventana,bg = color,text = "ejemplos: 60 ó 60.5").grid(row = 7,column = 3)
        #========================================================================
        tk.Label(ventana,bg = color,text = "Altura (cm):").grid(row = 8,column = 1)
        tk.Entry(ventana,bd = 4,textvariable = altura).grid(row = 8,column = 2)
        tk.Label(ventana,bg = color,text = "ejemplos: 185 ó 160.5").grid(row = 8,column = 3)
        tk.Button(ventana,bg = "#f77f00",text = "Confirmar", command = lambda: self.Upload2([fecha.get(),peso.get(),altura.get()],dicc,ventana) ).grid(row = 9, column = 2)
    def BuscarUsuario(self,searchRUT, ventana):
        estado,rut = self.ValidacionRut(searchRUT)
        datos = []
        dicc = {}
        state = False
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
            for item in datos:
                if item["rut"] == rut:
                    state = True
                    dicc = item
                    break
        if state == True:
            mbox.showinfo("Usuario encontrado","Ingresarán datos de "+dicc["nombre"]+".")
            self.InterfaceBuscar(ventana,dicc)
        else:
            mbox.showerror("No encontrado","Los datos ingresados no son válidos, favor revisar formulario.")      

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
    def FemeninoIMC(self,imc):
        estado = ""
        if imc<20:
            estado = "BAJO PESO"
        elif imc>19 and imc<23.95:
            estado = "PESO NORMAL"
        elif imc>23.94 and imc <28.95:
            estado = "OBESIDAD LEVE"
        elif imc>28.94 and imc < 38:
            estado = "OBESIDAD SEVERA"
        elif imc>37:
            estado = "OBESIDAD MUY SEVERA"
        return estado
    def MasculinoIMC(self,imc):
        estado = ""
        if imc<20:
            estado = "BAJO PESO"
        elif imc>19 and imc<24.95:
            estado = "PESO NORMAL"
        elif imc>24.94 and imc <29.95:
            estado = "OBESIDAD LEVE"
        elif imc>29.94 and imc < 41:
            estado = "OBESIDAD SEVERA"
        elif imc>40:
            estado = "OBESIDAD MUY SEVERA"
        return estado


    def Upload2(self,datos,dicc,ventana):
        valid = [False, False, False]
        valid[0] = self.ValidacionFecha(datos[0])
        valid[1],peso = self.ValidacionPeso(datos[1])
        valid[2],altura = self.ValidacionAltura(datos[2])
        diagnostico = ""
        frase = ""
        if(valid.count(True) == 0):
            imc = self.CalculoIMC([peso,altura])
            if(dicc["sexo"] == "Femenino"):
                diagnostico = self.FemeninoIMC(imc)
                frase = "Estimada "+dicc["nombre"]+", su imc es de "+str(imc)[:4]+".\nSu estado físico es "+diagnostico+"."
                mbox.showinfo("Estado de su IMC",frase)
            else:
                diagnostico = self.MasculinoIMC(imc)
                frase = "Estimado "+dicc["nombre"]+", su imc es de "+str(imc)[:4]+".\nSu estado físico es "+diagnostico+"."
                opc = mbox.askyesno("Estado de su IMC",frase+"\n\n¿Desea buscar a otra persona?")
                if opc == True:
                    ventana.destroy()
                    self.Ventana(1)
                else:
                    ventana.destroy()
                    self.main.deiconify()
            data = open("data.txt","a")
            guardar = dicc["rut"]+":"+datos[0]+":"+str(imc)[:4]+":"+diagnostico
            data.write(guardar+"\n")
            guardar = ""
            data.close()
        else:
            mbox.showerror("Datos inválidos","Los datos ingresados son inválidos, intente nuevamente.")
    def LeerUsuarios(self):
        users = open("users.txt","r")
        usuarios = {}
        user = {}
        for item in users:
            item = item.strip("\n").split(",")
            for caracteristica in item:
                caracteristica = caracteristica.split(":")
                user[caracteristica[0]] = caracteristica[1]
            usuarios[user["rut"]] = user
            user = {}
        users.close()
        return usuarios

    def Upload3(self,ventana,rut):
        def mostrar1(datosUsuario,usuarios):
            listbox = tk.Listbox(ventana,width = 30,height = 20)
            for item in range(len(datosUsuario)):
                    tk.Label(ventana,bg = "#eae7d7",text = "FECHA\tIMC\tSEXO").grid(row = 4, column = 4)   
                    mostrar = datosUsuario[item]["fecha"]+(" "*7)+datosUsuario[item]["imc"]+(" "*7)+usuarios[rut]["sexo"]
                    listbox.insert(item,mostrar)
            listbox.grid(row = 5,column = 4)
        def mostrar2(datosUsuario,usuarios,listbox):
            listbox = tk.Listbox(ventana,width = 30,height = 20)
            for item in range(len(datosUsuario)):
                    tk.Label(ventana,bg = "#eae7d7",text = "FECHA\tIMC\tEDAD").grid(row = 4, column = 4)   
                    mostrar = datosUsuario[item]["fecha"]+(" "*7)+datosUsuario[item]["imc"]+(" "*7)+str(2020-int(usuarios[rut]["nacimiento"].split("/")[2]))
                    listbox.insert(item,mostrar)
            listbox.grid(row = 5,column = 4)
        state = True
        data = open("data.txt","r")
        usuarios = self.LeerUsuarios()
        dicc = []
        aux = {}
        for item in data:
                item = item.strip("\n").split(":")
                aux["rut"] = item[0]
                aux["fecha"] = item[1]
                aux["imc"] = item[2]
                aux["descripcion"] = item[3]
                dicc.append(aux)
                aux = {}
        data.close()
        state,rut = self.ValidacionRut(rut)
        datosUsuario = []
        
        tk.Label(ventana,bg = "#eae7d7",text = " "*20).grid(row = 2, column = 5)
        if(state == False):
            for item in dicc:
                if item["rut"] == rut:
                    datosUsuario.append(item)
            tk.Label(ventana,bg = "#eae7d7",text = "Usuario: "+usuarios[rut]["nombre"]).grid(row = 1, column = 4)
            tk.Button(ventana, bg = "#eae7d7" , text = "  IMC/Sexo  ", command = lambda: mostrar1(datosUsuario,usuarios)).place(x = 300,y = 40)
            tk.Button(ventana, bg = "#eae7d7" , text = "IMC/Sexo/Edad", command = lambda: mostrar2(datosUsuario,usuarios)).place(x = 300,y = 70)
            #aux = usuarios[rut]
                
        else:
            mbox.showerror("Datos inválidos","Los datos ingresados son inválidos, intente nuevamente.")


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
        color = "#eae7d7"
        searchRUT = tk.StringVar()
        tk.Label(ventana,bg = color,text ="\n\n\tIngresar Rut del\n\tusuario a buscar").grid(row = 2,column = 1)
        tk.Label(ventana,bg = color,text ="\tRUT: ").grid(row = 3,column = 1)
        tk.Entry(ventana,bd = 3,textvariable = searchRUT).grid(row = 3,column = 2)
        tk.Button(ventana,bg = "#f77f00",text = "Confirmar", command = lambda:self.Upload3(ventana,searchRUT.get()) ).grid(row = 4, column = 2)

imc = ProgramImc()