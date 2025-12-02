from controlador import crear_bot
import RPi.GPIO as GPIO

TOKEN = "AQUI_TU_TOKEN_DE_TELEGRAM"

if __name__ == "__main__":
    try:
        bot = crear_bot(TOKEN)
        print("🤖 Bot iniciado...")
        bot.start_polling()
        bot.idle()

    except KeyboardInterrupt:
        print("Finalizando...")

    finally:
        GPIO.cleanup()
        print("GPIO liberado correctamente.")
