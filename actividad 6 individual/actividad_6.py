import tkinter as tk
from tkinter import messagebox
import json

FILENAME = "data.json"

class GestorCRUD:
    def cargar_datos(self) -> dict:
        try:
            with open(FILENAME, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def guardar_datos(self, datos: dict):
        with open(FILENAME, "w") as file:
            json.dump(datos, file, indent=4)

    def crear_entrada(self, clave: str, valor: str):
        datos = self.cargar_datos()
        if clave in datos:
            raise ValueError("La clave ya existe.")
        datos[clave] = valor
        self.guardar_datos(datos)

    def leer_entrada(self, clave: str) -> str:
        datos = self.cargar_datos()
        if clave in datos:
            return datos[clave]
        else:
            raise KeyError("Clave no encontrada.")

    def actualizar_entrada(self, clave: str, valor: str):
        datos = self.cargar_datos()
        if clave in datos:
            datos[clave] = valor
            self.guardar_datos(datos)
        else:
            raise KeyError("Clave no encontrada.")

    def eliminar_entrada(self, clave: str):
        datos = self.cargar_datos()
        if clave in datos:
            del datos[clave]
            self.guardar_datos(datos)
        else:
            raise KeyError("Clave no encontrada.")


class Aplicación:
    def __init__(self):
        self.raíz = tk.Tk()
        self.raíz.title("CRUD con Tkinter")
        self.raíz.geometry("300x250")

        self.gestor = GestorCRUD()

        tk.Label(self.raíz, text="Clave:").pack()
        self.entrada_clave = tk.Entry(self.raíz)
        self.entrada_clave.pack()

        tk.Label(self.raíz, text="Valor:").pack()
        self.entrada_valor = tk.Entry(self.raíz)
        self.entrada_valor.pack()

        self.btn_crear = tk.Button(self.raíz, text="Crear", command=self.crear)
        self.btn_crear.pack()

        self.btn_leer = tk.Button(self.raíz, text="Leer", command=self.leer)
        self.btn_leer.pack()

        self.btn_actualizar = tk.Button(self.raíz, text="Actualizar", command=self.actualizar)
        self.btn_actualizar.pack()

        self.btn_eliminar = tk.Button(self.raíz, text="Eliminar", command=self.eliminar)
        self.btn_eliminar.pack()

    def crear(self):
        clave = self.entrada_clave.get()
        valor = self.entrada_valor.get()
        if clave and valor:
            try:
                self.gestor.crear_entrada(clave, valor)
                messagebox.showinfo("Éxito", "Entrada creada correctamente.")
            except ValueError as e:
                messagebox.showwarning("Advertencia", str(e))
        else:
            messagebox.showerror("Error", "Llena ambos campos.")

    def leer(self):
        clave = self.entrada_clave.get()
        try:
            valor = self.gestor.leer_entrada(clave)
            messagebox.showinfo("Información", f"{clave}: {valor}")
        except KeyError as e:
            messagebox.showerror("Error", str(e))

    def actualizar(self):
        clave = self.entrada_clave.get()
        valor = self.entrada_valor.get()
        try:
            self.gestor.actualizar_entrada(clave, valor)
            messagebox.showinfo("Éxito", "Entrada actualizada correctamente.")
        except KeyError as e:
            messagebox.showerror("Error", str(e))

    def eliminar(self):
        clave = self.entrada_clave.get()
        try:
            self.gestor.eliminar_entrada(clave)
            messagebox.showinfo("Éxito", "Entrada eliminada correctamente.")
        except KeyError as e:
            messagebox.showerror("Error", str(e))

    def iniciar(self):
        self.raíz.mainloop()


# Ejecutar la aplicación
if __name__ == "__main__":
    app = Aplicación()
    app.iniciar()
