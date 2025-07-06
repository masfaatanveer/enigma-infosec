class Reflector:
    def __init__(self, wiring):
        """
        Initialize the reflector with its wiring configuration.
        :param wiring: A string representing the substitution of the reflector.
        """
        self.wiring = wiring

    def reflect(self, char):
        """
        Reflect the character through the reflector.
        :param char: Character to transform.
        :return: Reflected character.
        """
        index = ord(char) - ord('A')
        return self.wiring[index]

    def __str__(self):
        """
        String representation for debugging.
        """
        return f"Reflector(wiring: {self.wiring})"
