from game.opportunity_counter import SimpleOpportunityCounter
from game.hidden_word_generator import HiddenWordWithHints, HiddenWordWithoutHints
from game.letter_replacer import LetterReplacer
from game.letters_register import InMemoryUsedLettersRegister
from game.attempt_validator import ValidAlphabeticCharacter
from presentation import Presentation
from hangman_states import STATE
from controller import HangmanController

OPTIONS = {
    '1': 'Phrase or word with hints',
    '2': 'Phrase or word without hints'
}

OPTIONS_FACTORY = {
    '1': HiddenWordWithHints(),
    '2': HiddenWordWithoutHints(),
}

presentation = Presentation()
used_letters_register = InMemoryUsedLettersRegister()
error_counter = SimpleOpportunityCounter(6)
letter_replacer = LetterReplacer
valid_character = ValidAlphabeticCharacter
hangman_state = STATE

controller = HangmanController(
    presentation,
    error_counter,
    used_letters_register,
    letter_replacer,
    valid_character,
    hangman_state,
    OPTIONS,
    OPTIONS_FACTORY
)

controller.play()