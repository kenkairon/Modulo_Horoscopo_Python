# main.py

from zodiac import obtener_signo_zodiacal  # Importa desde el paquete zodiac

def main():
    
    while True:

        salir = int(input("Opción (1) - Para saber tu signo\nOpción (0) - Salir\nElige una opción: "))


        if salir == 0:
            print("Saliendo........")
            break
        else:
            mes = int(input("Ingresa el mes (1-12): "))
            dia = int(input("Ingresa el día : "))
        obtener_signo_zodiacal(mes, dia)

if __name__ == "__main__":
    main()
