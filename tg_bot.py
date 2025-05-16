from playwright.async_api import async_playwright
from aiogram import Bot , Dispatcher , F
from aiogram.types import Message 
from aiogram.filters import Command
import asyncio
from aiogram.types import FSInputFile
from dotenv import load_dotenv
import os

from tg_bot_kb import get_find , get_skrin

way = "" #Глобальные переменные
screenn = None
Title = ""

load_dotenv() #Загрузка окружения
TOKEN =os.getenv("TELEGRAM_TOKEN")
dp=Dispatcher()
bot=Bot(TOKEN)

@dp.message(Command("start")) #Команда старт
async def cmd_start (message :Message):
    await message.answer ("Бот для отслеживания сайтов" , reply_markup= get_find())

@dp.message(F.text == "Отследить сайт")
async def way_to_find (message : Message):
    await message.answer ("Введите ссылку на сайт")

@dp.message(F.text.startswith("ht")) # Обработка текста-ссылки
async def handle_text_message(message: Message):
    global way
    way = message.text.strip()
    await message.answer("Хотите ли вы сделать скриншот сайта?", reply_markup=get_skrin())

@dp.message(F.text == "Да")
async def screen(message: Message):
    global screenn
    screenn = True
    await message.answer("Запуск сайта...")
    result = await poisk()
    if result:
        await message.answer(f"Заголовок страницы: {result}")
        photo_path = "data/example.png"
        await message.answer_photo(FSInputFile(photo_path))
    else:
        await message.answer("Не удалось открыть сайт.")
    
@dp.message(F.text == "Нет")
async def screen_no (message : Message):
    global screenn
    screenn = False
    await message.answer("Запуск сайта...")
    result = await poisk()
    if result:
        await message.answer(f"Заголовок страницы: {result}")
    else:
        await message.answer("Не удалось открыть сайт.")

async def poisk():
    async with async_playwright() as p:
        global Title, way, screenn
        print("screenn:", screenn)
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        try:
            await page.goto(way, timeout=30000)
            if screenn:
                await page.screenshot(path="data/example.png")
            Title = await page.title()
            return Title
        except Exception as e:  
            return f"Ошибка при открытии сайта: {e}"
        finally:
            await browser.close()

async def main():
    print("Бот запускается...")
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен")