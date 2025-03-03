import abc

class WordValidator:
    @staticmethod
    def validate(word: str) -> bool:
        return all((letter.isalpha() or letter == ' ') for letter in word)

class AbstractWord(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def get(): ...

class WordFromInput(AbstractWord):

    @staticmethod
    def get(message):
        while True:
            word = input(message)
            if not WordValidator.validate(word):
                continue
            break
        return word