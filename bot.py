import telebot
import time

TOKEN = '7553523292:AAE68iKAw5XEjO4rGiR6YbgbJoCscYfR-DM'
CHAT_ID = '1856443989'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "✅ Bot attivo e funzionante!")

def send_signals():
    while True:
        try:
            bot.send_message(CHAT_ID, "📈 Tesla: Compra")
            bot.send_message(CHAT_ID, "📉 Oro: Vendi")
            bot.send_message(CHAT_ID, "📈 Gas Naturale: Compra")
        except Exception as e:
            print(f"Errore: {e}")
        time.sleep(60 * 60 * 3)  # ogni 3 ore

if __name__ == '__main__':
    send_signals()
