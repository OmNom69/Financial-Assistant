from telegram.ext import MessageHandler, filters
from keyboards.main_menu import main_keyboard


''' MESSAGES '''
async def handler_message(update, context):
    text = update.message.text

    if text == "Баланс":
        await update.message.reply_text("Узнайте сколько у вас денег!")
    elif text == "Продукты":
        await update.message.reply_text("Запомнил сколько вы потратили на вкусняшки!")
    elif text == "Транспорт":
        await update.message.reply_text("Запишу траты на транспорт!")
    elif text == "Прочее":
        await update.message.reply_text("Запишу траты!")
    elif text == "Инвестиции":
        await update.message.reply_text("Запомнил куда вы инвестировали!")
    elif text == "Статистика":
        await update.message.reply_text("Посмотрим все траты!")
    elif text == "Помощь":
        await update.message.reply_text(
            "ПОМОЩЬ\n"
            "\n"
            "Баланс - узнайте сколько у вас денег!\n"
            "Продукты - запомнил сколько вы потратили на вкусняшки!\n"
            "Транспорт - запишу траты на транспорт!\n"
            "Прочее - запишу траты!\n"
            "Инвестиции - запишу куда вы инвестировали!\n"
            "Статистика - посмотрим все траты!\n"
        )

    else:
        await update.message.reply_text(
            f"Я не совсем вас понял: {text}  | напишите /help ",
            reply_markup=main_keyboard()
        )


''' REGISTER MESSAGES '''
def register_messages(app):
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handler_message))