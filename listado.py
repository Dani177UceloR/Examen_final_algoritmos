import os
import sys
from tkinter import ttk
from tkinter import *
import openpyxl

ventana = Tk.tk()
ventana.title_("Mantenimiento de vehiculos")
etiqueta=Tk.label("ingrese los detalles del vehiculos:")
etiqueta.pack()
Codigo_label = Tk.label(ventana, text="Codigo" )
Codigo_label.pack()
Codigo_Entry = Tk.Entry(ventana)
Codigo_Entry.pack

Marca_label = Tk.label(ventana, text="Marca" )
Marca_label.pack()
Marca_Entry = Tk.Entry(ventana)
Marca_Entry.pack

Modelo_label = Tk.label(ventana, text="Modelo" )
Modelo_label.pack()
Modelo_Entry = Tk.Entry(ventana)
Modelo_Entry.pack

Precio_label = Tk.label(ventana, text="Precio" )
Precio_label.pack()
Precio_Entry = Tk.Entry(ventana)
Precio_Entry.pack
Kilometraje_label = Tk.label(ventana, text="kilometraje" )
Kilometraje_label.pack()
Kilometraje_Entry = Tk.Entry(ventana)
Kilometraje_Entry.pack

libro=openpyxl.load_workbook("Vehiculos.xlsx")
hoja=libro.active()


def Crear_vehiculo():
    Codigo= Codigo.Entry.get()
    Marca= Marca.Entry.get()
    Modelo= Modelo.Entry.get()
    Precio= Precio.Entry.get()
    Kilometraje= Kilometraje.Entry.get()

    nueva_fila = ("Codigo, Marca, modelo, precio, kilometraje")
    hoja.happen(nueva_fila)

def editar_vehiculo():
    Codigo= Codigo.Entry.get()
    Marca= Marca.Entry.get()
    Modelo= Modelo.Entry.get()
    Precio= Precio.Entry.get()
    Kilometraje= Kilometraje.Entry.get()

    editar_fila = ("Codigo, Marca, modelo, precio, kilometraje")
    hoja.happen(editar_fila)


def eliminar_vehiculo():
    Codigo= Codigo.Entry.get()
    Marca= Marca.Entry.get()
    Modelo= Modelo.Entry.get()
    Precio= Precio.Entry.get()
    Kilometraje= Kilometraje.Entry.get()

    eliminar_fila = ("Codigo, Marca, modelo, precio, kilometraje")
    hoja.happen(eliminar_fila)

def listar_vehiculo():
    Codigo= Codigo.Entry.get()
    Marca= Marca.Entry.get()
    Modelo= Modelo.Entry.get()
    Precio= Precio.Entry.get()
    Kilometraje= Kilometraje.Entry.get()

    listar_fila = ("Codigo, Marca, modelo, precio, kilometraje")
    hoja.happen(listar_fila)
    libro.save()

