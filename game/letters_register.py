import abc

class AbstractUsedLettersRegister(abc.ABC):
    @abc.abstractmethod
    def __init__(self): ...

    @abc.abstractmethod
    def add_letter(self, letter): ...


class InMemoryUsedLettersRegister(AbstractUsedLettersRegister):

    def __init__(self):
        self.used_letters = set()

    def add_letter(self, letter):
        self.used_letters.add(letter)