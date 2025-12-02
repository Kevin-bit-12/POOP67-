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


class Logger:
    def __init__(self, archivo):
        self.archivo = archivo

    def escribir(self, mensaje):
        hora = time.strftime("[%Y-%m-%d %H:%M:%S]")
        with open(self.archivo, 'a') as f:
            f.write(f"{hora} {mensaje}\n")


logger = Logger("log.txt")   # Logger global


class Led:
    def encender(self):
        GPIO.output(PIN_LED, True)
        logger.escribir("LED encendido")

    def apagar(self):
        GPIO.output(PIN_LED, False)
        logger.escribir("LED apagado")


class Boton:
    def esta_presionado(self):
        estado = GPIO.input(PIN_BOTON) == GPIO.HIGH
        logger.escribir(f"Botón leído: {'PRESIONADO' if estado else 'suelto'}")
        return estado


class SensorDHT:
    def leer(self):
        humedad, temperatura = Adafruit_DHT.read_retry(sensor_dht, PIN_DHT)
        if humedad is None:
            logger.escribir("Error al leer DHT")
        else:
            logger.escribir(f"DHT leído: Temp={temperatura}°C Hum={humedad}%")
        return humedad, temperatura
