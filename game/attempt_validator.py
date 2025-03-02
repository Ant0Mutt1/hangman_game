import abc

class AbstractAttemptValidator(abc.ABC):

    @staticmethod
    @abc.abstractmethod
    def validate(letter: str) -> bool: ...

class ValidAlphabeticCharacter(AbstractAttemptValidator):
    @staticmethod
    def validate(letter: str) -> bool:
        if letter.isalpha() and len(letter) == 1:
            return True
        return False