import json

def save_configuration(rotors, reflector, filename="config/custom_config.json"):
    """
    Save the configuration of the rotors and the reflector into a JSON file.
    
    :param rotors: List of Rotor objects with their wiring and notch positions.
    :param reflector: Reflector object with its wiring.
    :param filename: Name of the file where configuration will be saved (default: config/custom_config.json).
    """
    config = {
        "rotors": [{"wiring": rotor.wiring, "notch": rotor.notch} for rotor in rotors],
        "reflector": reflector.wiring
    }
    with open(filename, 'w') as file:
        json.dump(config, file, indent=4)
    print(f"Configuration saved to {filename}")

def load_configuration(filename="config/default_config.json"):
    """
    Load the configuration of rotors and reflector from a JSON file.
    
    :param filename: Name of the configuration file (default: config/default_config.json).
    :return: Dictionary containing the configuration of rotors and reflector.
    """
    with open(filename, 'r') as file:
        config = json.load(file)
    print(f"Configuration loaded from {filename}")
    return config
