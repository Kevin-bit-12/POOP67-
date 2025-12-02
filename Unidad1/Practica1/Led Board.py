import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
LED_PIN = 12
GPIO.setup(LED_PIN, GPIO.OUT)

print("Encendiendo LED por 5 segundos en modo BOARD...")
GPIO.output(LED_PIN, GPIO.HIGH)
time.sleep(5)
GPIO.output(LED_PIN, GPIO.LOW)

GPIO.cleanup()
