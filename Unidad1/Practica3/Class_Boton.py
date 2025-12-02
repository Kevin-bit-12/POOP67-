import RPi.GPIO as GPIO
import time

class Boton:
    def __init__(self, modo, pin_led, pin_boton):
        GPIO.setwarnings(False)

        if modo == "BCM":
            GPIO.setmode(GPIO.BCM)
        else:
            GPIO.setmode(GPIO.BOARD)

        self.pin_led = pin_led
        self.pin_boton = pin_boton

        GPIO.setup(self.pin_led, GPIO.OUT)
        GPIO.setup(self.pin_boton, GPIO.IN)

    def ejecutar(self):
        while True:
            if GPIO.input(self.pin_boton):
                GPIO.output(self.pin_led, True)
            else:
                GPIO.output(self.pin_led, False)
