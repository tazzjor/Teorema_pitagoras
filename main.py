import tkinter as tk
from tkinter import ttk, messagebox
from math import sqrt
from idiomas import textos


idioma_actual = "Español"


def cambiar_idioma(event=None):
    global idioma_actual
    idioma_actual = combo_idioma.get()
    actualizar_textos()


def cambiar_lado(event=None):
    actualizar_etiquetas_valores()


def actualizar_textos():
    t = textos[idioma_actual]

    # Conservamos la opción seleccionada antes de cambiar el idioma
    lado_anterior = combo_lado.current()

    ventana.title(t["titulo"])
    label_seleccion.config(text=t["seleccion"])
    boton_calcular.config(text=t["calcular"])
    label_resultado.config(text=t["resultado"])

    combo_lado.config(
        values=[
            t["hipotenusa"],
            t["opuesto"],
            t["adyacente"]
        ]
    )

    # Si había un lado seleccionado, mantenemos su posición
    if lado_anterior >= 0:
        combo_lado.current(lado_anterior)
    else:
        combo_lado.set("")

    actualizar_etiquetas_valores()


def actualizar_etiquetas_valores():
    t = textos[idioma_actual]
    lado = combo_lado.get()

    if lado == t["hipotenusa"]:
        label_valor1.config(text=t["cateto_opuesto"])
        label_valor2.config(text=t["cateto_adyacente"])

    elif lado == t["opuesto"]:
        label_valor1.config(text=t["dato_hipotenusa"])
        label_valor2.config(text=t["cateto_adyacente"])

    elif lado == t["adyacente"]:
        label_valor1.config(text=t["dato_hipotenusa"])
        label_valor2.config(text=t["cateto_opuesto"])

    else:
        label_valor1.config(text=t["valor1"])
        label_valor2.config(text=t["valor2"])

def calcular():
    t = textos[idioma_actual]
    lado = combo_lado.get()

    try:
        val1 = float(entry_valor1.get())
        val2 = float(entry_valor2.get())

        if val1 <= 0 or val2 <= 0:
            raise ValueError(t["error_valores"])

        if lado == t["hipotenusa"]:
            resultado = sqrt(val1**2 + val2**2)

        elif lado == t["opuesto"] or lado == t["adyacente"]:
            # En estos dos casos, el primer valor es la hipotenusa
            if val1 <= val2:
                raise ValueError(t["error_hipotenusa"])

            resultado = sqrt(val1**2 - val2**2)

        else:
            raise ValueError(t["error_lado"])

        label_resultado.config(
            text=f"{t['resultado']} {round(resultado, 2)}"
        )

    except ValueError as error:
        messagebox.showerror(t["error"], str(error))


# Ventana principal
ventana = tk.Tk()
ventana.geometry("320x300")


# Selector de idioma
combo_idioma = ttk.Combobox(
    ventana,
    values=list(textos.keys()),
    state="readonly"
)
combo_idioma.set(idioma_actual)
combo_idioma.pack(pady=5)
combo_idioma.bind("<<ComboboxSelected>>", cambiar_idioma)


# Selector de lado
label_seleccion = tk.Label(ventana)
label_seleccion.pack()

combo_lado = ttk.Combobox(
    ventana,
    state="readonly"
)
combo_lado.pack()
combo_lado.bind("<<ComboboxSelected>>", cambiar_lado)


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
boton_calcular = tk.Button(
    ventana,
    command=calcular
)
boton_calcular.pack(pady=10)


label_resultado = tk.Label(ventana)
label_resultado.pack()


# Inicializar textos
actualizar_textos()

ventana.mainloop()