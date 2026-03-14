from telegram.ext import Application
from dotenv import load_dotenv
import os
from handlers.commands_handler import register_commands
from handlers.messages_handler import register_messages
from documentation import docs


''' TOKEN и запуск бота + дока'''
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")


def main():
    app = Application.builder().token(TOKEN).build()

    register_commands(app)  # все команды чтобы(удобна)
    register_messages(app)  # все команды чтобы(удобна)

    docs.print_docs()
    app.run_polling()
    print("running")


if __name__ == "__main__":
    if not TOKEN:
        print("нет токена")
        exit()
    main()