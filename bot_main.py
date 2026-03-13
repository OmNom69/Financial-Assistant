from telegram.ext import Application, CommandHandler, MessageHandler, filters
from telegram import ReplyKeyboardMarkup
from dotenv import load_dotenv
import os
import docs


'''TOKEN'''
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")


'''KEYBOARD AND MESSAGES'''
async def start(update, context):
    buttons = [
        ["ЗАРПЛАТА"],
        ["Еда","Транспорт"],
        ["Покупки", "Инвестиции"],
        ["Статистика"],
        ["Помощь"]
    ]

    keyboard = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    await update.message.reply_text(
        "Привет, я Финансовый Помощник! Что сегодня сделаем?",
        reply_markup=keyboard
    )


async def help(update, context):
    await update.message.reply_text(
        'Вы можете пользоваться Кнопками! Также есть "Помощь" , там сможете найти все что вам нужно! Но если Кнопки не работают, то ниже можете ознакомиться.\n'
        "========================================\n"
        "ЗАРПЛАТА - запомню сколько у вас денег!\n"
        "Еда - запишу сколько вы потратили на вкусняшки!\n"
        "Транспорт - запишу за сколько вы ездили!\n"
        "Покупки - запишу траты!\n"
        "Инвестиции - запишу куда вы инвестировали!\n"
        "Статистика - посмотрим все траты!\n"
        "Помощь - расскажу о Командах и Кнопках!\n"
    )


async def handle_message(update, context):
    text = update.message.text

    if text == "ЗАРПЛАТА":
        await update.message.reply_text("Запомнил сколько у вас денег!")
    elif text == "Еда":
        await update.message.reply_text("Запомнил сколько вы потратили на вкусняшки!")
    elif text == "Транспорт":
        await update.message.reply_text("Запомнил за сколько вы ездили!")
    elif text == "Покупки":
        await update.message.reply_text("Запомнил траты!")
    elif text == "Инвестиции":
        await update.message.reply_text("Запомнил куда вы инвестировали!")
    elif text == "Статистика":
        await update.message.reply_text("Посмотрим все траты!")
    elif text == "Помощь":
        await update.message.reply_text(
            "ПОМОЩЬ\n"
            "========================================="
            "ЗАРПЛАТА - запомню сколько у вас денег!\n"
            "Еда - запишу сколько вы потратили на вкусняшки!\n"
            "Транспорт - запишу за сколько вы ездили!\n"
            "Покупки - запишу траты!\n"
            "Инвестиции - запишу куда вы инвестировали!\n"
            "Статистика - посмотрим все траты!\n"
        )
    else:
        await update.message.reply_text(f"Я не совсем понял вас: {text}| напишите '/help' ")


'''BOT'''
if __name__ == "__main__":
    if not TOKEN:
        print("нет токена")
        exit()


docs.print_docs()  # вывод документации

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("running...")
app.run_polling()
