from game.attempt_validator import AbstractAttemptValidator
from game.hidden_word_generator import AbstractHiddenWord
from game.letter_replacer import AbstractLetterReplacer
from game.letters_register import  AbstractUsedLettersRegister
from game.opportunity_counter import AbstractRemainingOpportunitiesCounter
from game.position_finder import PositionFinder
from game.word_generator import AbstractWord

class Hangman:
    def __init__(
                    self,
                    remaining_attempts: AbstractRemainingOpportunitiesCounter,
                    used_letters_register: AbstractUsedLettersRegister,
                    word: AbstractWord,
                    hidden_word: AbstractHiddenWord,
                    letter_replacer: AbstractLetterReplacer,
                    attempt_validator: AbstractAttemptValidator
                ) -> None:

        self.remaining_attempts = remaining_attempts
        self.used_letters = used_letters_register
        self.word = word
        self.hidden_word = hidden_word.hide(word)
        self.letter_replacer = letter_replacer
        self.attempt_validator = attempt_validator

    def validate_entered_character(self, letter: str) -> bool:
        return self.attempt_validator.validate(letter)

    def check_if_character_already_entered(self, letter) -> bool:
        return letter in self.used_letters.used_letters

    def add_used_letter(self, letter: str) -> None:
        self.used_letters.add_letter(letter)

    def guess_letter(self, letter: str) -> None:
        positions = PositionFinder.get(self.word, letter)

        if positions:
            self.hidden_word = self.letter_replacer.get_word(positions, letter, self.hidden_word)
        else:
            self.remaining_attempts.decrement()

    def get_remaining_attempts(self) -> int:
        return self.remaining_attempts.total

    def get_hidden_word(self) -> str:
        return self.hidden_word

    def has_won(self) -> bool:
        return self.word == self.hidden_word

    def has_lost(self) -> bool:
        return self.remaining_attempts.total == 0