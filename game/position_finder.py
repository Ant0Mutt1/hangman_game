class PositionFinder:
    @staticmethod
    def get(word, letter):
        return [i for i, _ in enumerate(word) if letter == word[i]]