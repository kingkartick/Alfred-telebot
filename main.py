
from logging import error
from typing import Text
import telebot
import re
from telegram import message
from telegram.ext import*
from telegram.ext import updater
from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters



API = "2137716683:AAGTENCXqgWp1Ninxxbm-uATr58Qz__qNrA"
bot = telebot.TeleBot(API,parse_mode=None)

updater = Updater(API,
                  use_context=True)
  
  
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Hello sir, Welcome my Name is Alfred.")
  
def help(update: Update, context: CallbackContext):
    update.message.reply_text("I can do many tricks Like I can teach you coding")


#someresponses
def message_processor(message, response_array ,response):
    #splits the message and punctuations into an array 
    listOfMessage = re.findall(r"[\w']+|[.,!=@#$%^&*:;:'/?.><]",message.lower())
    #scores will decide which message should be posted 
    score = 0 
    for words in listOfMessage:
        if words in response_array:
            score = score + 1
    print(score,response)
    return [score , response]     


def get_response(message):
    response_list = [
        message_processor(message,['hello','hi','hey','is','your'],'Nice to meet you Freind my name is Alfred!'),
        message_processor(message,['bye','good','love','nice'],'It was my pleasure'),
        message_processor(message,['want','to','learn','study','read','help','topic'],'Respected! I can teach you to code watch this video contactme on Insta https://www.instagram.com/reel/cwyqhvihsib/?utm_medium=share_sheet'),
        message_processor(message,['work','buisness','Do','you'],'You can contact My master Kartick Sharma he can do a lot of Data science Machine learning web android '),
        message_processor(message,['number ','contact','follow'],'You can contact My master Kartick SharmaInsta https://www.instagram.com/reel/cwyqhvihsib/?utm_medium=share_sheet'),
        message_processor(message,['how ','are'],'I am nice Thanks for asking'),
        message_processor(message,['fuck','bad','worst','off'],'You Hate me cuzz,I am Beautiful Nigaaaaa'), ]  
    response_scores = []
    for response in response_list:
        response_scores.append(response[0])

    #Get the max value for the best response and  store it into a variable 
    wining_response = max(response_scores)
    matching_response = response_list[response_scores.index(wining_response)]

    if wining_response == 0 :
         bot_response = "I man of simplicity can we come back to topic"
    else:
        bot_response = matching_response[1] 
    print("Bot response:",bot_response)
    return bot_response  

def messageprocessor(update: Update, context: CallbackContext):
    Text = str(update.message.text).lower() 
    responder = get_response(Text)
    update.message.reply_text(responder) 
      





  
  

  
  
updater.dispatcher.add_handler(CommandHandler('start', start))

updater.dispatcher.add_handler(CommandHandler('help', help))


# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text,messageprocessor))
  
updater.start_polling()
updater.idle()

