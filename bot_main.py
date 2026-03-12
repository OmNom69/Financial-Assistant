from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram import ReplyKeyboardMarkup
from dotenv import load_dotenv
import os


load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")


'''KEYBOARD AND MESSAGES'''
async def start(update, context):
    buttons = [
        ["Еда","Транспорт"],
        ["Сегодня", "Статистика"],
        ["Помощь"]
    ]

    keyboard = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    await update.message.reply_text(
        "Привет, я Финансовый помощник!",
        reply_markup=keyboard
    )


async def help(update, context):
    await update.message.reply_text(
        'Вы можете пользоваться Кнопками! Также есть "Помощь" , там сможете найти все что вам нужно! Но если Кнопки не работают, то ниже можете ознакомиться.\n'
        "========================================\n"
        "Продукты - запишу сколько вы потратили!\n"
        "Транспорт - запишу за сколько вы ездили!\n"
        "Сегодня - посмотрим траты за сегодня!\n"
        "Статистика - посмотрим все траты!\n"
    )


async def handle_message(update, context):
    text = update.message.text

    if text == "Продукты":
        await update.message.reply_text("Запомнил, что вы кушали")
    elif text == "Транспорт":
        await update.message.reply_text("Запомнил, за сколько вы ездили")
    elif text == "Сегодня":
        await update.message.reply_text("Посмотрим что вы покупали сегодня!")
    elif text == "Статистика":
        await update.message.reply_text("Посмотрим что вы покупали за все время!")
    elif text == "Помощь":
        await update.message.reply_text(
            "Продукты - запишу сколько вы потратили\n"
            "Транспорт - запишу за сколько вы ездили\n"
            "Сегодня - посмотрим траты за сегодня\n"
            "Статистика - посмотрим все траты\n"
        )
    else:
        await update.message.reply_text(f"Я не совсем понял вас: {text}| напишите '/help' ")


'''BOT'''
app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("running...")
app.run_polling()
