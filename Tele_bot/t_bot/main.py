import asyncio
import logging
import aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from bs4 import BeautifulSoup
import re

TOKEN = "YOUR-API-TOKEN-FROM-BOTFATHER"  # Вставь сюда токен
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Клавиатура с кнопкой "Отправить ссылку"
start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Отправить ссылку")],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(
        "Привет! Отправь мне ссылку на сайт, и я сделаю краткое содержание страницы.",
        reply_markup=start_kb
    )

async def get_text_summary(text: str, max_sentences=5) -> str:
    sentences = re.split(r'(?<=[.!?])\s+', text)
    summary = ' '.join(sentences[:max_sentences])
    return summary

@dp.message(lambda message: message.text and message.text.startswith("http"))
async def handle_url(message: types.Message):
    url = message.text.strip()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10) as response:
                if response.status != 200:
                    await message.answer("Не удалось загрузить страницу.")
                    return
                html = await response.text()
        soup = BeautifulSoup(html, 'lxml')
        texts = []
        for tag in soup.find_all(['h1','h2','h3','p']):
            t = tag.get_text(strip=True)
            if t:
                texts.append(t)
        full_text = ' '.join(texts)
        summary = await get_text_summary(full_text, max_sentences=10)
        if summary:
            await message.answer(f"📄 Краткое содержание:\n\n{summary}")
        else:
            await message.answer("Не удалось извлечь текст с сайта.")
    except Exception as e:
        await message.answer(f"Ошибка при обработке ссылки:\n{e}")

async def main():
    logging.basicConfig(level=logging.INFO)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

