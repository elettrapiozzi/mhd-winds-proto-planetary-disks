import os
import numpy as np
import matplotlib.pyplot as plt

# Imposta la cartella di output
output_dir = 'vy_superearth'
os.makedirs(output_dir, exist_ok=True)

# Cartella di input dei file
input_dir = '../outputs_superearth/fargo_multifluid/'

# Definisco la forma che mi aspetto
shape = (128, 384)

# Elenco dei file
frame_files = sorted([f for f in os.listdir(input_dir) if f.startswith("dust3vy") and f.endswith(".dat")])

print(f"Trovati {len(frame_files)} file, inizio il salvataggio...")


for i, frame_file in enumerate(frame_files):
    filepath = os.path.join(input_dir, frame_file)
    
    # Leggere i dati dal file
    data = np.fromfile(filepath, dtype=np.float64)
    
    # Stampo la dimensione dell'array
    print(f"File: {frame_file}, Dimensione dell'array: {len(data)}")
    
    # Verifico se la dimensione dell'array corrisponde alla forma che mi aspetto
    if len(data) == shape[0] * shape[1]:
        # Se la dimensione è corretta, fai il reshape
        data = data.reshape(shape)
        
        # Crea la figura
        plt.imshow(data, origin='lower', cmap='viridis', aspect='auto')
        plt.colorbar(label="Velocità Radiale (vy)")
        plt.xlabel('ϕ [rad]')
        plt.ylabel('r [AU]')

        # Salvo l'immagine come PNG
        frame_filename = f"{output_dir}/frame_{i:03d}.png"
        plt.savefig(frame_filename)
        plt.close()
        print(f"Salvato: {frame_filename}")
    else:
        print(f"Errore con il file {frame_file}: dimensione dell'array non corretta.")

print("Salvataggio completato!")