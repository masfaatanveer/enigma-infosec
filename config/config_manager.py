import json

def save_configuration(rotors, reflector, filename="config/custom_config.json"):
    """
    Sauvegarde la configuration des rotors et du réflecteur dans un fichier JSON.
    
    :param rotors: Liste d'objets Rotor avec leur câblage et leurs positions de notch.
    :param reflector: Objet Reflector avec son câblage.
    :param filename: Nom du fichier dans lequel enregistrer la configuration (par défaut dans config/custom_config.json).
    """
    config = {
        "rotors": [{"wiring": rotor.wiring, "notch": rotor.notch} for rotor in rotors],
        "reflector": reflector.wiring
    }
    with open(filename, 'w') as file:
        json.dump(config, file, indent=4)
    print(f"Configuration sauvegardée dans {filename}")

def load_configuration(filename="config/default_config.json"):
    """
    Charge la configuration des rotors et du réflecteur depuis un fichier JSON.
    
    :param filename: Nom du fichier de configuration (par défaut config/default_config.json).
    :return: Dictionnaire contenant la configuration des rotors et du réflecteur.
    """
    with open(filename, 'r') as file:
        config = json.load(file)
    print(f"Configuration chargée depuis {filename}")
    return config