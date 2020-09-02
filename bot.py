import telebot
import config
import random

from telebot import types

bot=telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start(message):
	#этот метод приветствует пользователя при первом запуске
	sti=open('static/ricardo.webp','rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
	obj1=types.KeyboardButton('да')
	obj2=types.KeyboardButton('нет')

	markup.add(obj1,obj2)

	bot.send_message(message.chat.id,'добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, хотите заказать такси?'.format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)#просто красивый вывод, не обращай внимания



@bot.message_handler(content_types=['text'])
def answer(message):
	#этот метод дублирует отправленные пользователем сообщения
	#bot.send_message(message.chat.id,message.text)
	if message.chat.type == 'private':
		if message.text=="да":
			bot.send_message(message.chat.id,'отлично!\nВ таком случае продолжим')

			markup= types.InlineKeyboardMarkup(row_width=2)

			obj1=types.InlineKeyboardMarkup("yandex")
			obj2=types.InlineKeyboardMarkup("uber")
			obj3=types.InlineKeyboardMarkup("не важно")
			markup.add(obj1,obj2,obj3)

			bot.send_message(message.chat.id,'выберите пожалуйста фирму', reply_markup=markup)

		elif message.text=="нет":
			bot.send_message(message.chat.id,'ну и ладно, вот случайное число - '+(str((random.randint(0,100)))))#всегда указывай чат айди, иначе пошлет хз куда
		else:
			bot.send_message(message.chat.id,'я не знаю что вам ответить(')

#run
bot.polling(none_stop=True)

#ничего не понимаю, но в уроке было так