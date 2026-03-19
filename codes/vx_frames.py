import os
import numpy as np
import matplotlib.pyplot as plt

# Imposta la cartella di output
output_dir = 'vx_superearth_1d'
os.makedirs(output_dir, exist_ok=True)

# Cartella di input dei file
input_dir = '../outputs_superearth/fargo_multifluid/'

# Definisco la forma che mi aspetto
shape = (128, 384)

# Valori radiali (assunti da Rmin a Rmax)
Rmin = 0.4
Rmax = 2.5 
Nr = shape[0]
r_vals = np.linspace(Rmin, Rmax, Nr).reshape(-1,1) # vuol dire fare da 1 a 128

# Leggere velocità angolare del pianeta dalla prima riga di planet0.dat
planet_file = os.path.join(input_dir, 'planet0.dat')
planet_data = np.loadtxt(planet_file)


# Elenco dei file
frame_files = sorted([f for f in os.listdir(input_dir) if f.startswith("dust3vx") and f.endswith(".dat") and "_2d" not in f])

print(f"Trovati {len(frame_files)} file, inizio il salvataggio...")

# Controllo che il numero di file 'gasvx' corrisponda al numero di righe di planet0.dat
if len(frame_files) != planet_data.shape[0]:
    print("Attenzione: il numero di file 'gasvx' non corrisponde al numero di righe in 'planet0.dat!")
    exit ()

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

        # Correzione di vx: trasformo in sistema inerziale
        omega_p = planet_data[i, 5]
        data_inerziale = data + omega_p * r_vals
        
        # Crea la figura 2d
        # plt.imshow(data_inerziale, origin='lower', cmap='viridis', aspect='auto')
        # plt.colorbar(label="Velocità Azimutale (vx)")
        # plt.xlabel('ϕ [rad]')
        # plt.ylabel('r [AU]')

        # Crea la figura 1d
        media_vx = np.mean(data_inerziale, axis=1)
        r_vals_flat = r_vals.flatten() 
        v_kepl = 1 / np.sqrt(r_vals_flat)

        plt.plot(r_vals_flat, media_vx, label='vx medio')
        plt.plot(r_vals_flat, v_kepl, '--', label=r'$1/\sqrt{r}$ (Kepleriano)', color='black')
        plt.xlabel('r [Au]')
        plt.ylabel('vx medio')
        plt.legend()
        plt.grid()

        # Salvo l'immagine come PNG
        frame_filename = f"{output_dir}/vx_2d_{i:03d}.png"
        plt.savefig(frame_filename)
        plt.close()
        print(f"Salvato: {frame_filename}")
    else:
        print(f"Errore con il file {frame_file}: dimensione dell'array non corretta.")

print("Salvataggio completato!")
