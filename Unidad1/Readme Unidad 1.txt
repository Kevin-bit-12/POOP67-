Unidad 1 – Fundamentos de GPIO, Funciones y POO en Raspberry Pi

En esta unidad se trabaja con la configuración inicial de la Raspberry Pi, el uso básico del módulo RPi.GPIO y la evolución del código desde control directo, luego con funciones y finalmente con programación orientada a objetos (POO).

Los programas se basan en las prácticas del curso y en el uso de numeración BCM y BOARD, junto con los métodos principales:
GPIO.setup(), GPIO.output(), GPIO.input() y GPIO.cleanup().

Objetivos de la unidad

Comprender la diferencia entre numeración BCM y BOARD.

Encender y apagar un LED desde Python.

Leer el estado de un botón con GPIO.input.

Crear funciones para reutilizar código en LED + botón.

Implementar clases con herencia para controlar dispositivos GPIO.

Separar el programa en módulos (dispositivos.py + main.py).

Familiarizarse con ciclos while True y retardos con time.sleep().

Contenido de la carpeta
Práctica 1 – GPIO Básico

led_bcm.py
Control básico de LED usando numeración BCM.

led_board.py
Mismo funcionamiento pero usando BOARD.

boton_bcm.py
Lectura de botón con BCM; combina botón + LED.

boton_board.py
Versión equivalente usando BOARD.

Práctica 2 – GPIO con Funciones

led_funciones.py
Encender/apagar LED usando funciones.

boton_funciones.py
Lee un botón y activa un LED usando funciones personalizadas.

toggle_led.py
Cada presión del botón alterna el estado del LED.

Práctica 3 – POO con Herencia y Módulos

dispositivos.py
Contiene las clases:

Dispositivo (clase base)

Led (hereda de Dispositivo)

Boton (hereda de Dispositivo)

main.py
Script principal que importa las clases y ejecuta la lógica LED + botón.

uml.png
Diagrama básico de relaciones entre las clases.

Requisitos

Raspberry Pi 3 o 4

Python 3

Librería RPi.GPIO instalada

LED + resistencia 220Ω

Botón + resistencia pull-up/pull-down

Protoboard y cables dupont

Cómo ejecutar

Ejecutar cualquier script con:

python3 nombre_del_archivo.py


Ejemplos:

python3 led_bcm.py
python3 boton_bcm.py
python3 led_funciones.py
python3 main.py