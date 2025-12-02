import telebot

# Token de tu bot
TOKEN = "7989308082:AAFTpd_1LGVQGd2PJ2jX8NEyfWgFPdRTZ_M"
bot = telebot.TeleBot(TOKEN)

# Estado del simulador
estado = "OFF"

@bot.message_handler(commands=['start'])
def start(msg):
    bot.reply_to(msg, "🤖 Simulador ON/OFF listo. Usa:\n/on para encender\n/off para apagar\n/status para ver el estado")

@bot.message_handler(commands=['on'])
def encender(msg):
    global estado
    estado = "ON"
    bot.reply_to(msg, "🔵 El simulador está: ON")

@bot.message_handler(commands=['off'])
def apagar(msg):
    global estado
    estado = "OFF"
    bot.reply_to(msg, "⚫ El simulador está: OFF")

@bot.message_handler(commands=['status'])
def status(msg):
    bot.reply_to(msg, f"📌 Estado actual: {estado}")

print("Bot ON...")
bot.infinity_polling()
