from game.hidden_word_generator import HiddenWordWithHints
from game.word_generator import WordFromInput
from game.hangman import Hangman
from utils.screen_cleaner import clear

class HangmanController:
    def __init__(self, presentation, error_counter, used_letters_register, letter_replacer, valid_character, state, options, options_factory):

        self.presentation = presentation
        self.error_counter = error_counter
        self.used_letters_register = used_letters_register
        self.letter_replacer = letter_replacer
        self.valid_character = valid_character
        self.state = state
        self.OPTIONS = options
        self.OPTIONS_FACTORY = options_factory
        self.hangman = None

    def play(self):

        self._initialize_game()
        while not self.hangman.has_won():
            self._show_current_state()
            letter = self._get_valid_letter()
            self._process_letter(letter)
            if self.hangman.has_lost():
                self._show_current_state()

                self.presentation.show_message(f'\nYou lost!\nThe word was {self.hangman.word}')
                break

        if self.hangman.has_won():
            self.presentation.show_message(f'The word is: {self.hangman.word}\nCongratulations! You won.\n')

    def _initialize_game(self):

        self.presentation.show_options(self.OPTIONS)
        option = self.presentation.get_option('>>>\t').strip()
        word = WordFromInput.get('\nEnter a word:\n>> ')
        hidden_word_generator = self.OPTIONS_FACTORY.get(option, HiddenWordWithHints())
        self.hangman = Hangman(
            self.error_counter,
            self.used_letters_register,
            word,
            hidden_word_generator,
            self.letter_replacer,
            self.valid_character
        )
        clear()

    def _show_current_state(self):
        self.presentation.show_message(self.hangman.get_hidden_word())
        num = len(self.state) - 1 - self.hangman.get_remaining_attempts()
        self.presentation.show_drawing(self.state, num)

    def _get_valid_letter(self):

        while True:
            letter = self.presentation.get_letter('\nEnter a letter:\n>> ')
            if self.hangman.validate_entered_character(letter):
                if not self.hangman.check_if_character_already_entered(letter):
                    return letter
                else:
                    self.presentation.show_message('\nThat letter has already been entered.\n')
            else:
                self.presentation.show_message('\nInvalid input.\n')

    def _process_letter(self, letter):

        self.hangman.add_used_letter(letter)
        self.hangman.guess_letter(letter)