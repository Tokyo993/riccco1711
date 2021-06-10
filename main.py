from datetime import datetime
import config
import logging
import calendar
import pyowm

from aiogram import Bot, Dispatcher, executor, types

#Уровень логирования
logging.basicConfig(level=logging.INFO)

owm = OWM('771bf41fd780ca0d32ee26a4a64928c4')

#1854863310:AAH1WVcXDQSgzm48d8qBaRSbYNAVGHn8Vp4
bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def printStart(message: types.Message):
        await message.answer('Привет, я виртуальный асистент Сэм, сейчас я знаю довольно мало команд, кстати с ними ты можешь ознакомиться написав /help. Я учусь новому каждый день, и тебе советую)')

def nowTime():
    this_time = datetime.now().strftime("%H:%M")
    return this_time

def nowDate():
    this_date = datetime.now().date()
    return this_date

def nowCalendar():
    this_m0 = datetime.now().strftime('%m')
    this_m = this_m0.replace('0','')
    return calendar.month(2021,int(this_m))

@dp.message_handler(commands=['time'])
async def printTi(message: types.Message):
        await message.answer('Текущее время: ' + str(nowTime()))

@dp.message_handler(commands=['date'])
async def printDate(message: types.Message):
        await message.answer('Текущая дата: ' + str(nowDate()))

@dp.message_handler(commands=['calendar'])
async def printCalendar(message: types.Message):
        await message.answer('Календарь на месяц\n' + nowCalendar())

@dp.message_handler(commands=['help'])
async def printHelp(message: types.Message):
        await message.answer('Вот все команды которым меня научили:\n /time - команда выведет точное время\n /date - команда выведет сегодняшнюю дату\n /calendar - эта команда выведет календарь на этот месяц')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

