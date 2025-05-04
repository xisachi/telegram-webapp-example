from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackContext, Updater

TOKEN = '7981812399:AAEdhMdV5pS4dWvHQCG0KdRAbIMhVOpCAEc'
WEBAPP_URL = 'https://xisachi.github.io/telegram-webapp-example/'

def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("Web App'ni ochish", web_app={'url': WEBAPP_URL})]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("Quyidagi tugmani bosing:", reply_markup=reply_markup)

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.start_polling()

