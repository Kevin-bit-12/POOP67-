from modelo import Led, Boton, SensorDHT
from vista import mensaje, info_dht, estado_boton
from telegram.ext import Updater, CommandHandler

led = Led()
boton = Boton()
dht = SensorDHT()


def start(update, context):
    update.message.reply_text("🤖 Raspberry lista.\nComandos: /on /off /boton /dht")


def prender(update, context):
    led.encender()
    update.message.reply_text(mensaje("LED encendido 💡"))


def apagar(update, context):
    led.apagar()
    update.message.reply_text(mensaje("LED apagado 💡"))


def boton_estado(update, context):
    estado = boton.esta_presionado()
    update.message.reply_text(estado_boton(estado))


def leer_dht(update, context):
    h, t = dht.leer()
    if h is None:
        update.message.reply_text("❌ No se pudo leer el DHT")
    else:
        update.message.reply_text(info_dht(t, h))


def crear_bot(token):
    updater = Updater(token)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("on", prender))
    dp.add_handler(CommandHandler("off", apagar))
    dp.add_handler(CommandHandler("boton", boton_estado))
    dp.add_handler(CommandHandler("dht", leer_dht))

    return updater
