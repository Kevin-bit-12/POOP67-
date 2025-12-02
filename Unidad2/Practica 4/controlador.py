from modelo import Led
from vista import enviar
from telegram.ext import Updater, CommandHandler

led = Led(18)  # PIN REAL EN PROTO

def start(update, context):
    enviar(update, "Bot encendido.\nComandos:\n/on\n/off")

def on(update, context):
    led.encender()
    enviar(update, "LED encendido 🔆")

def off(update, context):
    led.apagar()
    enviar(update, "LED apagado 💡")

def main():
    updater = Updater("TU_TOKEN_AQUI", use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("on", on))
    dp.add_handler(CommandHandler("off", off))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
