import RPi.GPIO as GPIO
import Adafruit_DHT
import time

# ==============================
#  CONFIGURACIÓN GPIO REAL
# ==============================

GPIO.setmode(GPIO.BCM)

PIN_LED = 17
PIN_BOTON = 27
PIN_DHT = 4

GPIO.setup(PIN_LED, GPIO.OUT)
GPIO.setup(PIN_BOTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

sensorDHT = Adafruit_DHT.DHT11   # Cambiar a DHT22 si es el caso


# ==============================
#  CLASES DE ROBOTS
# ==============================

class Robot:
    def __init__(self, nombre):
        self.nombre = nombre
        self.bateria = 100
        print(f"\n🤖 Creado robot: {self.nombre}")

    def mover(self, pasos):
        print(f"{self.nombre} se mueve {pasos} pasos")
        self.bateria -= 10
        print("Batería:", self.bateria)

    def estado(self):
        print(f"{self.nombre}: batería = {self.bateria}")


# --------------------- ROBOT CONSTRUCTOR → LED
class RobotConstructor(Robot):
    def __init__(self, nombre):
        super().__init__(nombre)

    def encender_led(self):
        GPIO.output(PIN_LED, GPIO.HIGH)
        print("💡 LED encendido (Constructor trabajando)")

    def apagar_led(self):
        GPIO.output(PIN_LED, GPIO.LOW)
        print("💡 LED apagado")

    def construir(self):
        print(f"{self.nombre}: Construyendo...")
        self.bateria -= 15
        print("Batería:", self.bateria)


# --------------------- ROBOT EXPLORADOR → BOTÓN
class RobotExplorador(Robot):
    def __init__(self, nombre):
        super().__init__(nombre)

    def explorar(self):
        if GPIO.input(PIN_BOTON) == GPIO.HIGH:
            print(f"{self.nombre}: Botón PRESIONADO → Explorando...")
            self.bateria -= 15
            print("Batería:", self.bateria)
        else:
            print(f"{self.nombre}: Botón suelto → No explora")


# --------------------- ROBOT MÉDICO → DHT
class RobotMedico(Robot):
    def __init__(self, nombre):
        super().__init__(nombre)

    def leer_dht(self):
        humedad, temperatura = Adafruit_DHT.read_retry(sensorDHT, PIN_DHT)

        if humedad is not None and temperatura is not None:
            print(f"🌡️ Temperatura: {temperatura:.1f}°C  |  💧 Humedad: {humedad:.1f}%")
        else:
            print("Error leyendo DHT — Verifica conexiones")


# ==============================
#  PROGRAMA PRINCIPAL REAL
# ==============================

if __name__ == "__main__":
    try:
        r1 = RobotConstructor("Constructor-1")
        r2 = RobotExplorador("Explorador-1")
        r3 = RobotMedico("Medico-1")

        print("\n===== SISTEMA INICIADO EN RASPBERRY =====\n")

        while True:

            # ---------- Constructor
            r1.encender_led()
            time.sleep(1)
            r1.construir()
            time.sleep(1)
            r1.apagar_led()
            time.sleep(1)

            print("\n---------------------------\n")

            # ---------- Explorador
            r2.explorar()
            time.sleep(1)

            print("\n---------------------------\n")

            # ---------- Médico
            r3.leer_dht()
            time.sleep(2)

            print("\n=============================\n")

    except KeyboardInterrupt:
        print("Programa terminado por el usuario.")
    finally:
        GPIO.cleanup()
        print("GPIO liberados correctamente.")
