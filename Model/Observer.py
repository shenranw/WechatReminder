from Observable import Observable


class Observer:
    """
    Observer is an interface. An observer can subscribe to an Observable object and get notified when the Observable
    updates
    Programmed by Shenran Wang
    """

    def update(self, *args) -> None:
        pass

    def subscribe(self, observable: Observable) -> None:
        pass
