import telebot
import time
import threading

TOKEN = '8177802068:AAGV1Tcsmcp5sWFoSm8vevEvbjLxaLYsZUU-DM'
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
    # Avvia il thread per inviare i segnali
    signal_thread = threading.Thread(target=send_signals)
    signal_thread.daemon = True
    signal_thread.start()
    
    # Avvia il polling per ascoltare i comandi
    bot.infinity_polling()
