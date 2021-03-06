import threading

from Exception.TimeException import TimeException
from Util.WR_Util import *


class Event:
    """
    Event is an event on a certain date time
    Designed & programmed by Shenran Wang
    fields                              type                                Description
    --------------------------------------------------------------------------------------------------------------------
    event                               (str)                               Event description
    time                                (datetime.datetime)                 Time of the event
    call_back                           (function str, Any -> None)         Callback function for when event occurs
    args                                (Any)                               Args for callback function
    cond                                (threading.Condition)               Condition variable used for count down
    """

    def __init__(self, time: datetime.datetime, event: str, call_back=None, *args):
        """
        Constructor that takes a datetime
        :param time: (datetime.datetime) time of event
        :param event: (str) event description
        :param call_back: (function str, Any -> None) callback function to call on event, default = None
        :param args: (Any) arguments for callback function, default = None
        :return: None
        """
        self.time = time
        self.event = event
        self.call_back = call_back
        self.args = args
        self.cond = threading.Condition()

    @classmethod
    def datetime_event(cls, year: int, month: int, day: int, hour: int, minute: int, event: str, call_back=None, args=None):
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
        return cls(datetime.datetime(year, month, day, hour, minute), event, call_back, args)

    def set_time(self, year, month, day, hour, minute):
        """
        Sets self.time to new time
        Requires: None
        Modifies: self.time
        :param year: (int) year of new time
        :param month: (int) month of new time
        :param day: (int) day of new time
        :param hour: (int) hour of new time
        :param minute: (int) minute of new time
        :return: None
        """
        self.time = datetime.datetime(year, month, day, hour, minute)

    def set_callback(self, call_back, args):
        """
        Sets self.call_back and self.args to new values
        Requires: None
        Modifies: self.call_back, self.args
        :param call_back: (function str, Any -> None) new callback function
        :param args: (Any) arguments for the new callback function
        :return: None
        """
        self.call_back = call_back
        self.args = args

    def start_count_down(self):
        """
        Starts countdown on current thread, on countdown call self.call_back if not None
        Requires: self.event, self.time are not None
        Modifies: None
        :return: None
        :raise: TimeException
        """
        if (datetime.datetime.now() - self.time).total_seconds() <= 0:
            raise TimeException
        with self.cond:
            self.cond.wait_for(check_time(self.time))
            if self.args:
                self.call_back(self.event, self.args)
            else:
                self.call_back(self.event)

    def __lt__(self, other):
        return self.time < other.time

    def __gt__(self, other):
        return self.time > other.time

    def __le__(self, other):
        return self.time <= other.time

    def __ge__(self, other):
        return self.time >= other.time

    def __eq__(self, other):
        return self.event == other.event and self.time == other.time
