from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

kb = ReplyKeyboardMarkup(resize_keyboard=True,
                         one_time_keyboard=True)
kb.add(KeyboardButton('/test'))

total_kb = ReplyKeyboardMarkup(resize_keyboard=True,
                               one_time_keyboard=True)
total_kb.add(KeyboardButton('/total'))

answer_ikb = InlineKeyboardMarkup(row_width=3)
ab1 = InlineKeyboardButton('1',
                           callback_data='1')
ab2 = InlineKeyboardButton('2',
                           callback_data='2')
ab3 = InlineKeyboardButton('3',
                           callback_data='3')
ab4 = InlineKeyboardButton('4',
                           callback_data='4')
answer_ikb.add(ab1, ab2).add(ab3, ab4)

