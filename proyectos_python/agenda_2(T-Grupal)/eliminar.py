"------ importaciones de modulos --------------"

from tkinter import *

"------ variables --------------"

archivo = 'persona'
campos = ('dni')

"------ definiciones --------------"


def imprimir(variables):
    for variable in variables:
        print('Input => "%s"' % variable.get())


def CrearFormEliminar(root, campos):
    formulario = Frame(root)
    div1 = Frame(formulario, width=100)
    div2 = Frame(formulario, padx=7, pady=2)
    formulario.pack(fill=X)
    div1.pack(side=LEFT)
    div2.pack(side=RIGHT, expand=YES, fill=X)
    variables = []
    lab = Label(div1, width=10, text="ID")
    ent = Entry(div2, width=30, relief=SUNKEN)
    lab.pack(side=TOP)
    ent.pack(side=TOP, fill=X)
    var = StringVar()
    ent.config(textvariable=var)
    var.set('---')
    variables.append(var)
    return variables


"------------- root -------------------------"

if __name__ == '__main__':
    root = Tk()
    vars_elimina = CrearFormEliminar(root, campos)
    Button(root, text='Imprimir', command=(
        lambda: imprimir(vars_elimina))).pack(side=LEFT)
    Cerrar(root).pack(side=RIGHT)
    root.bind('<Return>', (lambda event: imprimir(vars_elimina)))
    root.mainloop()