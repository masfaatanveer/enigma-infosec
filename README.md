<h1>Saadi_code<h2>
# Projet Enigma

## Description
This project is an emulation of the Enigma machine in Python. It includes encryption and decryption features with customizable rotor configuration and reflector. The interface is available as a command line and with a graphical interface.


## Fonctionnalités
- Encryption and decryption of messages.
- Command line interface and GUI.
- Configuration of rotors and reflector via a JSON file.
- Ability to save and load custom configurations.
- Verbose mode to display encryption/decryption steps.
- Unit tests to verify the validity of encryption and decryption.


## Prérequis
- Python 3.x


## Installation
1. Clone the repo :
   ```bash
   git clone https://github.com/votre-depot/Projet_Enigma.git
2. Make sure all dependencies are installed if necessary.

## Utilisation
### Interface en ligne de commande
1. Exécutez le fichier cli_interface.py :
   ```bash
   python cli_interface.py
   ```
2. Choose whether you want to load the default configuration or a custom configuration.
3. Enter the initial key (ex: "ABC") to set the starting position of the rotors.
4. Select Encrypt or Decrypt mode.
5. Processing a message: Enter a message to encrypt or decrypt.
6. Processing a file: Choose option F to select a text file to encrypt or decrypt. The file will be processed and saved with an _encrypted.txt or _decrypted.txt suffix.
7. Configuration Backup: Choose option S to save the current configuration to config/custom_config.json.

### Interface graphique
1. Excute this commadn gui_interface.py :
   ```bash
   python gui_interface.py
   ```
2. Enter the initial key (ex: "ABC") to set the starting position of the rotors.
3. Choose rotors and reflector from the drop-down menus.
4. Select Encrypt or Decrypt mode.
5. Processing a message: Enter a message in the "Message to process" field and click Process.
6. Processing a file: Click Process File, select a text file, and the file will be processed and saved with an _encrypted.txt or _decrypted.txt suffix.
7. Configuration Backup: Click Save Configuration to save the current configuration to config/custom_config.json.

## Tests unitaires
Run the unit tests to verify that everything is working correctly:
   ```bash
   python -m unittest discover -s tests
   ```


## project stuctre
   ```bash
   Projet_Enigma/
   ├── enigma.py               
   ├── rotor.py               
   ├── reflector.py           
   ├── cli_interface.py        
   ├── gui_interface.py        
   ├── config/
   │   └── config_manager.py
   │   └── custom_config.json 
   │   └── default_config.json 
   │   └── user_config.json
   ├── tests/
   │   ├── test_enigma.py     
   │    └── test_rotor.py       
   └── README.md               # Documentation
   ```

   ```bash
   python3 -m unittest discover -s tests
   ```bash
   python3 cli_interface.py
   ```bash
   python3 gui_interface.py
