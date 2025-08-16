import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Practica 02 - PA")
ventana.geometry("250x250")
lbNombre  = ttk.Label(ventana, text="Nombre: ")
lbNombre.place(x=50, y=70)
tbNombre = ttk.Entry(ventana)
tbNombre.place(x=100, y=70)
btnAceptar = ttk.Button(ventana, text="Aceptar")
btnAceptar.place(x=50, y=100)
btnCancelar = ttk.Button(ventana, text="Cancelar")
btnCancelar.place(x=110, y=100)
ventana.mainloop()