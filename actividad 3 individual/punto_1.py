class Cuenta:
    """
    Clase que modela una cuenta bancaria con atributos básicos como saldo,
    número de consignaciones, número de retiros, tasa anual y comisión mensual.
    """
    def __init__(self, saldo, tasa_anual):
        self.saldo = saldo
        self.numero_consignaciones = 0
        self.numero_retiros = 0
        self.tasa_anual = tasa_anual
        self.comision_mensual = 0

    def consignar(self, cantidad):
        """
        Consigna una cantidad de dinero en la cuenta, actualizando el saldo
        y aumentando el número de consignaciones.
        """
        self.saldo += cantidad
        self.numero_consignaciones += 1

    def retirar(self, cantidad):
        """
        Retira una cantidad de dinero de la cuenta si el saldo es suficiente.
        """
        nuevo_saldo = self.saldo - cantidad
        if nuevo_saldo >= 0:
            self.saldo -= cantidad
            self.numero_retiros += 1
        else:
            print("La cantidad a retirar excede el saldo actual.")

    def calcular_interes(self):
        """
        Calcula el interés mensual basado en la tasa anual y lo añade al saldo.
        """
        tasa_mensual = self.tasa_anual / 12
        interes_mensual = self.saldo * tasa_mensual
        self.saldo += interes_mensual

    def extracto_mensual(self):
        """
        Genera el extracto mensual, aplicando la comisión mensual
        y calculando el interés.
        """
        self.saldo -= self.comision_mensual
        self.calcular_interes()


class CuentaAhorros(Cuenta):
    """
    Clase que modela una cuenta de ahorros como subclase de Cuenta.
    Añade un atributo adicional para determinar si la cuenta está activa.
    """
    def __init__(self, saldo, tasa_anual):
        super().__init__(saldo, tasa_anual)
        self.activa = saldo >= 10000

    def retirar(self, cantidad):
        """
        Retira una cantidad de dinero si la cuenta está activa.
        """
        if self.activa:
            super().retirar(cantidad)
            if self.saldo < 10000:
                self.activa = False
        else:
            print("La cuenta está inactiva. No se puede retirar.")

    def consignar(self, cantidad):
        """
        Consigna una cantidad de dinero si la cuenta está activa.
        """
        if self.activa:
            super().consignar(cantidad)
        else:
            print("La cuenta está inactiva. No se puede consignar.")

    def extracto_mensual(self):
        """
        Genera el extracto mensual, aplicando comisiones adicionales
        si hay más de 4 retiros.
        """
        if self.numero_retiros > 4:
            self.comision_mensual += (self.numero_retiros - 4) * 1000
        super().extracto_mensual()
        if self.saldo < 10000:
            self.activa = False

    def imprimir(self):
        """
        Muestra el estado actual de la cuenta.
        """
        print(f"Saldo: ${self.saldo:.2f}")
        print(f"Comisión mensual: ${self.comision_mensual:.2f}")
        print(f"Número de transacciones: {self.numero_consignaciones + self.numero_retiros}")
        print(f"Cuenta activa: {self.activa}")


class CuentaCorriente(Cuenta):
    """
    Clase que modela una cuenta corriente como subclase de Cuenta.
    Añade un atributo adicional para manejar sobregiros.
    """
    def __init__(self, saldo, tasa_anual):
        super().__init__(saldo, tasa_anual)
        self.sobregiro = 0

    def retirar(self, cantidad):
        """
        Permite realizar un retiro incluso si el saldo no es suficiente,
        generando un sobregiro.
        """
        resultado = self.saldo - cantidad
        if resultado < 0:
            self.sobregiro -= resultado
            self.saldo = 0
        else:
            super().retirar(cantidad)

    def consignar(self, cantidad):
        """
        Permite consignar dinero, cubriendo primero el sobregiro si lo hay.
        """
        if self.sobregiro > 0:
            residuo = self.sobregiro - cantidad
            if residuo > 0:
                self.sobregiro = residuo
            else:
                self.sobregiro = 0
                self.saldo += -residuo
        else:
            super().consignar(cantidad)

    def imprimir(self):
        """
        Muestra el estado actual de la cuenta.
        """
        print(f"Saldo: ${self.saldo:.2f}")
        print(f"Comisión mensual: ${self.comision_mensual:.2f}")
        print(f"Número de transacciones: {self.numero_consignaciones + self.numero_retiros}")
        print(f"Sobregiro: ${self.sobregiro:.2f}")


# Prueba del programa
if __name__ == "__main__":
    print("Cuenta de Ahorros:")
    saldo_inicial = float(input("Ingrese el saldo inicial: "))
    tasa_anual = float(input("Ingrese la tasa anual (%): "))
    cuenta_ahorros = CuentaAhorros(saldo_inicial, tasa_anual)

    cantidad_consignar = float(input("Ingrese la cantidad a consignar: "))
    cuenta_ahorros.consignar(cantidad_consignar)

    cantidad_retirar = float(input("Ingrese la cantidad a retirar: "))
    cuenta_ahorros.retirar(cantidad_retirar)

    cuenta_ahorros.extracto_mensual()
    cuenta_ahorros.imprimir()