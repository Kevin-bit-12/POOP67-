import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

def configurar_modo(modo):
    if modo == "BCM":
        GPIO.setmode(GPIO.BCM)
        pin_led = 18
        pin_boton = 23
    elif modo == "BOARD":
        GPIO.setmode(GPIO.BOARD)
        pin_led = 12
        pin_boton = 16
    else:
        print("Modo no válido, usando BCM por defecto.")
        GPIO.setmode(GPIO.BCM)
        pin_led = 18
        pin_boton = 23

    GPIO.setup(pin_led, GPIO.OUT)
    GPIO.setup(pin_boton, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    return pin_led, pin_boton

def modo_parpadeo(pin_led):
    print("Modo parpadeo automático.")
    for i in range(10):
        GPIO.output(pin_led, True)
        print("LED encendido")
        time.sleep(0.5)
        GPIO.output(pin_led, False)
        print("LED apagado")
        time.sleep(0.5)

def modo_boton(pin_led, pin_boton):
    print("Modo control con botón. CTRL+C para salir.")
    try:
        while True:
            estado = GPIO.input(pin_boton)
            if estado == GPIO.LOW:
                GPIO.output(pin_led, True)
                print("Botón presionado -> LED encendido")
            else:
                GPIO.output(pin_led, False)
                print("Botón suelto -> LED apagado")
            time.sleep(0.2)
    except KeyboardInterrupt:
        print("Saliendo de modo botón.")

def limpiar():
    GPIO.cleanup()
    print("GPIO limpiado por programa_led.")
