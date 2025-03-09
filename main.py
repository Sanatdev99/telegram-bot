import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from dotenv import load_dotenv
from keyboards import buttons_category
from texnomart_pars import pars_texnomart
from configs import get_value
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = Bot(TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: Message):
    full_name = message.from_user.full_name
    await message.answer(f'Salom {full_name}! Texnomarkga xush kelibsiz')
    await show_category_products(message)


async def show_category_products(message: Message):
    chat_id = message.chat.id
    await bot.send_message(chat_id, 'Kategoriyani tanlang',
                           reply_markup=buttons_category())


# ✅ Properly define button_link function
def button_link(link):
    markup = InlineKeyboardMarkup()
    btn = InlineKeyboardButton(text='Batafsil', url=link)
    return markup


@dp.message_handler()
async def get_prduct_texnomart(message: Message):
    chat_id = message.chat.id
    category_text = message.text

    try:
        category_value = get_value(category_text)
        get_product = pars_texnomart(category_value)

        if not get_product:
            await message.answer("Kechirasiz, bu kategoriya bo'yicha mahsulot topilmadi.")
            return

        for product in get_product:
            images = product.get('images')
            prices = product.get('prices')
            content = product.get('content')
            installment_price = product.get('installment_price')
            link = product.get('link')

            caption = f"""
{content}
Narxi: {prices}
Bo'lib to'lash narxi: {installment_price if installment_price else 'Mavjud emas'}
"""
            await message.answer_photo(photo=images, caption=caption, reply_markup=button_link(link))

    except Exception as e:
        await message.answer("Xatolik yuz berdi, iltimos qaytadan urinib ko'ring.")
        print(f"Error: {e}")


async def main():
    await dp.start_polling()


if __name__ == "__main__":
    asyncio.run(main())
