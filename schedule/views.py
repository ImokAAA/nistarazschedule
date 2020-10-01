from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from telegram import Bot
from telegram.ext import Dispatcher
from telegram import Update
from telegram import KeyboardButton 
from telegram import ReplyKeyboardMarkup
from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import Filters
from telegram.ext import MessageHandler
from telegram.ext import Updater
from telegram.ext import ConversationHandler
from telegram.ext import CallbackQueryHandler
from telegram.ext import BaseFilter
from telegram.utils.request import Request
from telegram.utils import helpers
from selenium import webdriver
from time import sleep
import json

CALLBACK_BUTTON7a = "callback_button7a"
CALLBACK_BUTTON7b = "callback_button7b"
CALLBACK_BUTTON7c = "callback_button7c"
CALLBACK_BUTTON7d = "callback_button7d"
CALLBACK_BUTTON7e = "callback_button7e"
CALLBACK_BUTTON8a = "callback_button8a"
CALLBACK_BUTTON8b = "callback_button8b"
CALLBACK_BUTTON8c = "callback_button8c"
CALLBACK_BUTTON8d = "callback_button8d"
CALLBACK_BUTTON8e = "callback_button8e"
CALLBACK_BUTTON8f = "callback_button8f"
CALLBACK_BUTTON8g = "callback_button8g"
CALLBACK_BUTTON8h = "callback_button8h"
CALLBACK_BUTTON9a = "callback_button9a"
CALLBACK_BUTTON9b = "callback_button9b"
CALLBACK_BUTTON9c = "callback_button9c"
CALLBACK_BUTTON9d = "callback_button9d"
CALLBACK_BUTTON9e = "callback_button9e"
CALLBACK_BUTTON9f = "callback_button9f"
CALLBACK_BUTTON10a = "callback_button10a"
CALLBACK_BUTTON10b = "callback_button10b"
CALLBACK_BUTTON10c = "callback_button10c"
CALLBACK_BUTTON10d = "callback_button10d"
CALLBACK_BUTTON11a = "callback_button11a"
CALLBACK_BUTTON11b = "callback_button11b"
CALLBACK_BUTTON11c = "callback_button11c"
CALLBACK_BUTTON11d = "callback_button11d"
CALLBACK_BUTTON11e = "callback_button11e"
CALLBACK_BUTTON12a = "callback_button12a"
CALLBACK_BUTTON12b = "callback_button12b"
CALLBACK_BUTTON12c = "callback_button12c"
CALLBACK_BUTTON12d = "callback_button12d"
CALLBACK_BUTTON12e = "callback_button12e"
CALLBACK_BUTTON12f = "CALLBACK_BUTTON12f"

TITLES = {
	CALLBACK_BUTTON7a : "7a",
	CALLBACK_BUTTON7b : "7b",
	CALLBACK_BUTTON7c : "7c",
	CALLBACK_BUTTON7d : "7d",
	CALLBACK_BUTTON7e : "7e",
	CALLBACK_BUTTON8a : "8a",
	CALLBACK_BUTTON8b : "8b",
	CALLBACK_BUTTON8c : "8c",
	CALLBACK_BUTTON8d : "8d",
	CALLBACK_BUTTON8e : "8e",
	CALLBACK_BUTTON8f : "8f",
	CALLBACK_BUTTON8g : "8g",
	CALLBACK_BUTTON8h : "8h",
	CALLBACK_BUTTON9a : "9a",
	CALLBACK_BUTTON9b : "9b",
	CALLBACK_BUTTON9c : "9c",
	CALLBACK_BUTTON9d : "9d",
	CALLBACK_BUTTON9e : "9e",
	CALLBACK_BUTTON9f : "9f",
	CALLBACK_BUTTON10a : "10a",
	CALLBACK_BUTTON10b : "10b",
	CALLBACK_BUTTON10c : "10c",
	CALLBACK_BUTTON10d : "10d",
	CALLBACK_BUTTON11a : "11a",	
	CALLBACK_BUTTON11b : "11b",
	CALLBACK_BUTTON11c : "11c",
	CALLBACK_BUTTON11d : "11d",
	CALLBACK_BUTTON11e : "11e",
	CALLBACK_BUTTON12a : "12a",
	CALLBACK_BUTTON12b : "12b",
	CALLBACK_BUTTON12c : "12c",
	CALLBACK_BUTTON12d : "12d",
	CALLBACK_BUTTON12e : "12e",
	CALLBACK_BUTTON12f : "12f",
	}


