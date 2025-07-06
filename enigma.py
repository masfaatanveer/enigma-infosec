from rotor import Rotor
from reflector import Reflector

class MachineEnigma:
    def __init__(self, rotors, reflector):
        """
        Initialize the Enigma machine with a list of rotors and a reflector.
        :param rotors: List of rotor objects used in the machine.
        :param reflector: Reflector object used for symmetric substitution.
        """
        self.rotors = rotors
        self.reflector = reflector
        self.initial_positions = None

    def set_rotor_positions(self, positions):
        """
        Set the initial positions of the rotors.
        :param positions: String of letters representing the starting positions (e.g., 'ABC').
        """
        self.initial_positions = positions  # Save the initial state
        for i, position in enumerate(positions):
            self.rotors[i].position = ord(position.upper()) - ord('A')

    def set_ring_settings(self, ring_settings):
        """
        Set the ring settings for the rotors.
        :param ring_settings: List of integers representing each rotor's ring offset.
        """
        for i, ring_setting in enumerate(ring_settings):
            self.rotors[i].ring_setting = ring_setting

    def reset_rotors(self):
        if self.initial_positions:
            self.set_rotor_positions(self.initial_positions)

    def encrypt(self, message, verbose=False, log_file="enigma_verbose.log"):
        """
        Encrypts a message by passing it through rotors (forward), reflector, then rotors (backward).
        :param message: The text to encrypt.
        :param verbose: If True, logs each step of encryption.
        :param log_file: File to write verbose output (default: enigma_verbose.log).
        :return: Encrypted string.
        """
        self.reset_rotors()
        if verbose:
            with open(log_file, 'w') as log:
                log.write("Starting encryption process...\n")

        encrypted_message = ""

        for char in message:
            if verbose:
                with open(log_file, 'a') as log:
                    log.write(f"Original character: {char}\n")

            if not char.isalpha():
                encrypted_message += char
                continue

            original_char = char

            # Rotate rotors before encryption
            if self.rotors[0].rotate():
                if self.rotors[1].rotate():
                    self.rotors[2].rotate()

            # Forward pass through rotors
            for rotor in self.rotors:
                char = rotor.encrypt_forward(char)

            # Reflector
            char = self.reflector.reflect(char)

            # Backward pass through rotors
            for rotor in reversed(self.rotors):
                char = rotor.encrypt_backward(char)

            encrypted_message += char

            if verbose:
                print(f"Original: {original_char}, Encrypted: {char}")

        return encrypted_message

    def decrypt(self, message, verbose=True):
        """
        Decrypts a message. The process is identical to encryption in Enigma.
        :param message: The encrypted text.
        :param verbose: If True, logs each step of decryption.
        :return: Decrypted string.
        """
        return self.encrypt(message, verbose)
