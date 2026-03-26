from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from handlers.telegram_handlers import message_handler, button_callback

import os
import argparse;
from dotenv import load_dotenv

from handlers.test_handlers.test_handlers import handle_command

def env_path(levels_up=1, filename=".env.bot.secret"):
    path = __file__
    for _ in range(levels_up):
        path = os.path.dirname(path)
    return os.path.join(path, filename)

load_dotenv(env_path())

def main():

    updater = Updater(os.getenv("BOT_TOKEN"))
    dispatcher = updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler))
    dispatcher.add_handler(MessageHandler(Filters.command, message_handler))
    dispatcher.add_handler(CallbackQueryHandler(button_callback))

    updater.start_polling()
    updater.idle()

    parser = argparse.ArgumentParser()
    parser.add_argument("--test", type=str, help="Test a bot command")
    args = parser.parse_args()

    if args.test:
        # Test mode: process the command and exit
        response = handle_command(args.test)
        print(response)
        exit(0)

    # Normal bot startup here (Telegram connection)
    print("Starting bot normally... (Telegram connection)")
    # bot.run() or whatever your Telegram startup is

if __name__ == "__main__":
    main()