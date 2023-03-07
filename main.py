from aiogram import executor, Bot, types, Dispatcher

from config import TOKEN
from questions import questions, answers, start_text, finish_text
from keyboard import answer_ikb, kb
from questions import result

bot = Bot(TOKEN)
dp = Dispatcher(bot)


total = 0
i = 0


async def on_startup(_):
    print("I've been started up")


async def send_answer(message: types.Message):
    global i
    await bot.send_message(chat_id=message.chat.id,
                           text=f'{questions[i]} \n {"".join(answers[i])}',
                           reply_markup=answer_ikb)
    await message.delete()
    i += 1


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text=start_text,
                           reply_markup=kb)


@dp.message_handler(commands=['test'])
async def test_command(message: types.Message):
    global total
    global i
    i = 0
    total = 0
    await send_answer(message)
    i += 1


@dp.callback_query_handler()
async def answer_callback(callback: types.CallbackQuery):
    global total
    if i == 17:
        await bot.send_message(chat_id=callback.message.chat.id,
                               text=finish_text)
    elif callback.data == '1':
        total += 4
        await send_answer(message=callback.message)
    elif callback.data == '2':
        total += 3
        await send_answer(message=callback.message)
    elif callback.data == '3':
        total += 2
        await send_answer(message=callback.message)
    elif callback.data == '4':
        total += 1
        await send_answer(message=callback.message)


if total <= 34:
    total_text = result[0]
elif total <= 41:
    total_text = result[1]
elif total <= 60:
    total_text = result[2]
else:
    total_text = result[3]


@dp.message_handler(commands=['total'])
async def total_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,
                           text=total_text)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
