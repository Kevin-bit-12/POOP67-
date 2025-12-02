import time
import random

class SensorDHT:
    def __init__(self, nombre):
        self.nombre = nombre
        print("Sensor DHT creado:", self.nombre)

    def leer(self):
        temperatura = 20 + random.randint(0, 10)
        humedad = 40 + random.randint(0, 20)
        print("Lectura de", self.nombre, "-> Temp:", temperatura, "°C  Hum:", humedad, "%")
        return temperatura, humedad

class Robot:
    def __init__(self, nombre):
        self.nombre = nombre
        self.bateria = 100
        print("Robot creado:", self.nombre)

    def saludar(self):
        print("Hola, soy", self.nombre)

    def estado(self):
        print("Robot:", self.nombre, "- Batería:", self.bateria)

class RobotClima(Robot):
    def __init__(self, nombre, sensor):
        super().__init__(nombre)
        self.sensor = sensor

    def revisar_clima(self):
        print(self.nombre, "está revisando el clima...")
        t, h = self.sensor.leer()
        self.bateria = self.bateria - 10
        print("Batería después de leer clima:", self.bateria)

if __name__ == "__main__":
    dht = SensorDHT("DHT-Simulacion-1")
    robot = RobotClima("Robot-Clima-1", dht)

    robot.saludar()
    for i in range(3):
        robot.revisar_clima()
        robot.estado()
        time.sleep(1)
