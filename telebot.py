import datetime
import logging
import logging
import os
import time

from dotenv import load_dotenv, find_dotenv
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from bot_commands import universal_command
from get_client import stop_clients, create_bots
from settings import *

load_dotenv(find_dotenv())

TOKEN = os.getenv('TELEGRAM_TOKEN')


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

clients = []
settings = {}
c_type = ''


def start(update, context):
    """Send a message when the command /start is issued."""
    global clients
    global c_type
    if clients:
        stop_clients(clients)
        clients = []
    keyboard = [[txt_command_in_the_chat, txt_timeline]]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text(txt_broadcast_type, reply_markup=reply_markup)


def exit(update, context):
    """Stop bots"""
    global clients
    if clients:
        stop_clients(clients)
        clients = []
    update.message.reply_text(txt_exit)


def echo(update, context):
    global clients
    global c_type
    global settings
    user_input = update.message.text
    if user_input == txt_timeline or user_input == txt_command_in_the_chat:
        if user_input == txt_timeline:
            c_type = 'timeline'
        elif user_input == txt_command_in_the_chat:
            c_type = 'command'
        update.message.reply_text(txt_enter_number_of_bots)
        return
    if not clients:
        try:
            number_of_bots = int(user_input)
            if number_of_bots <= 0 or number_of_bots > settings['general_settings']['max_amount_of_bots']:
                update.message.reply_text(txt_positive_number)
            else:
                update.message.reply_text(txt_the_process_of_creating_bots)
                clients = create_bots(number_of_bots, settings)
                # clients = [True]
                update.message.reply_text(txt_bots_are_created)
                update.message.reply_text(txt_start_commands)
        except ValueError or TypeError:
            update.message.reply_text(txt_positive_number)
    else:
        if c_type == 'command':
            available_commands = get_available_commands(way_to_receive_commands_and_messages)
            command = user_input
            if command in available_commands.keys():
                try:
                    result = universal_command(
                        clients=clients,
                        command=command,
                        settings=settings,
                        available_commands=available_commands
                    )
                    if result:
                        update.message.reply_text(txt_command_completed_successfully)
                    else:
                        update.message.reply_text(txt_command_has_not_been_implemented)
                except Exception as e:
                    with open('log.txt', 'a') as f:  # noqa
                        f.write(f'{datetime.datetime.now()}: {e}\n')
            elif command == 'exit':
                update.message.reply_text(txt_stop_bots_button)
                stop_clients(clients)
                clients = []
            else:
                update.message.reply_text(txt_command_not_found)
        elif c_type == 'timeline':
            settings = get_settings()
            if user_input in settings['timeline'].keys():
                timeline = settings['timeline'][user_input]
                commands = sorted(timeline, key=lambda x: datetime.time.fromisoformat(x['time']))
                for command in commands:
                    command_time = datetime.time.fromisoformat(command['time'])
                    if command_time > datetime.datetime.now().time():
                        while command_time > datetime.datetime.now().time():
                            # update.message.reply_text('waiting...')
                            time.sleep(1)
                        try:
                            result = universal_command(clients=clients, command=command, settings=settings)
                            if result:
                                update.message.reply_text(txt_command_completed_successfully)
                            else:
                                update.message.reply_text(txt_command_has_not_been_implemented)
                        except Exception as e:
                            with open('log.txt', 'a') as f:  # noqa
                                f.write(f'{datetime.datetime.now()}: {e}\n')
            else:
                update.message.reply_text(txt_timeline_not_found)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
    with open('log.txt', 'a') as f:  # noqa
        f.write(f'{datetime.datetime.now()}: {context.error}\n')


def main():
    """Start the bot."""
    global settings
    settings = get_settings()
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("exit", exit))
    dp.add_handler(MessageHandler(Filters.text, echo))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
