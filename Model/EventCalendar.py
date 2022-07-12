from Event import Event


class EventCalendar:
    """
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
        # TODO: perform binary search to find spot to add event

    def remove_event(self, event: Event):
        """
        Removes the specifies event from self.calendar
        :param event: event to be removed
        :return: None
        """
        # TODO: perform binary search to find spot to add event
