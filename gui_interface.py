import tkinter as tk
from tkinter import ttk, filedialog
from enigma import MachineEnigma
from rotor import Rotor
from reflector import Reflector
from config.config_manager import save_configuration, load_configuration

# Charger la configuration pour les options de rotors et réflecteurs
config = load_configuration("config/default_config.json")

def chiffrer_message():
    key = key_entry.get().upper()
    message = message_entry.get().upper()
    operation = operation_var.get()

    # Obtenir les choix de rotors et de réflecteur de l'utilisateur
    rotor1_choice = rotor1_combo.get()
    rotor2_choice = rotor2_combo.get()
    rotor3_choice = rotor3_combo.get()
    reflector_choice = reflector_combo.get()

    # Initialiser les rotors et le réflecteur selon les choix de l'utilisateur
    rotor1 = Rotor(config['rotors'][rotor1_choice]['wiring'], config['rotors'][rotor1_choice]['notch'])
    rotor2 = Rotor(config['rotors'][rotor2_choice]['wiring'], config['rotors'][rotor2_choice]['notch'])
    rotor3 = Rotor(config['rotors'][rotor3_choice]['wiring'], config['rotors'][rotor3_choice]['notch'])
    reflector = Reflector(config['reflectors'][reflector_choice])

    machine = MachineEnigma([rotor1, rotor2, rotor3], reflector)
    machine.set_rotor_positions(key)

    verbose = verbose_var.get() == 1

    if operation == "Chiffrer":
        encrypted_message = machine.encrypt(message, verbose=verbose)
        result_label.config(text=f"Message chiffré : {encrypted_message}")
    elif operation == "Déchiffrer":
        decrypted_message = machine.decrypt(message, verbose=verbose)
        result_label.config(text=f"Message déchiffré : {decrypted_message}")

def sauvegarder_configuration():
    # Obtenir les choix de rotors et de réflecteur
    rotor1_choice = rotor1_combo.get()
    rotor2_choice = rotor2_combo.get()
    rotor3_choice = rotor3_combo.get()
    reflector_choice = reflector_combo.get()

    # Initialiser les rotors et le réflecteur selon les choix de l'utilisateur
    rotor1 = Rotor(config['rotors'][rotor1_choice]['wiring'], config['rotors'][rotor1_choice]['notch'])
    rotor2 = Rotor(config['rotors'][rotor2_choice]['wiring'], config['rotors'][rotor2_choice]['notch'])
    rotor3 = Rotor(config['rotors'][rotor3_choice]['wiring'], config['rotors'][rotor3_choice]['notch'])
    reflector = Reflector(config['reflectors'][reflector_choice])

    # Sauvegarder la configuration dans custom_config.json
    save_configuration([rotor1, rotor2, rotor3], reflector, "config/custom_config.json")
    result_label.config(text="Configuration sauvegardée dans config/custom_config.json")

def traiter_fichier():
    """
    Permet de chiffrer ou déchiffrer un fichier texte sélectionné par l'utilisateur.
    """
    # Ouvre une boîte de dialogue pour sélectionner le fichier
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if not file_path:
        return  # Annule si aucun fichier n'est sélectionné

    # Récupère la clé et l'opération
    key = key_entry.get().upper()
    operation = operation_var.get()

    # Obtenir les choix de rotors et de réflecteur
    rotor1_choice = rotor1_combo.get()
    rotor2_choice = rotor2_combo.get()
    rotor3_choice = rotor3_combo.get()
    reflector_choice = reflector_combo.get()

    # Initialiser les rotors et le réflecteur
    rotor1 = Rotor(config['rotors'][rotor1_choice]['wiring'], config['rotors'][rotor1_choice]['notch'])
    rotor2 = Rotor(config['rotors'][rotor2_choice]['wiring'], config['rotors'][rotor2_choice]['notch'])
    rotor3 = Rotor(config['rotors'][rotor3_choice]['wiring'], config['rotors'][rotor3_choice]['notch'])
    reflector = Reflector(config['reflectors'][reflector_choice])

    machine = MachineEnigma([rotor1, rotor2, rotor3], reflector)
    machine.set_rotor_positions(key)

    verbose = verbose_var.get() == 1

    # Chiffrement/Déchiffrement du fichier
    with open(file_path, 'r') as file:
        text = file.read()

    if operation == "Chiffrer":
        processed_text = machine.encrypt(text, verbose=verbose)
        output_filename = f"{file_path}_encrypted.txt"
    elif operation == "Déchiffrer":
        processed_text = machine.decrypt(text, verbose=verbose)
        output_filename = f"{file_path}_decrypted.txt"

    # Sauvegarde du résultat
    with open(output_filename, 'w') as file:
        file.write(processed_text)
    
    result_label.config(text=f"Fichier traité et sauvegardé sous : {output_filename}")

