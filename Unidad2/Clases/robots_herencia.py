import time

class Robot:
    def __init__(self, nombre):
        self.nombre = nombre
        self.bateria = 100
        print("Creando robot:", self.nombre)

    def saludar(self):
        print("Hola, soy el robot", self.nombre)

    def mover(self, distancia):
        print(self.nombre, "se mueve", distancia, "pasos")
        self.bateria = self.bateria - 10
        print("Batería:", self.bateria)

    def estado(self):
        print("Robot:", self.nombre, "- Batería:", self.bateria)

class RobotConstructor(Robot):
    def construir(self):
        print(self.nombre, "está construyendo un muro")
        self.bateria = self.bateria - 15
        print("Batería:", self.bateria)

class RobotExplorador(Robot):
    def explorar(self):
        print(self.nombre, "está explorando el terreno")
        self.bateria = self.bateria - 15
        print("Batería:", self.bateria)

class RobotMedico(Robot):
    def curar(self):
        print(self.nombre, "está curando a otro robot")
        self.bateria = self.bateria - 20
        print("Batería:", self.bateria)

if __name__ == "__main__":
    r1 = RobotConstructor("Constructor-1")
    r2 = RobotExplorador("Explorador-1")
    r3 = RobotMedico("Medico-1")

    r1.saludar()
    r1.construir()
    r1.estado()
    time.sleep(1)

    r2.saludar()
    r2.explorar()
    r2.estado()
    time.sleep(1)

    r3.saludar()
    r3.curar()
    r3.estado()
