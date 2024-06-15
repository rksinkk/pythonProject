from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command, CommandObject
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.fsm.state import StatesGroup, State

import aiogram
import sqlite3
import requests
import asyncio
import logging

kbStandart = [
        [types.KeyboardButton(text="Сделать заказ")],
        [types.KeyboardButton(text="Задать вопрос")],
        [types.KeyboardButton(text="Помощь")]
    ]

kbCancel = [
        [types.KeyboardButton(text="Отмена")]
    ]

keyboardStandart = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kbStandart)

keyboardCancel = types.ReplyKeyboardMarkup(resize_keyboard=True, keyboard=kbCancel)

logging.basicConfig(level=logging.INFO)

helpMessage = "Help"

ADMIN_IDS = [6253591594, 500639411]
GROUP_ID = -4134727319

bot = Bot(token="6450022143:AAGYsWxCt7EOSmGUmWZ0fDKuZjhh7PWkerw")

dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(helpMessage, reply_markup=keyboardStandart)

db = sqlite3.connect("block.db")
cur = db.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS block (id TEXT);")
db.commit()

class OrderForm(StatesGroup):
    order_name = State()
    order_price = State()
    order_description = State()

class QuestionForm(StatesGroup):
    question_name = State()
    question_description = State()

@dp.message(Command("block"))
async def block(message: Message, command: CommandObject):
    if message.from_user.id in ADMIN_IDS:
        if not cur.execute("SELECT * FROM block WHERE id=?", (str(command.args),)).fetchone():
            if command.args is None:
                await message.answer("/block @username")
            else:
                cur.execute("INSERT INTO block (id) VALUES (?)", (str(command.args),))
                db.commit()
                await message.answer(f"{command.args} заблокирован")

@dp.message(Command("unblock"))
async def unblock(message: Message, command: CommandObject):
    if message.from_user.id in ADMIN_IDS:
        if command.args is None:
            await message.answer("/unblock @username")
        else:
            cur.execute("DELETE FROM block WHERE id=?", (str(command.args),))
            db.commit()
            await message.answer(f"{command.args} разблокирован")

@dp.message(Command("say"))
async def say(message: Message, command: CommandObject):
    command_parts = message.text.split(maxsplit=2)
    if len(command_parts) != 3:
        await message.answer("/say id text")
        return
    username = command_parts[1]
    text = command_parts[2]
    try:
        await bot.send_message(int(username), text)
        await message.answer(f"Сообщение успешно отправлено пользователю {username}")
    except aiogram.exceptions.TelegramBadRequest:
        pass

@dp.message(F.text.lower() == "сделать заказ")
async def make_order(message: Message, state: FSMContext):
    if not cur.execute("SELECT * FROM block WHERE id=?", (str(message.from_user.id),)).fetchone():
        await message.reply("Напишите что нужно сделать", reply_markup=keyboardCancel)
        await state.set_state(OrderForm.order_name)

@dp.message(F.text.lower() == "задать вопрос")
async def make_question(message: Message, state: FSMContext):
    if not cur.execute("SELECT * FROM block WHERE id=?", (str(message.from_user.id),)).fetchone():
        await message.reply("Напишите тему вопроса", reply_markup=keyboardCancel)
        await state.set_state(QuestionForm.question_name)

@dp.message(F.text.lower() == "отмена")
async def cansel_question(message: Message):
    await message.reply("Успешно отменено", reply_markup=keyboardStandart)

@dp.message(F.text.lower() == "помощь")
async def show_help(message: Message):
    await message.reply(helpMessage, reply_markup=keyboardStandart)

@dp.message(OrderForm.order_name)
async def order_name_set(message: Message, state: FSMContext):
    await state.update_data(order_name=message.text)
    await message.answer(text="Напишите цену заказа (минимальная - максимальная Валюта; фиксированная Валюта)")
    await state.set_state(OrderForm.order_price)

@dp.message(OrderForm.order_price)
async def order_price_set(message: Message, state: FSMContext):
    await state.update_data(order_price=message.text)
    await message.answer(text="Напишите дополнительные пожелания.")
    await state.set_state(OrderForm.order_description)

@dp.message(OrderForm.order_description)
async def order_description_set(message: Message, state: FSMContext):
    await state.update_data(order_description=message.text)
    data = await state.get_data()
    await message.answer(text="Ваш заказ отправлен на рассмотрение. С Вами свяжутся.", reply_markup=keyboardStandart)
    await bot.send_message(GROUP_ID, f"""Новый заказ. 
User: @{message.from_user.username}
ID: {message.from_user.id}
Название: {data.get("order_name")}
Цена: {data.get("order_price")}
Дополнения к заказу: {data.get("order_description")}""")
    await state.clear()


@dp.message(QuestionForm.question_name)
async def order_name_set(message: Message, state: FSMContext):
    await state.update_data(order_name=message.text)
    await message.answer(text="Напишите ваш вопрос")
    await state.set_state(QuestionForm.question_description)

@dp.message(QuestionForm.question_description)
async def question_description_set(message: Message, state: FSMContext):
    await state.update_data(question_description=message.text)
    data = await state.get_data()
    await message.answer(text="Ваш вопрос отправлен. С Вами свяжутся.", reply_markup=keyboardStandart)
    await bot.send_message(GROUP_ID, f"""Новый вопрос. 
User: @{message.from_user.username}
ID: {message.from_user.id}
Название: {data.get("question_name")}
Текст: {data.get("question_description")}""")
    await state.clear()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())