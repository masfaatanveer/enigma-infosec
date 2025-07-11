import unittest
from enigma import MachineEnigma
from rotor import Rotor
from reflector import Reflector

class TestEnigmaMachine(unittest.TestCase):
    def setUp(self):
        rotor1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", 16)
        rotor2 = Rotor("AJDKSIRUXBLHWTMCQGZNPYFVOE", 4)
        rotor3 = Rotor("BDFHJLCPRTXVZNYEIWGAKMUSQO", 21)
        reflector = Reflector("YRUHQSLDPXNGOKMIEBFZCWVJAT")
        self.machine = MachineEnigma([rotor1, rotor2, rotor3], reflector)

    def test_encryption_decryption(self):
        # Verifies that the original message is retrieved after encryption and decryption
        self.machine.set_rotor_positions("ABC")
        message = "HELLO"
        encrypted = self.machine.encrypt(message)
        decrypted = self.machine.decrypt(encrypted)
        self.assertEqual(message, decrypted)

if __name__ == "__main__":
    unittest.main()
