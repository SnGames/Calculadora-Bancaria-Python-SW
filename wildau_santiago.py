import time


# =========================================
# CONSTANTES
# =========================================

PIN_CORRECTO = "1234"
INTENTOS_MAXIMOS = 3
SALDO_INICIAL = 50000

OPCION_DEPOSITAR = 1
OPCION_EXTRAER = 2
OPCION_SALIR = 3

INTENTOS_CONEXION = 3
PAUSA_CONEXION = 1


# =========================================
# FUNCIONES
# =========================================

def simular_conexion():
    """Muestra los intentos de conexión al servidor."""
    # escribir el código de la función
    for i in range(INTENTOS_CONEXION):
        print(f"Conectando al servidor... intento {i+1}")
        time.sleep(PAUSA_CONEXION)


def validar_acceso(pin_correcto):
    """Pide el PIN y devuelve True si es correcto dentro de los intentos permitidos."""
    # escribir el código de la función
    intentos = INTENTOS_MAXIMOS
    
    while intentos > 0:

        pin = input(f"Ingrese el pin para ingresar al cajero (quedan {intentos} intentos): ")

        if pin == pin_correcto:
            print("Pin correcto")
            time.sleep(0.7)
            return True
        else:
            print("Pin incorrecto")
            intentos -= 1

        time.sleep(0.7)
    
    return False



def mostrar_menu():
    """Muestra el menú y devuelve una opción válida."""
    # escribir el código de la función
    while True:
        print("1. Depositar")
        print("2. Extraer")
        print("3. Salir")

        opcion = int(input("Elige una opción: "))

        if opcion == 1 or opcion == 2 or opcion == 3:
            return opcion
        else:
            print("Opción incorrecta. Elige 1, 2 o 3")
        
        time.sleep(0.7) 


def pedir_monto():
    """Pide un monto mayor a cero y lo devuelve."""
    # escribir el código de la función
    monto = int(input("Ingrese el monto a depositar: "))

    if monto > 0:
        return monto
    else:
        print("Error: el monto debe ser mayor a 0. Operación cancelada")
        time.sleep(0.7)



def depositar(saldo, monto):
    """Devuelve el saldo luego de depositar."""
    # escribir el código de la función
    return saldo + monto


def extraer(saldo, monto):
    """Intenta extraer dinero. Si no alcanza, mantiene el saldo."""
    # escribir el código de la función
    if saldo >= monto:
        return saldo - monto
    else:
        print("Fondos insuficientes")
        return saldo


# =========================================
# PROGRAMA PRINCIPAL
# =========================================

def main():
    """Ejecuta el cajero automático."""
    simular_conexion()

    if not validar_acceso(PIN_CORRECTO):
        print("Acceso denegado.")
        return

    saldo = SALDO_INICIAL
    print("Acceso concedido.")
    print("Saldo actual:", saldo)

    while True:
        opcion = mostrar_menu()

        if opcion == OPCION_DEPOSITAR:
            monto = pedir_monto()
            if monto != None: #agregado por mi
                saldo = depositar(saldo, monto)
                print("Depósito realizado.")
                print("Saldo actual:", saldo)

        elif opcion == OPCION_EXTRAER:
            monto = pedir_monto()
            if monto != None: #agregado por mi
                saldo = extraer(saldo, monto)
                print("Saldo actual:", saldo)

        else:
            print("Gracias por usar el cajero.")
            break


main()