# Interface Tkinter
window = tk.Tk()
window.title("Emulateur Enigma")
window.geometry("600x400")  # Ajuste la taille de la fenêtre

# Utiliser ttk pour les widgets modernes
style = ttk.Style(window)
style.theme_use("default")

# Entrée pour la clé
ttk.Label(window, text="Clé initiale (ex: ABC) :").pack(pady=5)
key_entry = ttk.Entry(window, width=10)
key_entry.pack(pady=5)

# Entrée pour le message
ttk.Label(window, text="Message à traiter :").pack(pady=5)
message_entry = ttk.Entry(window, width=50)
message_entry.pack(pady=5)

# Menus déroulants pour les rotors et le réflecteur
ttk.Label(window, text="Sélectionner le Rotor 1 :").pack(pady=5)
rotor1_combo = ttk.Combobox(window, values=list(config['rotors'].keys()))
rotor1_combo.set("I")  # Valeur par défaut
rotor1_combo.pack(pady=5)

ttk.Label(window, text="Sélectionner le Rotor 2 :").pack(pady=5)
rotor2_combo = ttk.Combobox(window, values=list(config['rotors'].keys()))
rotor2_combo.set("II")  # Valeur par défaut
rotor2_combo.pack(pady=5)

ttk.Label(window, text="Sélectionner le Rotor 3 :").pack(pady=5)
rotor3_combo = ttk.Combobox(window, values=list(config['rotors'].keys()))
rotor3_combo.set("III")  # Valeur par défaut
rotor3_combo.pack(pady=5)

ttk.Label(window, text="Sélectionner le Réflecteur :").pack(pady=5)
reflector_combo = ttk.Combobox(window, values=list(config['reflectors'].keys()))
reflector_combo.set("B")  # Valeur par défaut
reflector_combo.pack(pady=5)

# Options de traitement (Chiffrer ou Déchiffrer)
operation_var = tk.StringVar(value="Chiffrer")
operation_frame = ttk.Frame(window)
operation_frame.pack(pady=10)
ttk.Radiobutton(operation_frame, text="Chiffrer", variable=operation_var, value="Chiffrer").pack(side=tk.LEFT, padx=10)
ttk.Radiobutton(operation_frame, text="Déchiffrer", variable=operation_var, value="Déchiffrer").pack(side=tk.LEFT, padx=10)

# Option pour activer le mode verbose
verbose_var = tk.IntVar()
ttk.Checkbutton(window, text="Activer le mode verbose", variable=verbose_var).pack(pady=5)

# Bouton pour traiter le message
ttk.Button(window, text="Traiter", command=chiffrer_message).pack(pady=15)

# Bouton pour sauvegarder la configuration
ttk.Button(window, text="Sauvegarder Configuration", command=sauvegarder_configuration).pack(pady=5)

# Bouton pour traiter un fichier
ttk.Button(window, text="Traiter un Fichier", command=traiter_fichier).pack(pady=5)

# Label pour afficher le résultat
result_label = ttk.Label(window, text="Message traité :", font=("Arial", 12))
result_label.pack(pady=5)

window.mainloop()