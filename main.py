import logging 
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
import random 
import datetime 
from datetime import timedelta


from telegram.ext import Updater
updater = Updater(token='976356887:AAEmSQSSWc97LBSMZsPSytgIr3ExJuQWe4g', use_context=True)
dispatcher = updater.dispatcher
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="i only know how to echo dur !")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
#######################################################################################################
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

from telegram.ext import MessageHandler, Filters
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

def caps(update, context):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)


def nendsudes(update,context):
     if(timedelta.hour==0):
        context.bot.send_photo(chat_id=update.effective_chat.id,photo ='https://i.imgur.com/7G4KARD.jpg',caption='they turned me into a black pickle')

print('starting...')