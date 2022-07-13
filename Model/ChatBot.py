import queue

from Model.Observable import Observable
from wxpy import *


class ChatBot(Observable):
    """
    ChatBot is in charge of sending and receiving messages to one friend in friend list
    Designed & programmed by Shenran Wang
    fields                          Type                            Description
    --------------------------------------------------------------------------------------------------------------------
    bot                             (wxpy.Bot)                      Bot object for chatting
    friend                          (wxpy.Friend)                   Current conversation friend
    """

    def __init__(self, observers=None):
        super().__init__(observers)
        self.bot = None
        self.friend = None

    def start_session(self):
        """
        Starts ChatBot session
        Requires: None
        Modifies: self.bot
        :arg: None
        :return: None
        """
        self.bot = Bot()
        self.subscribe_friend_msg()

    def set_bot(self, bot: Bot):
        """
        Assign bot to self.bot
        Requires: None
        Modifies: self.bot
        :param bot: (wxpy.Bot) the wxpy.Bot object to set self.bot to
        :return: None
        """
        self.bot = bot

    def set_friend(self, friend: Friend):
        """
        Assign friend to self.friend
        Requires: None
        Modifies: self.friend
        :param friend: (wxpy.Friend) the wxpy.friend object to set self.friend to
        :return: None
        """
        self.friend = friend

    def find_friend(self, name: str, sex=None, city=None, province=None):
        """
        Find a friend of self.bot by name, sex and city and assign to self.friend
        Requires: self.bot is not None
        Modifies: self.friend
        :param name: (str) name of friend to find
        :param sex: (wxpy.MALE / wxpy.FEMALE) sex of friend to find, default None
        :param city: (str) city of friend to find, default None
        :param province: (str) province of friend to find, default None
        :return: (Friend) friend found
        """
        return self.bot.friends().search(name, sex=sex, city=city, province=province)[0]

    def send_text(self, msg: str):
        """
        Send text message to self.friend
        Requires: self.bot, self.friend are not None
        Modifies: None
        :param msg: (str) message to send to self.friend
        :return: None
        """
        self.friend.send(msg)

    def send_img(self, img_path: str):
        """
        Send image to self.friend
        Requires: self.bot, self.friend are not None
        Modifies: None
        :param img_path: (str) path to image to be sent
        :return: None
        """
        self.friend.send_image(img_path)

    def subscribe_friend_msg(self):
        """
        Continuously receive message from self.friend and update all observers
        Requires: self.bot, self.friend are not None
        Modifies: self.new_msgs_lsnr_q
        :return: None
        """
        cb = self

        @self.bot.register(Friend, TEXT)
        def receive_friend_msg(msg):
            cb.notify_all(msg)

        embed()
