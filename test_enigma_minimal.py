class Rotor:
    def __init__(self, wiring, notch, position=0):
        self.wiring = wiring
        self.notch = ord(notch) - ord('A')
        self.position = position

    def rotate(self):
        # You can modify this method if rotation behavior is required in tests
        return False

    def encrypt_forward(self, char):
        # Calculate the index by shifting based on rotor's current position
        index = (ord(char) - ord('A') + self.position) % 26
        encrypted_char = self.wiring[index]
        # Adjust back by rotor's position
        result = chr((ord(encrypted_char) - ord('A') - self.position + 26) % 26 + ord('A'))
        print(f"encrypt_forward - {char} -> {result}")
        return result

    def encrypt_backward(self, char):
        # Calculate encrypted index in wiring
        shifted_index = (ord(char) - ord('A') + self.position) % 26
        original_index = (self.wiring.index(chr(shifted_index + ord('A'))) - self.position + 26) % 26
        result = chr(original_index + ord('A'))
        print(f"encrypt_backward - {char} -> {result}")
        return result

# Minimal test to verify symmetry of forward and backward encryption
rotor = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q")

for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    encrypted_char = rotor.encrypt_forward(char)
    decrypted_char = rotor.encrypt_backward(encrypted_char)
    assert char == decrypted_char, f"Symmetry error on character: {char}"

print("Symmetry verified for all letters.")