def get_keyboard1():
	""" Получить клавиатуру для сообщения
	Эта клавиатура будет видна под каждым сообщением, где её прикрепили
	"""
	# Каждый список внутри `keyboard` -- это один горизонтальный ряд кнопок
	keyboard = [
		# Каждый элемент внутри списка -- это один вертикальный столбец.
		# Сколько кнопок -- столько столбцов
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON7a], callback_data=CALLBACK_BUTTON7a),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON7b], callback_data=CALLBACK_BUTTON7b),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON7c], callback_data=CALLBACK_BUTTON7c),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON7d], callback_data=CALLBACK_BUTTON7d),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON7e], callback_data=CALLBACK_BUTTON7e),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON8a], callback_data=CALLBACK_BUTTON8a),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON8b], callback_data=CALLBACK_BUTTON8b),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON8c], callback_data=CALLBACK_BUTTON8c),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON8d], callback_data=CALLBACK_BUTTON8d),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON8e], callback_data=CALLBACK_BUTTON8e),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON8f], callback_data=CALLBACK_BUTTON8f),
		],

		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON8g], callback_data=CALLBACK_BUTTON8g),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON8h], callback_data=CALLBACK_BUTTON8h),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON9a], callback_data=CALLBACK_BUTTON9a),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON9b], callback_data=CALLBACK_BUTTON9b),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON9c], callback_data=CALLBACK_BUTTON9c),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON9d], callback_data=CALLBACK_BUTTON9d),
		],

		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON9e], callback_data=CALLBACK_BUTTON9e),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON9f], callback_data=CALLBACK_BUTTON9f),
		],

		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON10a], callback_data=CALLBACK_BUTTON10a),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON10b], callback_data=CALLBACK_BUTTON10b),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON10c], callback_data=CALLBACK_BUTTON10c),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON10d], callback_data=CALLBACK_BUTTON10d),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON11a], callback_data=CALLBACK_BUTTON11a),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON11b], callback_data=CALLBACK_BUTTON11b),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON11c], callback_data=CALLBACK_BUTTON11c),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON11d], callback_data=CALLBACK_BUTTON11d),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON11e], callback_data=CALLBACK_BUTTON11e),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON12a], callback_data=CALLBACK_BUTTON12a),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON12b], callback_data=CALLBACK_BUTTON12b),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON12c], callback_data=CALLBACK_BUTTON12c),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON12d], callback_data=CALLBACK_BUTTON12d),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON12e], callback_data=CALLBACK_BUTTON12e),
		],
		[
			InlineKeyboardButton(TITLES[CALLBACK_BUTTON12f], callback_data=CALLBACK_BUTTON12f),
		],

		]
	return InlineKeyboardMarkup(keyboard)


# Create your views here.

bot = Bot(settings.TOKEN)
dispatcher = Dispatcher(bot, None, workers=0, use_context = True)




def web_hook_view(request):
	if request.method == 'POST':
		dispatcher.process_update(Update.de_json(json.loads(request.body), bot))
		return HttpResponse(status=200)
	return HttpResponse('404 not found')



def start(update, callback_context):
	update.message.reply_text(
			text = 'Выбери свой класс и я скину тебе расписание',
			reply_markup = get_keyboard1(),
			)


