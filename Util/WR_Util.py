import datetime
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
    :param time: time to check
    :return: (bool) True if now is equal to time, False otherwise
    """
    now = datetime.datetime.now()
    return now == time
