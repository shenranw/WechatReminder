from Observer import Observer


class Observable:
    """
    Observable is an object that updates all its observers when decided
    Programmed by Shenran Wang
    fields                                  type                                    description
    --------------------------------------------------------------------------------------------------------------------
    observers                               (list<Observer>                         subscribed observers
    """

    def __init__(self, observers=None):
        if observers is None:
            self.observers = []
        else:
            self.observers = observers

    def add_observer(self, observer: Observer):
        """
        Adds observer to self.observers list
        Requires: self.observers is not None
        Modifies: self.observers
        :param observer: the observer to be added
        :return: None
        """
        self.observers.append(observer)

    def notify_all(self, *args):
        """
        Notify all observers and pass args
        :param args: arguments to pass to observers
        :return: None
        """
        for o in self.observers:
            o.update(args)

    def remove_observer(self, obserber: Observer):
        """
        Removes the selected observer
        Requires: self.observers is not None
        Modifise: self.observers
        :param obserber: the observer to remove
        :return: None
        """
        self.observers.remove(obserber)
