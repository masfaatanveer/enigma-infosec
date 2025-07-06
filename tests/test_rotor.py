import unittest
from rotor import Rotor

class TestRotor(unittest.TestCase):
    def setUp(self):
        # Initialize the rotor with a sample wiring and notch at 'Q'
        self.rotor = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", 'Q')

    def test_rotation(self):
        # Test rotor rotation increments the position
        initial_position = self.rotor.position
        self.rotor.rotate()
        self.assertEqual(self.rotor.position, (initial_position + 1) % 26)

    def test_encrypt_forward(self):
        # Test forward encryption from "A" to "E" at initial position
        encrypted = self.rotor.encrypt_forward("A")
        self.assertEqual(encrypted, "E")  # "A" should encrypt to "E" with initial settings

    def test_encrypt_backward(self):
        # Test backward encryption should reverse the forward encryption
        encrypted = self.rotor.encrypt_forward("A")
        decrypted = self.rotor.encrypt_backward(encrypted)
        self.assertEqual(decrypted, "A")  # After encrypting and decrypting, it should return "A"

if __name__ == "__main__":
    unittest.main()
