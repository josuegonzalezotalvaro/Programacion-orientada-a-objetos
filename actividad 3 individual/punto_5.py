class Profesor:
    """
    Clase base Profesor.
    """
    def imprimir(self):
        print("Es un profesor.")

class ProfesorTitular(Profesor):
    """
    Subclase ProfesorTitular que hereda de Profesor.
    """
    def imprimir(self):
        print("Es un profesor titular.")

def main():
    """
    Función principal que demuestra el uso de polimorfismo.
    """
    profesor1 = ProfesorTitular()  # Se declara como Profesor pero se instancia como ProfesorTitular
    profesor1.imprimir()           # Salida: "Es un profesor titular."

if __name__ == "__main__":
    main()
