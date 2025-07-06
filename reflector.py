class Reflector:
    def __init__(self, wiring):
        """
        Initialise le réflecteur avec sa configuration de câblage.
        :param wiring: Chaîne représentant la substitution du réflecteur.
        """
        self.wiring = wiring

    def reflect(self, char):
        """
        Transforme la lettre en passant par le réflecteur.
        :param char: Lettre à transformer.
        :return: Lettre après passage dans le réflecteur.
        """
        index = ord(char) - ord('A')
        return self.wiring[index]

    def __str__(self):
        """
        Représentation textuelle pour le débogage.
        """
        return f"Reflector(wiring: {self.wiring})"