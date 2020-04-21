import logging 
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
updater = Updater(token='token', use_context=True)
dispatcher = updater.dispatcher
token = '976356887:AAEmSQSSWc97LBSMZsPSytgIr3ExJuQWe4g' #Token of your bot
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
updater.start_polling()

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

