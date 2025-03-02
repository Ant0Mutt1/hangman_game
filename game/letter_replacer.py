import abc

class AbstractLetterReplacer(abc.ABC):

    @staticmethod
    @abc.abstractmethod
    def get_word(positions, letter, hidden_word): ...

class LetterReplacer(AbstractLetterReplacer):

    @staticmethod
    def get_word(positions, letter, hidden_word):
        updated_word = [letter if i in positions else char for i, char in enumerate(hidden_word)]
        return ''.join(updated_word)