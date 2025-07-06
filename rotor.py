class Rotor:
    def __init__(self, wiring, notch, position=0, ring_setting=0):
        """
        Initialize a rotor with its wiring, notch, position, and ring setting.
        :param wiring: String representing rotor wiring.
        :param notch: The position that causes the next rotor to advance.
        :param position: Initial rotor position.
        :param ring_setting: Ring setting adjustment for rotor.
        """
        self.wiring = wiring
        self.notch = ord(notch) - ord('A') if isinstance(notch, str) else notch
        self.position = position
        self.ring_setting = ring_setting

    def rotate(self):
        """
        Rotate the rotor by one position.
        :return: True if the rotor reaches the notch position (to trigger next rotor).
        """
        self.position = (self.position + 1) % 26
        return self.position == self.notch

    def encrypt_forward(self, char):
        """
        Encrypt the character in the forward direction through the rotor.
        :param char: Character to encrypt.
        :return: Encrypted character.
        """
        index = (ord(char) - ord('A') + self.position - self.ring_setting) % 26
        encrypted_char = self.wiring[index]
        # print(f"Encrypting Forward: {char} -> {encrypted_char} (index: {index})")  # Optional debug
        return encrypted_char

    def encrypt_backward(self, char):
        """
        Encrypt the character in the backward direction through the rotor.
        :param char: Character to decrypt.
        :return: Decrypted character.
        """
        index = (self.wiring.index(char) - self.position + self.ring_setting) % 26
        decrypted_char = chr(index + ord('A'))
        # print(f"Decrypting Backward: {char} -> {decrypted_char} (index: {index})")  # Optional debug
        return decrypted_char

    def __str__(self):
        return f"Rotor(wiring: {self.wiring}, position: {self.position}, ring_setting: {self.ring_setting})"
