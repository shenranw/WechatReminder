import datetime
from Model.ChatBot import ChatBot
from wxpy import *


def receive_msg(bot: Bot):
    """
    receive message from bot
    :param bot: (wxpy.Bot) bot to receive message from
    :return: (str) message received
    """
    @bot.register()
    def receive(msg):
        return msg

    m = receive()
    return m


def check_time(time):
    """
    Checks whether now is equal to given time
    :param time: (datetime.datetime) time to check
    :return: (bool) True if now is equal to time, False otherwise
    """
    now = datetime.datetime.now()
    return now == time


def push_notification(notification_title: str, bot: ChatBot):
    """
    Sends notification to bot's current friend
    :param notification_title: (str) notification to send to bot's current friend
    :param bot: (ChatBot) the chat bot to send the notification
    :return: None
    """
    bot.send_text(notification_title)
