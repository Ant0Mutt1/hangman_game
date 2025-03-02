import abc

class AbstractHiddenWord(abc.ABC):

    @abc.abstractmethod
    def hide(self, word): ...

class HiddenWordWithHints(AbstractHiddenWord):
    def hide(self, word):
        hidden_word = ['_' if letter.isalpha() else ' ' for letter in word]
        hidden_word[0] = word[0]
        hidden_word[-1] = word[-1]
        return ''.join(hidden_word)

class HiddenWordWithoutHints(AbstractHiddenWord):
    def hide(self, word):
        print(word)
        return ''.join(['_' if letter.isalpha() else ' ' for letter in word])