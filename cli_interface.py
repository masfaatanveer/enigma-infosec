from enigma import MachineEnigma
from rotor import Rotor
from reflector import Reflector
from config.config_manager import save_configuration, load_configuration

def encrypt_decrypt_file(machine, filename, operation, verbose=False):
    """
    Chiffre ou déchiffre le contenu d'un fichier texte et sauvegarde le résultat dans un nouveau fichier.
    :param machine: Instance de la machine Enigma configurée.
    :param filename: Chemin du fichier à traiter.
    :param operation: Type d'opération ('C' pour chiffrer, 'D' pour déchiffrer).
    :param verbose: Si True, affiche chaque étape du chiffrement/déchiffrement.
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
    
    print(f"Fichier traité et sauvegardé sous : {output_filename}")

def main():
    config_choice = input("Voulez-vous charger la configuration par défaut (D) ou une configuration personnalisée (P) ? (D/P) : ").strip().upper()
    if config_choice == "P":
        config = load_configuration("config/custom_config.json")
    else:
        config = load_configuration("config/default_config.json")

    # Initialisation des rotors et du réflecteur
    try:
        rotor1 = Rotor(config['rotors']['I']['wiring'], config['rotors']['I']['notch'])
        rotor2 = Rotor(config['rotors']['II']['wiring'], config['rotors']['II']['notch'])
        rotor3 = Rotor(config['rotors']['III']['wiring'], config['rotors']['III']['notch'])

        # Accessing the reflector properly
        reflector_key = 'B'  # You can change this to 'C' if needed
        reflector_wiring = config['reflectors'][reflector_key]  # Access the reflector wiring
        reflector = Reflector(reflector_wiring)

        machine = MachineEnigma([rotor1, rotor2, rotor3], reflector)

        # Demande de la clé de départ
        key = input("Entrez la clé initiale (ex: ABC) : ").upper()

        # Définir la position initiale des rotors
        machine.set_rotor_positions(key)

        verbose = input("Souhaitez-vous activer le mode verbose ? (O/N) : ").strip().upper() == "O"

        operation_type = input("Voulez-vous traiter un (M)essage ou un (F)ichier ? (M/F) : ").strip().upper()
        
        if operation_type == 'M':
            operation = input("Voulez-vous (C)hiprer, (D)échiffrer ou (S)auvegarder la configuration ? (C/D/S) : ").strip().upper()
            if operation == 'C':
                message = input("Entrez le message à chiffrer : ").upper()
                encrypted_message = machine.encrypt(message, verbose=verbose)
                print(f"Message chiffré : {encrypted_message}")
            elif operation == 'D':
                message = input("Entrez le message à déchiffrer : ").upper()
                decrypted_message = machine.decrypt(message, verbose=verbose)
                print(f"Message déchiffré : {decrypted_message}")
            elif operation == 'S':
                save_configuration([rotor1, rotor2, rotor3], reflector, "config/custom_config.json")
                print("Configuration sauvegardée dans config/custom_config.json")
            else:
                print("Opération non reconnue.")

        elif operation_type == 'F':
            filename = input("Entrez le chemin du fichier texte à traiter : ")
            operation = input("Voulez-vous (C)hiprer ou (D)échiffrer le fichier ? (C/D) : ").strip().upper()
            
            if operation in ['C', 'D']:
                encrypt_decrypt_file(machine, filename, operation, verbose=verbose)
            else:
                print("Opération non reconnue.")
                
    except KeyError as e:
        print(f"Erreur de configuration : clé manquante {e}")
    except TypeError as e:
        print(f"Erreur de type : {e}")

if __name__ == "__main__":
    main()
