import RPi.GPIO as GPIO
import Adafruit_DHT
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

PIN_LED = 17
PIN_BOTON = 27
PIN_DHT = 4

GPIO.setup(PIN_LED, GPIO.OUT)
GPIO.setup(PIN_BOTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

sensor_dht = Adafruit_DHT.DHT11   # Cambiar si usas DHT22


class Led:
    def encender(self):
        GPIO.output(PIN_LED, True)

    def apagar(self):
        GPIO.output(PIN_LED, False)


class Boton:
    def esta_presionado(self):
        return GPIO.input(PIN_BOTON) == GPIO.HIGH


class SensorDHT:
    def leer(self):
        humedad, temperatura = Adafruit_DHT.read_retry(sensor_dht, PIN_DHT)
        return humedad, temperatura
