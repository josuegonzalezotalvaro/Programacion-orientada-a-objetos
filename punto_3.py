# Clase raíz
class Mascota:
    def __init__(self, nombre, edad, color):
        self.nombre = nombre
        self.edad = edad
        self.color = color

# -------------------------
# PERROS
# -------------------------
class Perro(Mascota):
    def __init__(self, nombre, edad, color, peso, muerde):
        super().__init__(nombre, edad, color)
        self.peso = peso
        self.muerde = muerde

    @staticmethod
    def sonido():
        print("Los perros ladran")

# Tamaños
class PerroPequeño(Perro): pass
class PerroMediano(Perro): pass
class PerroGrande(Perro): pass

# Razas de perros pequeños
class Caniche(PerroPequeño): pass
class YorkshireTerrier(PerroPequeño): pass
class Schnauzer(PerroPequeño): pass
class Chihuahua(PerroPequeño): pass

# Razas de perros medianos
class Collie(PerroMediano): pass
class Dalmata(PerroMediano): pass
class Bulldog(PerroMediano): pass
class Galgo(PerroMediano): pass
class Sabueso(PerroMediano): pass

# Razas de perros grandes
class PastorAleman(PerroGrande): pass
class Doberman(PerroGrande): pass
class Rottweiler(PerroGrande): pass

# -------------------------
# GATOS
# -------------------------
class Gato(Mascota):
    def __init__(self, nombre, edad, color, altura_salto, longitud_salto):
        super().__init__(nombre, edad, color)
        self.altura_salto = altura_salto
        self.longitud_salto = longitud_salto

    @staticmethod
    def sonido():
        print("Los gatos maúllan y ronronean")

# Tipos por pelaje
class GatoSinPelo(Gato): pass
class GatoPeloLargo(Gato): pass
class GatoPeloCorto(Gato): pass

# Razas de gatos sin pelo
class Esfinge(GatoSinPelo): pass
class Elfo(GatoSinPelo): pass
class Donskoy(GatoSinPelo): pass

# Razas de gatos de pelo largo
class Angora(GatoPeloLargo): pass
class Himalayo(GatoPeloLargo): pass
class Balines(GatoPeloLargo): pass
class Somali(GatoPeloLargo): pass

# Razas de gatos de pelo corto
class AzulRuso(GatoPeloCorto): pass
class Britanico(GatoPeloCorto): pass
class Manx(GatoPeloCorto): pass
class DevonRex(GatoPeloCorto): pass

# -------------------------
# EJEMPLO
# -------------------------
# Crear instancias
perro = Bulldog("Rex", 4, "Marrón", 25.0, True)
gato = AzulRuso("Michi", 2, "Gris", 1.0, 2.5)

# Mostrar sonidos
Bulldog.sonido()    # Los perros ladran
AzulRuso.sonido()   # Los gatos maúllan y ronronean

# Acceder a atributos
print(f"{perro.nombre}, {perro.edad} años, color {perro.color}, muerde: {perro.muerde}")
print(f"{gato.nombre}, salta {gato.altura_salto}m de alto y mide {gato.longitud_salto}m de largo")