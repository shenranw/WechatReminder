from wxpy import *

from EventCalendar import EventCalendar
from Event import Event
from Exception import TimeException
from Observer import Observer
from Observable import Observable
from ChatBot import ChatBot
from Util.WR_Util import *


class RequestHandler(Observer):
    """
    RequestHandler acts as a backend library, and is in charge of handling server requests
    Designed & programmed by Shenran Wang
    fields                                      type                                        Description
    --------------------------------------------------------------------------------------------------------------------
    calendar                                    (EventCalendar)                             Calendar of events
    bot                                         (ChatBot)                                   bot to send notification
    """

    def __init__(self):
        self.calendar = EventCalendar()
        self.bot = ChatBot()
        self.bot.start_session()

    def handle_event_text(self, command: Command, args: str):
        """
        Handles string commands
        Requires: self.calendar and self.bot are not None
        Modifies: self.calendar
        :param command: (Command) command to perform
        :param args: (str) arguments passed, separated with ';'
        :return: None
        """
        args = args.split(";")
        time = datetime.datetime(int(args[0]), int(args[1]), int(args[2]), int(args[3]), int(args[4]))

        if command == Command.NOTIFY:
            self.handle_event_notify(time, self.bot.find_friend(args[5]), args[6])
        elif command == Command.DELETE:
            self.handle_text_event_delete(time, args[5])

    def handle_event(self, msg: Message):
        """
        Handles Message commands
        Requires: self.calendar and self.bot are not None
        Modifies: self.calendar
        :param msg: (Message) message object received
        :return: None
        """
        text = msg.text
        args = text.split(";")
        time = datetime.datetime(args[1], args[2], args[3], args[4], args[5])

        if args[0] == Command.NOTIFY:
            self.handle_event_notify(time, msg.sender, args[6])
        elif args[0] == Command.DELETE:
            self.handle_text_event_delete(time, args[6])

    def handle_event_notify(self, time: datetime.datetime, recipient: Friend, description: str):
        """
        Handles notify event
        Requires: self.calendar and self.bot are not None
        Modifies: self.calendar
        :param time: (datetime.datetime) time to notify
        :param recipient: (wxpy.Friend) friend to notify on event
        :param description: (str) event description
        :return: None
        """
        event = Event(time, description, push_notification, self.bot, recipient)
        self.calendar.add_event(event)
        try:
            event.start_count_down()
        except TimeException:
            print("Unable to start countdown on past event")

    def handle_text_event_delete(self, time: datetime.datetime, description: str):
        """
        Handles delete event
        Requires: self.calendar is not None
        Modifies: self.calendar
        :param time: (datetime.datetime) time of event to delete
        :param description: (str) description of event
        :return: None
        """
        event = Event(time, description)
        self.calendar.remove_event(event)

    def subscribe(self, observable: Observable):
        """
        Subscribes to an Observable object
        Requires: None
        Modifies: None
        :param observable: the observable object to subscribe to
        :return: None
        """
        observable.add_observer(self)

    def unsubscribe(self, observable: Observable):
        """
        Unsubscribes from an Observable object
        Requires: None
        Modifies: None
        :param observable: the observable object to unsubscribe from
        :return: None
        """
        observable.remove_observer(self)

    def update(self, *args):
        """
        Handles observable update
        Requires: None
        Modifies: None
        :param args: arguments passed from observable object
        :return: None
        """
        msg: Message = args[0]
        self.handle_event(msg)
