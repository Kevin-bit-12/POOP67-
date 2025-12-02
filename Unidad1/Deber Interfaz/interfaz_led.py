import programa_led as led
import time

def interfaz():
    while True:
        print("\n=== CONTROL DE LED ===")
        print("1. Modo BCM")
        print("2. Modo BOARD")
        print("3. Salir")
        modo = input("Selecciona modo (1, 2 o 3): ")

        if modo == "3":
            print("Saliendo del programa...")
            led.limpiar()
            break

        if modo == "1":
            pin_led, pin_boton = led.configurar_modo("BCM")
        elif modo == "2":
            pin_led, pin_boton = led.configurar_modo("BOARD")
        else:
            print("Opción no válida.")
            continue

        print("\n1. Modo parpadeo automático")
        print("2. Modo control con botón")
        opcion = input("Elige opción: ")

        if opcion == "1":
            led.modo_parpadeo(pin_led)
        elif opcion == "2":
            led.modo_boton(pin_led, pin_boton)
        else:
            print("Opción no válida.")

        print("Volviendo al menú principal...")
        time.sleep(1)

if __name__ == "__main__":
    interfaz()
