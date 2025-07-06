import tkinter as tk
from tkinter import ttk, filedialog
from enigma import MachineEnigma
from rotor import Rotor
from reflector import Reflector
from config.config_manager import save_configuration, load_configuration
import hashlib

# Load configuration for rotor and reflector options
config = load_configuration("config/default_config.json")

def process_message():
    key = key_entry.get().upper()
    message = message_entry.get().upper()
    operation = operation_var.get()

    # Get selected rotors and reflector
    rotor1_choice = rotor1_combo.get()
    rotor2_choice = rotor2_combo.get()
    rotor3_choice = rotor3_combo.get()
    reflector_choice = reflector_combo.get()

    # Initialize rotors and reflector
    rotor1 = Rotor(config['rotors'][rotor1_choice]['wiring'], config['rotors'][rotor1_choice]['notch'])
    rotor2 = Rotor(config['rotors'][rotor2_choice]['wiring'], config['rotors'][rotor2_choice]['notch'])
    rotor3 = Rotor(config['rotors'][rotor3_choice]['wiring'], config['rotors'][rotor3_choice]['notch'])
    reflector = Reflector(config['reflectors'][reflector_choice])

    machine = MachineEnigma([rotor1, rotor2, rotor3], reflector)
    machine.set_rotor_positions(key)

    verbose = verbose_var.get() == 1

    if operation == "Encrypt":
        encrypted_message = machine.encrypt(message, verbose=verbose)
        result_label.config(text=f"Encrypted Message: {encrypted_message}")
    elif operation == "Decrypt":
        decrypted_message = machine.decrypt(message, verbose=verbose)
        result_label.config(text=f"Decrypted Message: {decrypted_message}")

def save_user_configuration():
    rotor1_choice = rotor1_combo.get()
    rotor2_choice = rotor2_combo.get()
    rotor3_choice = rotor3_combo.get()
    reflector_choice = reflector_combo.get()

    rotor1 = Rotor(config['rotors'][rotor1_choice]['wiring'], config['rotors'][rotor1_choice]['notch'])
    rotor2 = Rotor(config['rotors'][rotor2_choice]['wiring'], config['rotors'][rotor2_choice]['notch'])
    rotor3 = Rotor(config['rotors'][rotor3_choice]['wiring'], config['rotors'][rotor3_choice]['notch'])
    reflector = Reflector(config['reflectors'][reflector_choice])

    save_configuration([rotor1, rotor2, rotor3], reflector, "config/custom_config.json")
    result_label.config(text="Configuration saved to config/custom_config.json")

def process_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if not file_path:
        return

    key = key_entry.get().upper()
    operation = operation_var.get()

    rotor1_choice = rotor1_combo.get()
    rotor2_choice = rotor2_combo.get()
    rotor3_choice = rotor3_combo.get()
    reflector_choice = reflector_combo.get()

    rotor1 = Rotor(config['rotors'][rotor1_choice]['wiring'], config['rotors'][rotor1_choice]['notch'])
    rotor2 = Rotor(config['rotors'][rotor2_choice]['wiring'], config['rotors'][rotor2_choice]['notch'])
    rotor3 = Rotor(config['rotors'][rotor3_choice]['wiring'], config['rotors'][rotor3_choice]['notch'])
    reflector = Reflector(config['reflectors'][reflector_choice])

    machine = MachineEnigma([rotor1, rotor2, rotor3], reflector)
    machine.set_rotor_positions(key)

    verbose = verbose_var.get() == 1

    with open(file_path, 'r') as file:
        text = file.read()

    if operation == "Encrypt":
        processed_text = machine.encrypt(text, verbose=verbose)
        output_filename = f"{file_path}_encrypted.txt"
    elif operation == "Decrypt":
        processed_text = machine.decrypt(text, verbose=verbose)
        output_filename = f"{file_path}_decrypted.txt"

    with open(output_filename, 'w') as file:
        file.write(processed_text)

    result_label.config(text=f"File processed and saved as: {output_filename}")

def generate_hashes():
    message = message_entry.get()
    if not message:
        result_label.config(text="Enter a message first.")
        return

    md5_hash = hashlib.md5(message.encode()).hexdigest()
    sha256_hash = hashlib.sha256(message.encode()).hexdigest()

    result = f"MD5: {md5_hash}\nSHA256: {sha256_hash}"
    result_label.config(text=result)

# GUI Setup
window = tk.Tk()
window.title("Enigma Emulator")
window.geometry("800x600")

style = ttk.Style(window)
style.theme_use("default")

# Key input
ttk.Label(window, text="Initial Key (e.g., ABC):").pack(pady=5)
key_entry = ttk.Entry(window, width=10)
key_entry.insert(0, "MAS")
key_entry.pack(pady=5)

# Message input
ttk.Label(window, text="Message to process:").pack(pady=5)
message_entry = ttk.Entry(window, width=50)
message_entry.insert(0, "MASFA")
message_entry.pack(pady=5)

# Rotor selection
ttk.Label(window, text="Select Rotor 1:").pack(pady=5)
rotor1_combo = ttk.Combobox(window, values=list(config['rotors'].keys()))
rotor1_combo.set("I")
rotor1_combo.pack(pady=5)

ttk.Label(window, text="Select Rotor 2:").pack(pady=5)
rotor2_combo = ttk.Combobox(window, values=list(config['rotors'].keys()))
rotor2_combo.set("II")
rotor2_combo.pack(pady=5)

ttk.Label(window, text="Select Rotor 3:").pack(pady=5)
rotor3_combo = ttk.Combobox(window, values=list(config['rotors'].keys()))
rotor3_combo.set("III")
rotor3_combo.pack(pady=5)

ttk.Label(window, text="Select Reflector:").pack(pady=5)
reflector_combo = ttk.Combobox(window, values=list(config['reflectors'].keys()))
reflector_combo.set("B")
reflector_combo.pack(pady=5)

# Operation selection
operation_var = tk.StringVar(value="Encrypt")
operation_frame = ttk.Frame(window)
operation_frame.pack(pady=10)
ttk.Radiobutton(operation_frame, text="Encrypt", variable=operation_var, value="Encrypt").pack(side=tk.LEFT, padx=10)
ttk.Radiobutton(operation_frame, text="Decrypt", variable=operation_var, value="Decrypt").pack(side=tk.LEFT, padx=10)

# Verbose mode
verbose_var = tk.IntVar()
ttk.Checkbutton(window, text="Enable verbose mode", variable=verbose_var).pack(pady=5)

# Buttons
ttk.Button(window, text="Process Message", command=process_message).pack(pady=10)
ttk.Button(window, text="Save Configuration", command=save_user_configuration).pack(pady=5)
ttk.Button(window, text="Process File", command=process_file).pack(pady=5)
ttk.Button(window, text="Generate MD5 + SHA256 Hash", command=generate_hashes).pack(pady=10)

# Output label
result_label = ttk.Label(window, text="Result:", font=("Arial", 12))
result_label.pack(pady=15)

window.mainloop()
