from Event import Event


class EventCalendar:
    """
    EventCalendar is a calendar containing all events, past or upcoming
    Designed & programmed by Shenran Wang
    fields                              type                                Description
    --------------------------------------------------------------------------------------------------------------------
    calendar                            (list<Event>)                       List of events in ascending order of time
    """
    def __init__(self):
        self.calendar = []

    def add_event(self, event: Event):
        """
        Adds an event to self.calendar
        Requires: None
        Modifies: self.calendar
        :param event: event to be added to self.calendar
        :return: None
        """
        lo = 0
        hi = len(self.calendar) - 1
        index = 0
        if hi < 0:
            pass
        elif self.calendar[hi] > event > self.calendar[lo]:
            while lo < hi:
                mid = int((lo + hi) / 2)
                mid_event = self.calendar[mid]
                if hi - lo == 1:
                    index = hi
                    break
                elif event == mid_event:
                    index = mid + 1
                    break
                elif event > mid_event:
                    lo = mid
                elif event < mid_event:
                    hi = mid
        elif self.calendar[hi] < event:
            index = hi + 1

        self.calendar.insert(index, event)


    def remove_event(self, event: Event):
        """
        Removes the specifies event from self.calendar if it exists
        :param event: event to be removed
        :return: None
        """
        self.calendar.remove(event)
