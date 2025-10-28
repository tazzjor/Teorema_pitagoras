import tkinter as tk
from tkinter import ttk, messagebox
from math import sqrt
from idiomas import textos

idioma_actual = "Español"  # Idioma por defecto

def cambiar_idioma(event):
    global idioma_actual
    idioma_actual = combo_idioma.get()
    actualizar_textos()

def actualizar_textos():
    t = textos[idioma_actual]
    ventana.title(t["titulo"])
    label_seleccion.config(text=t["seleccion"])
    label_valor1.config(text=t["valor1"])
    label_valor2.config(text=t["valor2"])
    boton_calcular.config(text=t["calcular"])
    label_resultado.config(text=t["resultado"])
    combo_lado.config(values=[t["hipotenusa"], t["opuesto"], t["adyacente"]])
    combo_lado.set("")

def calcular():
    t = textos[idioma_actual]
    lado = combo_lado.get()
    try:
        val1 = float(entry_valor1.get())
        val2 = float(entry_valor2.get())

        if lado == t["hipotenusa"]:
            resultado = sqrt(val1**2 + val2**2)
        elif lado == t["opuesto"] or lado == t["adyacente"]:
            if val1**2 <= val2**2:
                raise ValueError(t["error_hipotenusa"])
            resultado = sqrt(val1**2 - val2**2)
        else:
            raise ValueError(t["error_lado"])

        label_resultado.config(text=f"{t['resultado']} {round(resultado, 2)}")
    except ValueError as e:
        messagebox.showerror(t["error"], str(e))

# Ventana principal
ventana = tk.Tk()
ventana.geometry("320x280")

# Selector de idioma
combo_idioma = ttk.Combobox(ventana, values=list(textos.keys()))
combo_idioma.set(idioma_actual)
combo_idioma.pack(pady=5)
combo_idioma.bind("<<ComboboxSelected>>", cambiar_idioma)

# Selector de lado
label_seleccion = tk.Label(ventana)
label_seleccion.pack()
combo_lado = ttk.Combobox(ventana)
combo_lado.pack()

# Entradas
label_valor1 = tk.Label(ventana)
label_valor1.pack()
entry_valor1 = tk.Entry(ventana)
entry_valor1.pack()

label_valor2 = tk.Label(ventana)
label_valor2.pack()
entry_valor2 = tk.Entry(ventana)
entry_valor2.pack()

# Botón y resultado
boton_calcular = tk.Button(ventana, command=calcular)
boton_calcular.pack(pady=10)

label_resultado = tk.Label(ventana)
label_resultado.pack()

# Inicializar textos
actualizar_textos()
ventana.mainloop()