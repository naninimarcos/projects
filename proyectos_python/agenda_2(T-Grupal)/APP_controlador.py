""" 
----------- FUNCIONALIDAD --------------------------
La aplicacion fue creada dentro de Spider y los codigos funcionan correctamente en ese entorno, 
al pasar a otro entorno como es visual es que puede generar problemas la linea 31 
de esta misma parte la cual esta separada del resto de importaciones de modulos
----------- OBSERVADOR   --------------------------
El mismo deposita los datos en un archivo .log donde se guarda las acciones
----------- INFORMACION --------------------------
    Grupo 1, integrantes: 
    Corbatto, Mauricio
    Mielniczuk Lapp, Julio
    Nanini, Marcos
-------------- MODULOS ------------------------
controlador --> es en donde nos encontramos y es desde donde se lanza la app
base_datos --> es donde se encuentra la base de datos
Eliminar y eliminarmodal --> se encarga de las funciones de eliminar y su interfaz grafica
guardar y guardarModal --> se encarga de las funciones de guardar y su interfaz grafica
modificar y modificarModal --> se encarga de las funciones de modificar y su interfaz grafica
ParametrosTema--> se encarga de las funciones de los botones para cambiar los colores de la interfaz grafica
val--> funciones regex 
---------------------------------------------------"""

import logging
from modificarModal import *
from eliminarModal import *
from guardarModal import *
from tkinter import ttk
from base_datos import *
from tkinter.messagebox import *
from tkinter import *

"""------ importaciones de modulos --------------
en visual studio tiene que estar deshabilitado la siguiente linea
 pero en spider debe estar habilitada """
#from temas.OpcionTemas import EleccionTema

"------------- clases -------------------------"


class Tema:

    observadores = []

    def Agregar(self, obj):
        self.observadores.append(obj)

    def Quitar(self, obj):
        pass

    def Notificar(self):
        for observador in self.observadores:
            observador.Update()


class Observador:
    def Update(self):
        raise NotImplementedError("Delegación de actualización")


class Producto(Tema):

    def __init__(self, window):

        self.estado = None
        # Ventana principal
        self.root = window
        self.root.title("Tarea POO")

        self.titulo = Label(self.root, text="Ingrese sus datos", bg="#376E05",
                            fg="#fff", height=1, width=60, font=('courier', 20, 'bold'))
        self.titulo.grid(row=0, column=0, columnspan=4,
                         padx=1, pady=1, sticky=W+E)

        self.tree = ttk.Treeview(height=10, columns=3)
        self.tree["columns"] = ("uno", "dos", "tres", "cuatro")
        self.tree.grid(row=7, column=0, columnspan=3)
        self.tree.heading("#0", text="ID", anchor=CENTER)
        self.tree.heading("uno", text='Título', anchor=CENTER)
        self.tree.heading("dos", text='Fecha', anchor=CENTER)
        self.tree.heading("tres", text='Descripción', anchor=CENTER)
        self.tree.heading("cuatro", text='Estado', anchor=CENTER)

        Button(self.root, text='Guardar',
               command=lambda: self.pasarObjetoGuardar()).grid(row=11, column=0)
        Button(self.root, text='Eliminar',
               command=lambda: self.pasarObjetoEliminar()).grid(row=11, column=1)
        Button(self.root, text='Modificar',
               command=lambda: self.pasarObjetoModificar()).grid(row=11, column=2)

        # #####################################################
        # ################ TEMAS #############3#################
        # #####################################################3
        self.temas_opciones = Frame(
            self.root, bg="#376E05", borderwidth=2, relief=RAISED)
        self.temas_opciones.grid(
            row=12, column=0, columnspan=4, padx=1, pady=1, sticky=W+E)

        ancho_boton = 10
        self.temas = StringVar()
        self.temas.set("tema1")
        # Agrego variables de contorl para eleccion de tema
        self.tema_option = IntVar(value=0)

        Label(self.temas_opciones, borderwidth=4, relief=RAISED,
              text="Temas", bg="#222", fg="OrangeRed",).pack(fill=X)
        temas = ["tema1", "tema2", "tema3"]
        for opcion in temas:
            boton = Radiobutton(self.temas_opciones,
                                text=str(opcion), indicatoron=1, value=int(opcion[-1])-1, variable=self.tema_option,
                                bg="#222", fg="OrangeRed", command=self.bg_fg_option)
            boton["width"] = ancho_boton
            boton.pack(side=TOP)

    def SetEstado(self, value):
        self.estado = value
        self.Notificar()

    def GetEstado(self):
        return self.estado

    def pasarObjetoGuardar(self,):
        print(self)
        guardar(self)

    def pasarObjetoEliminar(self,):
        print(self)
        eliminar(self)

    def pasarObjetoModificar(self,):
        print(self)
        modificar(self)

    # #####################################################
    # ################ MODIFICAR TEMA ####################
    # #####################################################

    def bg_fg_option(self):
        self.temas_opciones["bg"] = EleccionTema(self.tema_option.get())
        self.root["bg"] = EleccionTema(self.tema_option.get())
        self.titulo["bg"] = EleccionTema(self.tema_option.get())

    # #####################################################
    # ################ MOSTRAR REGISTROS ##################
    # #####################################################
    def mostrar(self,):

        # limpieza de tabla
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)

        for valor_recuperado in Noticia.select():
            self.tree.insert('', 0, text=valor_recuperado.id, values=(
                valor_recuperado.titulo, valor_recuperado.fecha, valor_recuperado.descripcion, valor_recuperado.estado_de_publicacion))


class ConcreteObserverA(Observador):
    def __init__(self, obj):
        self.observadorA = obj
        self.observadorA.Agregar(self)

    def Update(self):
        print("Actualización dentro de ObservadorConcretoA")
        self.estado = self.observadorA.GetEstado()
        print("Estado = ", self.estado)
        if(self.estado == 1):
            print("Se ha guardado un dato informar")
        elif(self.estado == 2):
            print("Se ha eliminado un dato informar")
        elif(self.estado == 3):
            print("Se ha modificado un dato informar")


class ConcreteObserverB(Observador):
    def __init__(self, obj):
        self.observadorB = obj
        self.observadorB.Agregar(self)

    def Update(self):
        print("Actualización dentro de ObservadorConcretoB")
        LOG_FORMAT = "%(levelname)s %(asctime)s >> %(message)s"
        logging.basicConfig(filename='logfile.log',
                            level=logging.INFO,
                            filemode='w',
                            format=LOG_FORMAT)
        logger = logging.getLogger()
        self.estado = self.observadorB.GetEstado()

        if(self.estado == 1):
            logger.info('Se ha guardado un dato')

        elif(self.estado == 2):
            logger.info('Se ha eliminado un dato')

        elif(self.estado == 3):
            logger.info('Se ha modificado un dato')


"------------- root -------------------------"
if __name__ == '__main__':
    window = Tk()
    application = Producto(window)
    observadorA = ConcreteObserverA(application)
    observadorB = ConcreteObserverB(application)

    application.mostrar()
    window.mainloop()
