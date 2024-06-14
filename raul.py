import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import PRIMARY, DANGER

def parse_numeric_input(text):
    # Reemplazar comas con espacios vacíos y luego convertir puntos en comas
    formatted_text = text.replace(',', '').replace('.', ',')
    # Devolver el texto formateado convertido a punto flotante
    return round(float(formatted_text), 2)

# Función para formatear el precio en el formato específico
def format_price_ar(price, centavos):
    price_integer = int(price)
    price_decimal = round(price - price_integer, 2)  # Redondear a dos decimales

    formatted_price = "{:,.0f}".format(price_integer).replace(",", ".")
    if centavos != "00":
        formatted_price += "," + centavos
    elif price_decimal != 0:
        formatted_price += ",{:02d}".format(int(price_decimal * 100))

    return formatted_price

# Función para añadir artículos a la lista
def add_article():
    articulo = article_entry.get().upper()
    cant = quantity_entry.get()
    unit = price_entry.get()
    centavos = centavos_entry.get()  # Obtener los centavos
    try:
        cant = int(cant)
        unit = parse_numeric_input(unit)
        # Añadir los centavos al precio unitario antes de calcular el precio total
        unit_with_centavos = unit + (parse_numeric_input(centavos) / 100)
        total_with_centavos = cant * unit_with_centavos
        total_with_centavos = round(total_with_centavos, 2)  # Redondear el total a dos decimales
        lista.append(f"{articulo} CANT. {cant} PRECIO UNIT. {format_price_ar(unit_with_centavos, '00')} PRECIO TOTAL. {format_price_ar(total_with_centavos, '00')}/ ")
        messagebox.showinfo("Artículo añadido", f"Artículo añadido correctamente.\nPrecio total: {format_price_ar(total_with_centavos, '00')}")
        # Limpiar los campos de entrada
        article_entry.delete(0, tk.END)
        quantity_entry.delete(0, tk.END)
        price_entry.delete(0, tk.END)
        centavos_entry.delete(0, tk.END)
        # Devolver el foco al primer campo de entrada
        article_entry.focus_set()
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores válidos.")

# Función para mostrar la lista de artículos
def show_list():
    if lista:
        items = "\n".join(lista)
        messagebox.showinfo("Lista de artículos", items)
    else:
        messagebox.showinfo("Lista de artículos", "No se añadió ningún ítem")

# Función para eliminar todos los artículos de la lista
def clear_list():
    if lista:
        lista.clear()
        messagebox.showinfo("Lista vaciada", "Todos los artículos han sido eliminados.")
    else:
        messagebox.showinfo("Lista de artículos", "No hay artículos para eliminar.")

# Función para salir de la aplicación
def exit_app():
    if messagebox.askokcancel("Salir", "¿Está seguro que desea salir?"):
        root.destroy()

# Crear la ventana principal
root = ttk.Window(themename="flatly")
root.title("Gestor de Artículos")
root.minsize(400, 250)  # Establecer tamaño mínimo de la ventana

# Crear un Frame para los botones y las entradas
frame = ttk.Frame(root)
frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

# Crear y colocar las entradas de texto
article_label = ttk.Label(frame, text="Artículo:")
article_label.grid(row=0, column=0, sticky="w", padx=(0, 10))
article_entry = ttk.Entry(frame)
article_entry.grid(row=0, column=1, sticky="we")
article_entry.focus_set()

quantity_label = ttk.Label(frame, text="Cantidad:")
quantity_label.grid(row=1, column=0, sticky="w", padx=(0, 10))
quantity_entry = ttk.Entry(frame)
quantity_entry.grid(row=1, column=1, sticky="we")

price_label = ttk.Label(frame, text="Precio por unidad:")
price_label.grid(row=2, column=0, sticky="w", padx=(0, 10))
price_entry = ttk.Entry(frame)
price_entry.grid(row=2, column=1, sticky="we")

# Crear una etiqueta y un cuadro de entrada para los centavos
centavos_label = ttk.Label(frame, text="Centavos:")
centavos_label.grid(row=3, column=0, sticky="w", padx=(0, 10))
centavos_entry = ttk.Entry(frame)
centavos_entry.grid(row=3, column=1, sticky="we")

# Crear y colocar los botones
button_options = {'padx': 10, 'pady': 10, 'ipadx': 20, 'ipady': 10, 'sticky': "ew"}

add_button = ttk.Button(frame, text="Añadir artículo", command=add_article, bootstyle=PRIMARY)
add_button.grid(row=4, column=0, columnspan=2, **button_options)

show_button = ttk.Button(frame, text="Mostrar lista", command=show_list, bootstyle=PRIMARY)
show_button.grid(row=5, column=0, columnspan=2, **button_options)

clear_button = ttk.Button(frame, text="Eliminar todos los artículos", command=clear_list, bootstyle=DANGER)
clear_button.grid(row=6, column=0, columnspan=2, **button_options)

exit_button = ttk.Button(frame, text="Salir", command=exit_app, bootstyle=DANGER)
exit_button.grid(row=7, column=0, columnspan=2, **button_options)

# Configurar el Frame para que sea responsive
frame.columnconfigure((0, 1), weight=1)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Inicializar la lista de artículos
lista = []

# Ejecutar la aplicación
root.mainloop()