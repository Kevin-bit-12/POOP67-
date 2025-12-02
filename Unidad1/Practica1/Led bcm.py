import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
LED_PIN = 18
GPIO.setup(LED_PIN, GPIO.OUT)

print("Encendiendo LED por 5 segundos en modo BCM...")
GPIO.output(LED_PIN, GPIO.HIGH)
time.sleep(5)
GPIO.output(LED_PIN, GPIO.LOW)

GPIO.cleanup()
