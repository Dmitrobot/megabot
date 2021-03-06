from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='botlog.txt')


def greet_user(bot, update):
    text = 'Ленчик, а пельмени скоро будут?'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = "Привет, {}! Ты написал: '{}'".format(update.message.chat.first_name, update.message.text)
    # print(update.message)
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username,
                 update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)


def main():
    mybot = Updater(settings.TOKEN, request_kwargs=settings.PROXY)

    logging.info('Бот запускается')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()  # начни регулярно холдить на сервер и проверят наличие сообщений
    mybot.idle()  # работать бесконечно, пока не остановят


main()
