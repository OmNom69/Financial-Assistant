from telegram import ReplyKeyboardMarkup


''' KEYBOARD MAIN '''
def main_keyboard():
    buttons = [
        ["Баланс"],
        ["Продукты", "Транспорт"],
        ["Прочее", "Инвестиции"],
        ["Статистика"],
        ["Помощь"]
    ]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)