from telegram.ext import CommandHandler
from keyboards.main_menu import main_keyboard


''' COMMANDS '''
async def command_start(update, context):
    await update.message.reply_text(
        "Привет, я Финансовый Помощник! Что сегодня сделаем?",
        reply_markup=main_keyboard()
    )


async def command_help(update, context):
    await update.message.reply_text(
        'Вы можете пользоваться Кнопками! Также есть "Помощь" , там сможете найти все что вам нужно! Но если Кнопки не работают, то ниже можете ознакомиться.\n'
        "\n"
        "Баланс - узнайте сколько у вас денег!\n"
        "Продукты - запишу сколько вы потратили на вкусняшки!\n"
        "Транспорт - запишу траты на транспорт!\n"
        "Прочее - запишу траты!\n"
        "Инвестиции - запишу куда вы инвестировали!\n"
        "Статистика - посмотрим все траты!\n"
        "Помощь - расскажу о Командах и Кнопках!\n"
    )

''' REGISTER COMMANDS '''
def register_commands(app):
    app.add_handler(CommandHandler("start", command_start))
    app.add_handler(CommandHandler("help", command_help))