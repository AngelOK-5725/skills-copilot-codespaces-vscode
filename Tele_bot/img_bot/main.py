import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from PIL import Image
import pytesseract

# Укажи путь к tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r"PATH-TO-TESSERACT" 

# Вставь свой Telegram токен
BOT_TOKEN = 'YOUR-API-TOKEN'

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    photo_file = await update.message.photo[-1].get_file()
    file_path = 'temp_image.jpg'
    await photo_file.download_to_drive(file_path)

    try:
        text = pytesseract.image_to_string(Image.open(file_path), lang='eng+rus')
        if text.strip():
            await update.message.reply_text(f'📄 Распознанный текст:\n\n{text}')
        else:
            await update.message.reply_text('❌ Не удалось распознать текст.')
    except Exception as e:
        await update.message.reply_text(f'⚠️ Ошибка при распознавании: {e}')
    finally:
        os.remove(file_path)

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    print("🤖 Бот запущен...")
    app.run_polling()

