from flask import Flask, request, jsonify
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Initialize Flask application
app = Flask(__name__)

# Telegram Bot token
TELEGRAM_TOKEN = '7478446385:AAGo-VeOv2cBttUP3z4ev4ytCD6bUbJ610M'

# Initialize Telegram bot
bot = telegram.Bot(token=TELEGRAM_TOKEN)

# Define a route for Telegram webhook
@app.route(f'/7478446385:AAGo-VeOv2cBttUP3z4ev4ytCD6bUbJ610M', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return 'ok'

# Define a simple command handler
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm your bot.")

# Define a message handler
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# Initialize the dispatcher
dispatcher = Dispatcher(bot, None, workers=0)
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

# Main entry point
if __name__ == '__main__':
    # Set webhook for Telegram
    bot.set_webhook(url=f'https://yourdomain.com/7478446385:AAGo-VeOv2cBttUP3z4ev4ytCD6bUbJ610M')

    # Run Flask app
    app.run(debug=True)
