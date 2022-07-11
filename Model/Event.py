import threading
import datetime
from TimeException import TimeException


class Event:
    """
    fields                              type                                Description
    --------------------------------------------------------------------------------------------------------------------
    event                               (str)                               Event description
    time                                (datetime.datetime)                 time of the event
    call_back                           (function str, Any -> None)         callback function for when event occurs
    args                                (Any)                               args for callback function
    """
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, event: str, call_back=None, args=None):
        """
        :param year: (int) year of event
        :param month: (int) month of event
        :param day: (int) day of event
        :param hour: (int) hour of event
        :param minute: (int) minute of event
        :param event: (str) event description
        :param call_back: (function str, Any -> None) callback function to call on event. It must take a str input for
        the first argument, and any input for the rest, default = None
        :param args: (Any) arguments for callback function, default = None
        """
        self.time = datetime.datetime(year, month, day, hour, minute)
        if (datetime.datetime.now() - self.time).total_seconds() <= 0:
            raise TimeException
        self.event = event
        self.call_back = call_back
        self.args = args

    def start_count_down(self):
        """
        Starts countdown on current thread, on countdown call self.call_back if not None
        Requires: self.event, self.time are not None
        Modifies: None
        :return: None
        """
        now = datetime.datetime.now()
        while now != self.time:
            if now == self.time:
                self.call_back(self.event, self.args)
            else:
                continue
        self.call_back(self.event, self.args)