def callback(update, context):
	number = update.callback_query.data
	context.bot.send_message(chat_id = update.effective_message.chat_id, text = 'Хорошо, подождите 10 секунд')
	if number == 'callback_button7a':
		url = 'https://nistaraz.edupage.org/timetable/view.php?num=104&class=-51'
	if number == 'callback_button7b':
		url = 'https://nistaraz.edupage.org/timetable/view.php?num=104&class=-52'
	if number == 'callback_button7c':
		url = 'https://nistaraz.edupage.org/timetable/view.php?num=104&class=-53' 
	if number == 'callback_button7d':
		url = 'https://nistaraz.edupage.org/timetable/view.php?num=104&class=-54'
	if number == 'callback_button7e':
		url = 'https://nistaraz.edupage.org/timetable/view.php?num=104&class=-55'
	if number == 'callback_button8a':
		url = 'https://nistaraz.edupage.org/timetable/view.php?num=104&class=-56'		
	if number == 'callback_button8b':
		url = 'https://nistaraz.edupage.org/timetable/view.php?num=104&class=-57'
	if number == 'callback_button8c':
		url = 'https://nistaraz.edupage.org/timetable/view.php?num=104&class=-58'
	if number == 'callback_button8d':
		url = 'https://nistaraz.edupage.org/timetable/view.php?num=104&class=-59'
	if number == 'callback_button8e':
		url = 'https://nistaraz.edupage.org/timetable/view.php?num=104&class=-60'
	if number == 'callback_button8f':
		url = 'https://nistaraz.edupage.org/timetable/view.php?num=104&class=-61'
	if number == 'callback_button8g':
		url = 'https://nistaraz.edupage.org/timetable/view.php?num=104&class=-62'
	if number == 'callback_button8h':
		url = 'https://nistaraz.edupage.org/timetable/view.php?num=104&class=-63'
	if number == 'callback_button9a':
		url = 'https://nistaraz.edupage.org/timetable/view.php?num=104&class=-64'
	if number == 'callback_button9b':
		url = 'https://nistaraz.edupage.org/timetable/view.php?num=104&class=-65'
	if number == 'callback_button9c':
		url = 'https://nistaraz.edupage.org/timetable/view.php?num=104&class=-66'
	if number == 'callback_button9d':
		url = 'https://nistaraz.edupage.org/timetable/view.php?num=104&class=-67'
	if number == 'callback_button9e':
		url = 'https://nistaraz.edupage.org/timetable/view.php?num=104&class=-68'
	if number == 'callback_button9f':
		url = 'https://nistaraz.edupage.org/timetable/view.php?num=104&class=-69'
	if number == 'callback_button10a':
		url = 'https://nistaraz.edupage.org/timetable/view.php?num=104&class=-70'
	if number == 'callback_button10b':
		url = 'https://nistaraz.edupage.org/timetable/view.php?num=104&class=-71'
	if number == 'callback_button10c':
		url = 'https://nistaraz.edupage.org/timetable/view.php?num=104&class=-72'
	if number == 'callback_button10d':
		url = 'https://nistaraz.edupage.org/timetable/view.php?num=104&class=-73'
	if number == 'callback_button11a':
		url = 'https://nistaraz.edupage.org/timetable/view.php?num=104&class=-74'
	if number == 'callback_button11b':
		url = 'https://nistaraz.edupage.org/timetable/view.php?num=104&class=-75'
	if number == 'callback_button11c':
		url = 'https://nistaraz.edupage.org/timetable/view.php?num=104&class=-76'
	if number == 'callback_button11d':
		url = 'https://nistaraz.edupage.org/timetable/view.php?num=104&class=-77'
	if number == 'callback_button11e':
		url = 'https://nistaraz.edupage.org/timetable/view.php?num=104&class=-78'
	if number == 'callback_button12a':
		url = 'https://nistaraz.edupage.org/timetable/view.php?num=104&class=-79'
	if number == 'callback_button12b':
		url = 'https://nistaraz.edupage.org/timetable/view.php?num=104&class=-80'
	if number == 'callback_button12c':
		url = 'https://nistaraz.edupage.org/timetable/view.php?num=104&class=-81'
		context.bot.send_message(chat_id = update.effective_message.chat_id, text = 'Имангали бог, Нурик лох')
	if number == 'callback_button12d':
		url = 'https://nistaraz.edupage.org/timetable/view.php?num=104&class=-82'
	if number == 'callback_button12e':
		url = 'https://nistaraz.edupage.org/timetable/view.php?num=104&class=-83'
	if number == 'CALLBACK_BUTTON12f':
		url = 'https://nistaraz.edupage.org/timetable/view.php?num=104&class=-84'

	driver = webdriver.Firefox()
	driver.get(url)
	sleep(5)
	driver.get_screenshot_as_file("screenshot.png")
	driver.quit()
	print("end...")
	context.bot.send_photo(chat_id = update.effective_message.chat_id, photo=open('screenshot.png', 'rb'))
	context.bot.send_message(chat_id = update.effective_message.chat_id, text = 'Нажмите на команду "/start" чтобы заново выбрать класс')

start_handler = CommandHandler('start', start)
callback_handler = CallbackQueryHandler(callback)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(callback_handler)
