from EventCalendar import EventCalendar
from Event import Event
from Exception import TimeException
from ChatBot import ChatBot
from Util.WR_Util import *


class RequestHandler:
    # TODO: Implement Observer here and subscribe to ChatBot to handle message
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

    def handle_text_event_notify(self, event_description: str):
        """
        Adds notification event to calendar and starts countdown
        Requires: self.calendar is not None
        Modifies: self.calendar
        :param event_description: (str) notification event to be added, in format
        "yyyy;mm;dd;hh;mm;recipient;description;additional args to find recipient"
        :return: (Event) the constructed event object
        :except: TimeException
        """
        event_description = event_description.split(sep=";")
        year = int(event_description[0])
        month = int(event_description[1])
        day = int(event_description[2])
        hour = int(event_description[3])
        minute = int(event_description[4])
        recipient = event_description[5]
        description = event_description[6]
        args = None
        if len(event_description) > 7:
            args = event_description[7]

        self.bot.set_friend(self.bot.find_friend(recipient, args))
        event = Event(year, month, day, hour, minute, description, push_notification, self.bot)
        self.calendar.add_event(event)
        try:
            event.start_count_down()
        except TimeException:
            print("Unable to start countdown on past event")

    def handle_text_event_delete(self, event_description: str):
        """
        Deletes the selected event if it is in calendar
        Requires: self.calendar is not None
        Modifies: self.calendar
        :param event_description: (str) event to be deleted, in format "yyyy;mm;dd;hh;mm;description"
        :return: None
        """
        event_description = event_description.split(sep=";")
        year = int(event_description[0])
        month = int(event_description[1])
        day = int(event_description[2])
        hour = int(event_description[3])
        minute = int(event_description[4])
        description = event_description[5]

        event = Event(year, month, day, hour, minute, description)
        self.calendar.remove_event(event)
