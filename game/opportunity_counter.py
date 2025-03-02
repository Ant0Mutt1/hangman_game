import abc
class AbstractRemainingOpportunitiesCounter(abc.ABC):

    def __init__(self, opportunities: int) -> None:
        self.total = opportunities

    @abc.abstractmethod
    def decrement(self) -> None: ...

    @abc.abstractmethod
    def increment(self) -> None: ...

class SimpleOpportunityCounter(AbstractRemainingOpportunitiesCounter):
    def __init__(self, opportunities: int):
        super().__init__(opportunities)

    def decrement(self) -> None:
        self.total -= 1
        
    def increment(self) -> None:
        pass
