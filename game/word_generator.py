import abc

class WordValidator:
    @staticmethod
    def validate(word: str) -> bool:
        for letter in word:
            if not (letter.isalpha() or letter == ' '):  # Allow letters and spaces
                return False
        return True

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