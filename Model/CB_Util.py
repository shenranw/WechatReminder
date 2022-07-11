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
