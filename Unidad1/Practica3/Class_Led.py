import RPi.GPIO as GPIO
import time

class Led:
    def __init__(self, modo, pin_led):
        GPIO.setwarnings(False)

        if modo == "BCM":
            GPIO.setmode(GPIO.BCM)
        else:
            GPIO.setmode(GPIO.BOARD)

        self.pin_led = pin_led
        GPIO.setup(self.pin_led, GPIO.OUT)

    def parpadear(self):
        while True:
            GPIO.output(self.pin_led, True)
            time.sleep(1)
            GPIO.output(self.pin_led, False)
            time.sleep(1)
