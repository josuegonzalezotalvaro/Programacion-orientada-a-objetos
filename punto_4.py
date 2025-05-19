# Clase base
class Persona:
    def __init__(self, nombre: str, direccion: str):
        self.nombre = nombre
        self.direccion = direccion

    def getNombre(self) -> str:
        return self.nombre

    def getDireccion(self) -> str:
        return self.direccion

    def setNombre(self, nombre: str):
        self.nombre = nombre

    def setDireccion(self, direccion: str):
        self.direccion = direccion


# Subclase Estudiante
class Estudiante(Persona):
    def __init__(self, nombre: str, direccion: str, carrera: str, semestre: int):
        super().__init__(nombre, direccion)
        self.carrera = carrera
        self.semestre = semestre

    def getCarrera(self) -> str:
        return self.carrera

    def getSemestre(self) -> int:
        return self.semestre

    def setCarrera(self, carrera: str):
        self.carrera = carrera

    def setSemestre(self, semestre: int):
        self.semestre = semestre


# Subclase Profesor
class Profesor(Persona):
    def __init__(self, nombre: str, direccion: str, departamento: str, categoria: str):
        super().__init__(nombre, direccion)
        self.departamento = departamento
        self.categoria = categoria

    def getDepartamento(self) -> str:
        return self.departamento

    def getCategoria(self) -> str:
        return self.categoria

    def setDepartamento(self, departamento: str):
        self.departamento = departamento

    def setCategoria(self, categoria: str):
        self.categoria = categoria


# Ejemplo

# Crear un estudiante
est = Estudiante("Ana García", "Calle 123", "Ingeniería", 3)

# Acceder a sus datos
print("Estudiante:")
print("Nombre:", est.getNombre())
print("Dirección:", est.getDireccion())
print("Carrera:", est.getCarrera())
print("Semestre:", est.getSemestre())

# Modificar semestre
est.setSemestre(4)
print("Semestre actualizado:", est.getSemestre())

print()

# Crear un profesor
prof = Profesor("Dr. Luis Pérez", "Av. Principal 456", "Matemáticas", "Titular")

# Acceder a sus datos
print("Profesor:")
print("Nombre:", prof.getNombre())
print("Dirección:", prof.getDireccion())
print("Departamento:", prof.getDepartamento())
print("Categoría:", prof.getCategoria())

# Cambiar categoría
prof.setCategoria("Asociado")
print("Categoría actualizada:", prof.getCategoria())