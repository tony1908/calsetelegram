from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from flask import Flask
from flask_restful import Api
from flask import request

from spo import obtenerCancion
from wiki import obtenerBiografia

app = Flask(__name__)
api = Api(app)

updater = Updater(token='')
dispatcher = updater.dispatcher




def start(bot, informacion):
	bot.send_message(chat_id=informacion.message.chat_id, text="Holi humanox")

def nombreBot(bot, informacion):
    bot.send_message(chat_id=informacion.message.chat_id, text='Mi nombre es TeleSpotify')
    pass

def echo(bot,informacion):
	print("ECHo")
	bot.send_message(chat_id=informacion.message.chat_id,text=informacion.message.text)

def conArgumentos(bot, informacion, args):
	print(args)
	argumentoLimpio = ' '.join(args).upper()
	bot.send_message(chat_id=informacion.message.chat_id, text=argumentoLimpio)

def cancion(bot, informacion, args):
	argumentoLimpio = ' '.join(args)
	cancion = obtenerCancion(argumentoLimpio)
	bot.send_message(chat_id=informacion.message.chat_id, text=cancion)



comandoArgumento = CommandHandler('nuevo', conArgumentos, pass_args=True)
dispatcher.add_handler(comandoArgumento)

comandoCancion = CommandHandler('cancion', cancion, pass_args=True)
dispatcher.add_handler(comandoCancion)

echoHumano = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echoHumano)



comandoNombre = CommandHandler('name', nombreBot)
dispatcher.add_handler(comandoNombre)

comandoStart = CommandHandler('start',start)
dispatcher.add_handler(comandoStart)


updater.start_polling()


@app.route('/')
def hello_world():
	return "Holi"


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=4567)


