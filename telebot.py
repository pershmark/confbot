import datetime
import logging
import random

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from bot_commands import universal_command, universal_command_test
from get_client import stop_clients, create_bots
from settings import *

TOKEN = '5887785552:AAGBk2Nvam0SYRLZIDQGcWC1hTaOgmaCb5k'


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

clients = []


def start(update, context):
    """Send a message when the command /start is issued."""
    global clients
    if clients:
        stop_clients(clients)
        clients = []
    update.message.reply_text(txt_enter_number_of_bots)


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def exit(update, context):
    """Stop bots"""
    global clients
    if clients:
        stop_clients(clients)
        clients = []
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    global clients
    user_input = update.message.text
    if not clients:
        try:
            number_of_bots = int(user_input)
            if number_of_bots <= 0 or number_of_bots > max_amount_of_bots:
                update.message.reply_text(txt_positive_number)
            else:
                update.message.reply_text(txt_the_process_of_creating_bots)
                clients = create_bots(number_of_bots)
                update.message.reply_text(txt_bots_are_created)
                update.message.reply_text(txt_start_commands)

                # for test
                # clients = str(datetime.datetime.now())

        except ValueError or TypeError:
            update.message.reply_text(txt_positive_number)
    else:
        command = user_input
        if command in available_commands.keys():
            try:
                update.message.reply_text(universal_command(clients, command))

                # for test
                # update.message.reply_text(random.choice(available_commands[command]))
            except Exception as e:
                print(e)
        elif command == 'exit':
            update.message.reply_text(txt_stop_bots_button)
            stop_clients(clients)
            clients = []
        else:
            update.message.reply_text(txt_command_not_found)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("exit", exit))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
