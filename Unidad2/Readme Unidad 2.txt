Unidad 2 – MVC, Control con Telegram y Manejo de Archivos en Raspberry Pi

En esta unidad se trabaja con organización avanzada del código mediante arquitectura MVC, control remoto desde Telegram, y registro de datos utilizando clases y archivos. Todo el contenido se basa en la interacción entre Raspberry Pi, sensores y Python.

Objetivos de la unidad

Implementar la arquitectura Modelo–Vista–Controlador.

Controlar LED y botón con estructura ordenada y escalable.

Controlar la Raspberry Pi desde Telegram (LED + sensor DHT11).

Leer temperatura y humedad desde un sensor físico.

Registrar acciones y datos en archivos .txt o .csv usando POO.

Contenido de la carpeta
Práctica 4 – Arquitectura MVC

Carpeta: /mvc_project

Incluye:

modelo/dispositivos.py
Clases Led y Boton, configuradas con GPIO.

vista/consola.py
Función mostrar_estado() para imprimir mensajes.

controlador/main.py
Lógica principal que enciende/apaga el LED y actualiza la vista.

Reto:
Agregar la clase Boton y modificar el controlador para que el LED solo se encienda cuando el botón está presionado.

Práctica 5 – Control de Raspberry Pi con Telegram

Carpeta: /telegram_bot

Incluye:

bot.py
Control del LED y lectura del sensor DHT11 usando Telegram.
Comandos disponibles:

/led_on

/led_off

/status (temperatura y humedad)

Requisitos técnicos:

Bot creado en Telegram vía @BotFather.

Librerías necesarias:

pip install pyTelegramBotAPI Adafruit_DHT


Hardware:

LED en GPIO 18

Sensor DHT11 en GPIO 4

Reto:
Agregar comando /log que muestre historial desde un archivo de texto.

Práctica 6 – Manejo de Archivos con POO

Carpeta: /logger_system

Incluye:

logger.py
Clase Logger que registra acciones en un archivo .txt.

main.py
Integración del logger con LED, botón o sensor (según implementación).

Uso básico:

logger = Logger("log.txt")
logger.escribir("Sistema iniciado")


Reto:
Registrar en el archivo:

Encendido/apagado de LED

Lecturas del sensor DHT11

Eventos del botón

Requisitos

Raspberry Pi con Python 3

Librerías:

RPi.GPIO

pyTelegramBotAPI

Adafruit_DHT

LED + resistencia

Botón

Sensor DHT11

Protoboard y cables

Cómo ejecutar
Práctica 4 (MVC)
python3 mvc_project/controlador/main.py

Práctica 5 (Telegram)
python3 telegram_bot/bot.py

Práctica 6 (logger)
python3 logger_system/main.py