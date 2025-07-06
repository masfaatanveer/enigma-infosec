from rotor import Rotor
from reflector import Reflector

class MachineEnigma:
    def __init__(self, rotors, reflector):
        """
        Initialise la machine Enigma avec une liste de rotors et un réflecteur.
        :param rotors: Liste de rotors utilisés dans la machine.
        :param reflector: Réflecteur utilisé pour la substitution symétrique.
        """
        self.rotors = rotors
        self.reflector = reflector
        self.initial_positions = None

    def set_rotor_positions(self, positions):
        """
        Définit la position initiale des rotors.
        :param positions: Liste de lettres représentant les positions initiales des rotors.
        """
        self.initial_positions = positions  # Sauvegarde de la position initiale
        for i, position in enumerate(positions):
            self.rotors[i].position = ord(position.upper()) - ord('A')

    def set_ring_settings(self, ring_settings):
        """
        Définit les réglages d'anneaux des rotors.
        :param ring_settings: Liste de valeurs représentant les réglages d'anneaux des rotors.
        """
        for i, ring_setting in enumerate(ring_settings):
            self.rotors[i].ring_setting = ring_setting

    def reset_rotors(self):
        if self.initial_positions:
            self.set_rotor_positions(self.initial_positions)

    def encrypt(self, message, verbose=False, log_file="enigma_verbose.log"):
        """
        Chiffre un message en passant à travers les rotors, réflecteur, puis les rotors inversés.
        :param message: Le texte à chiffrer.
        :param verbose: Si True, affiche chaque étape du chiffrement.
        :return: Texte chiffré.
        """
        self.reset_rotors()
        if verbose:
            with open(log_file, 'w') as log:
                log.write("Début du chiffrement...\n")
        encrypted_message = ""
        for char in message:
            if verbose:
                with open(log_file, 'a') as log:
                    log.write(f"Charactère d'origine: {char}\n")

            if not char.isalpha():
                encrypted_message += char
                continue

            original_char = char

            # Rotation des rotors avant le chiffrement
            if self.rotors[0].rotate():
                if self.rotors[1].rotate():
                    self.rotors[2].rotate()

            # Passer à travers les rotors (avant)
            for rotor in self.rotors:
                char = rotor.encrypt_forward(char)

            # Réflecteur
            char = self.reflector.reflect(char)

            # Passer à travers les rotors (arrière)
            for rotor in reversed(self.rotors):
                char = rotor.encrypt_backward(char)

            encrypted_message += char
            
            if verbose:
                print(f"Original: {original_char}, Encrypted: {char}")
        
        return encrypted_message

    def decrypt(self, message, verbose=True):
        """
        Déchiffre un message. Le processus est identique au chiffrement.
        :param message: Texte chiffré.
        :param verbose: Si True, affiche chaque étape du déchiffrement.
        :return: Texte déchiffré.
        """
        return self.encrypt(message, verbose)