class Inmueble:
    """
    Clase base que modela un inmueble con identificador, área, dirección y precio de venta.
    """
    def __init__(self, identificador_inmobiliario, area, direccion):
        self.identificador_inmobiliario = identificador_inmobiliario
        self.area = area
        self.direccion = direccion
        self.precio_venta = 0

    def calcular_precio_venta(self, valor_area):
        self.precio_venta = self.area * valor_area
        return self.precio_venta

    def imprimir(self):
        print(f"Identificador inmobiliario: {self.identificador_inmobiliario}")
        print(f"Área: {self.area} m²")
        print(f"Dirección: {self.direccion}")
        print(f"Precio de venta: ${self.precio_venta}")


class InmuebleVivienda(Inmueble):
    """
    Subclase de Inmueble que representa una vivienda con número de habitaciones y baños.
    """
    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos):
        super().__init__(identificador_inmobiliario, area, direccion)
        self.numero_habitaciones = numero_habitaciones
        self.numero_banos = numero_banos

    def imprimir(self):
        super().imprimir()
        print(f"Número de habitaciones: {self.numero_habitaciones}")
        print(f"Número de baños: {self.numero_banos}")


class Casa(InmuebleVivienda):
    """
    Subclase de InmuebleVivienda que representa una casa con número de pisos.
    """
    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos, numero_pisos):
        super().__init__(identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos)
        self.numero_pisos = numero_pisos

    def imprimir(self):
        super().imprimir()
        print(f"Número de pisos: {self.numero_pisos}")


class Apartamento(InmuebleVivienda):
    """
    Subclase de InmuebleVivienda que representa un apartamento.
    """
    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos):
        super().__init__(identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos)


class Apartaestudio(Apartamento):
    """
    Subclase de Apartamento que representa un apartaestudio.
    """
    VALOR_AREA = 1500000

    def __init__(self, identificador_inmobiliario, area, direccion):
        super().__init__(identificador_inmobiliario, area, direccion, 1, 1)


class CasaRural(Casa):
    """
    Subclase de Casa que representa una casa rural con atributos adicionales de distancia a la cabecera
    municipal y altitud sobre el nivel del mar.
    """
    VALOR_AREA = 1500000

    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos, numero_pisos,
                 distancia_cabecera, altitud):
        super().__init__(identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos, numero_pisos)
        self.distancia_cabecera = distancia_cabecera
        self.altitud = altitud

    def imprimir(self):
        super().imprimir()
        print(f"Distancia a la cabecera municipal: {self.distancia_cabecera} km")
        print(f"Altitud sobre el nivel del mar: {self.altitud} metros")


class CasaUrbana(Casa):
    """
    Subclase de Casa que representa una casa urbana.
    """
    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos, numero_pisos):
        super().__init__(identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos, numero_pisos)


class CasaConjuntoCerrado(CasaUrbana):
    """
    Subclase de CasaUrbana que representa una casa en un conjunto cerrado.
    """
    VALOR_AREA = 2500000

    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos, numero_pisos,
                 valor_administracion, tiene_piscina, tiene_campos_deportivos):
        super().__init__(identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos, numero_pisos)
        self.valor_administracion = valor_administracion
        self.tiene_piscina = tiene_piscina
        self.tiene_campos_deportivos = tiene_campos_deportivos

    def imprimir(self):
        super().imprimir()
        print(f"Valor de administración: ${self.valor_administracion}")
        print(f"Tiene piscina: {'Sí' if self.tiene_piscina else 'No'}")
        print(f"Tiene campos deportivos: {'Sí' if self.tiene_campos_deportivos else 'No'}")


class CasaIndependiente(CasaUrbana):
    """
    Subclase de CasaUrbana que representa una casa independiente.
    """
    VALOR_AREA = 3000000

    def __init__(self, identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos, numero_pisos):
        super().__init__(identificador_inmobiliario, area, direccion, numero_habitaciones, numero_banos, numero_pisos)


class Local(Inmueble):
    """
    Subclase de Inmueble que representa un local.
    """
    def __init__(self, identificador_inmobiliario, area, direccion, tipo_local):
        super().__init__(identificador_inmobiliario, area, direccion)
        self.tipo_local = tipo_local

    def imprimir(self):
        super().imprimir()
        print(f"Tipo de local: {self.tipo_local}")


class LocalComercial(Local):
    """
    Subclase de Local que representa un local comercial.
    """
    VALOR_AREA = 3000000

    def __init__(self, identificador_inmobiliario, area, direccion, tipo_local, centro_comercial):
        super().__init__(identificador_inmobiliario, area, direccion, tipo_local)
        self.centro_comercial = centro_comercial

    def imprimir(self):
        super().imprimir()
        print(f"Centro comercial: {self.centro_comercial}")


class Oficina(Local):
    """
    Subclase de Local que representa una oficina.
    """
    VALOR_AREA = 3500000

    def __init__(self, identificador_inmobiliario, area, direccion, tipo_local, es_gobierno):
        super().__init__(identificador_inmobiliario, area, direccion, tipo_local)
        self.es_gobierno = es_gobierno

    def imprimir(self):
        super().imprimir()
        print(f"Es oficina gubernamental: {'Sí' if self.es_gobierno else 'No'}")


# Ejemplo de uso
if __name__ == "__main__":
    print("\nDatos Apartamento")
    apartamento_familiar = Apartamento(103067, 120, "Avenida Santander 45-45", 3, 2)
    apartamento_familiar.calcular_precio_venta(2000000)
    apartamento_familiar.imprimir()

    print("\nDatos Apartaestudio")
    apartaestudio = Apartaestudio(123454, 50, "Avenida Caracas 30-15")
    apartaestudio.calcular_precio_venta(Apartaestudio.VALOR_AREA)
    apartaestudio.imprimir()

    print("\nDatos Casa Conjunto Cerrado")
    casa_conjunto = CasaConjuntoCerrado(56789, 200, "Calle Principal 123", 4, 3, 2, 150000, True, True)
    casa_conjunto.calcular_precio_venta(CasaConjuntoCerrado.VALOR_AREA)
    casa_conjunto.imprimir()