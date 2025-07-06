from enigma import MachineEnigma
from rotor import Rotor
from reflector import Reflector
from config.config_manager import save_configuration, load_configuration

def encrypt_decrypt_file(machine, filename, operation, verbose=False):
    """
    Encrypts or decrypts the contents of a text file and saves the result to a new file.
    
    :param machine: Instance of the configured Enigma machine.
    :param filename: Path to the file to process.
    :param operation: Type of operation ('C' for encrypt, 'D' for decrypt).
    :param verbose: If True, displays each encryption/decryption step.
    """
    with open(filename, 'r') as file:
        text = file.read()
    
    if operation == 'C':
        processed_text = machine.encrypt(text, verbose=verbose)
        output_filename = f"{filename}_encrypted.txt"
    elif operation == 'D':
        processed_text = machine.decrypt(text, verbose=verbose)
        output_filename = f"{filename}_decrypted.txt"
    
    with open(output_filename, 'w') as file:
        file.write(processed_text)
    
    print(f"File processed and saved as: {output_filename}")

def main():
    config_choice = input("Load default configuration (D) or custom configuration (P)? (D/P): ").strip().upper()
    if config_choice == "P":
        config = load_configuration("config/custom_config.json")
    else:
        config = load_configuration("config/default_config.json")

    try:
        # Initialize rotors and reflector
        rotor1 = Rotor(config['rotors']['I']['wiring'], config['rotors']['I']['notch'])
        rotor2 = Rotor(config['rotors']['II']['wiring'], config['rotors']['II']['notch'])
        rotor3 = Rotor(config['rotors']['III']['wiring'], config['rotors']['III']['notch'])

        # Select the reflector
        reflector_key = 'B'  # You can change this to 'C' if needed
        reflector_wiring = config['reflectors'][reflector_key]
        reflector = Reflector(reflector_wiring)

        machine = MachineEnigma([rotor1, rotor2, rotor3], reflector)

        # Ask for initial key
        key = input("Enter initial key (e.g., ABC): ").upper()

        # Set rotor starting positions
        machine.set_rotor_positions(key)

        verbose = input("Enable verbose mode? (Y/N): ").strip().upper() == "Y"

        operation_type = input("Do you want to process a (M)essage or a (F)ile? (M/F): ").strip().upper()
        
        if operation_type == 'M':
            operation = input("Do you want to (E)ncrypt, (D)ecrypt, or (S)ave the configuration? (E/D/S): ").strip().upper()
            if operation == 'E':
                message = input("Enter message to encrypt: ").upper()
                encrypted_message = machine.encrypt(message, verbose=verbose)
                print(f"Encrypted message: {encrypted_message}")
            elif operation == 'D':
                message = input("Enter message to decrypt: ").upper()
                decrypted_message = machine.decrypt(message, verbose=verbose)
                print(f"Decrypted message: {decrypted_message}")
            elif operation == 'S':
                save_configuration([rotor1, rotor2, rotor3], reflector, "config/custom_config.json")
                print("Configuration saved to config/custom_config.json")
            else:
                print("Unrecognized operation.")

        elif operation_type == 'F':
            filename = input("Enter path to the text file: ")
            operation = input("Do you want to (E)ncrypt or (D)ecrypt the file? (E/D): ").strip().upper()
            
            if operation in ['E', 'D']:
                op = 'C' if operation == 'E' else 'D'
                encrypt_decrypt_file(machine, filename, op, verbose=verbose)
            else:
                print("Unrecognized operation.")
                
    except KeyError as e:
        print(f"Configuration error: missing key {e}")
    except TypeError as e:
        print(f"Type error: {e}")

if __name__ == "__main__":
    main()
