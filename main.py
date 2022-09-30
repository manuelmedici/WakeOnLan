from telegram.ext import *
from telegram import *
from requests import *
from telegram.ext import Updater, CommandHandler, MessageHandler,Filters
from wakeonlan import send_magic_packet
with open("Token.txt", "r" ) as f:
    TOKEN = f.read()
    f.close()
with open("whitelist.txt", "r") as g:
    IDList = [line.strip() for line in g]
    g.close()
updater = Updater(TOKEN, use_context= True)
dispatcher = updater.dispatcher

def start(update, context):
    username = update.message.from_user.username
    buttons = [[KeyboardButton("Pc Manuel")], [KeyboardButton("Pc Dario")]]
    context.bot.send_message(chat_id = update.effective_chat.id, text = f"Ciao {username}! che Pc desideri accendere?", reply_markup= ReplyKeyboardMarkup(buttons))

def reply(update, context):
    testo = update.message.text.lower()
    id = update.message.from_user.id
    str(id)
    print(id)
    if id in IDList:
        if "dario" in testo:
            update.message.reply_text("ok accendo dario...")
        elif "manuel" in testo:
            update.message.reply_text("ok accendo manuel...")
            #send_magic_packet("18.26.49.11.64.a3", interface="xxx.xxx.xxx.xxx")


dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(MessageHandler(Filters.text, reply))
updater.start_polling()