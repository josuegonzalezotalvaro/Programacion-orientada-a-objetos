import tkinter as tk
from tkinter import messagebox
import json

FILENAME = "data.json"

def load_data():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_data(data):
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)

def create_entry():
    key = entry_key.get()
    value = entry_value.get()
    if key and value:
        data = load_data()
        if key in data:
            messagebox.showwarning("Advertencia", "La clave ya existe.")
        else:
            data[key] = value
            save_data(data)
            messagebox.showinfo("Éxito", "Entrada creada correctamente.")
    else:
        messagebox.showerror("Error", "Llena ambos campos.")

def read_entry():
    key = entry_key.get()
    data = load_data()
    if key in data:
        messagebox.showinfo("Información", f"{key}: {data[key]}")
    else:
        messagebox.showerror("Error", "Clave no encontrada.")

def update_entry():
    key = entry_key.get()
    value = entry_value.get()
    data = load_data()
    if key in data:
        data[key] = value
        save_data(data)
        messagebox.showinfo("Éxito", "Entrada actualizada correctamente.")
    else:
        messagebox.showerror("Error", "Clave no encontrada.")

def delete_entry():
    key = entry_key.get()
    data = load_data()
    if key in data:
        del data[key]
        save_data(data)
        messagebox.showinfo("Éxito", "Entrada eliminada correctamente.")
    else:
        messagebox.showerror("Error", "Clave no encontrada.")

# Configurar la GUI
root = tk.Tk()
root.title("CRUD con Tkinter")
root.geometry("300x250")

tk.Label(root, text="Clave:").pack()
entry_key = tk.Entry(root)
entry_key.pack()

tk.Label(root, text="Valor:").pack()
entry_value = tk.Entry(root)
entry_value.pack()

tk.Button(root, text="Crear", command=create_entry).pack()
tk.Button(root, text="Leer", command=read_entry).pack()
tk.Button(root, text="Actualizar", command=update_entry).pack()
tk.Button(root, text="Eliminar", command=delete_entry).pack()

root.mainloop()