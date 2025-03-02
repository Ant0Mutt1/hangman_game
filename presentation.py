class Presentation:

    def show_options(self, options):
        print('Choose an option to play:')
        for k, v in options.items():
            print(f"\t{k} - {v}")

    def get_option(self, message):
        option = input(message)
        return option
    
    def show_drawing(self, state, num):
        print(state[num])

    def show_remaining_attempts(self, attempts):
        print(attempts)

    def show_message(self, message):
        print(message)

    def get_letter(self, message):
        letter = input(message)
        return letter