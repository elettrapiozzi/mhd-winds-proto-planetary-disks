import numpy as np
import matplotlib.pyplot as plt
import os

# === Parametri della simulazione ===
nr, nphi = 256, 1  # griglia (r, phi)
rmin, rmax = 0.4, 2.5  # dominio radiale

# === Percorso dei dati ===
input_dir = '../avvezione/fargo_multifluid'
frame_numbers = [0, 1000]  

# === Asse dei raggi ===
delta_r = (rmax - rmin) / nr
radii = rmin + (np.arange(nr) + 0.5) * delta_r


# === Plot ===
plt.figure(figsize=(10, 6)) 

for frame in frame_numbers:
    filename = f'gasvy{frame}.dat'
    filepath = os.path.join(input_dir, filename)
    
    # Carica il file
    if not os.path.exists(filepath):
        print(f"ATTENZIONE: File {filename} non trovato.")
        continue
        
    data = np.fromfile(filepath, dtype=np.float64)
    
    if data.size != nr * nphi:
        print(f"File {filename} ha una dimensione inattesa: {data.size}")
        continue

    data = data.reshape((nr, nphi))
    # Prendo solo la prima colonna se nphi > 1, altrimenti è già 1D
    radial_profile_vy = data[:, 0] if nphi > 1 else data.flatten()
    
    # Plot
    plt.plot(radii, radial_profile_vy, label=f'Orbita {frame}')

# profilo analitico V_DW costante

cs0 = np.sqrt(0.0025) 

analytical_vdw = -(3.0/2.0) * 0.01 * 0.05 * cs0 


plt.axhline(analytical_vdw, color='red', linestyle='--', label=f'V_DW analitica (costante) = {analytical_vdw:.2e}')


plt.yscale('linear') 
plt.xlabel('Raggio [unità Fargo]')
plt.ylabel('Velocità Radiale (Vy) [unità Fargo]')
plt.title('Profilo radiale della velocità Vy - Disco coi venti (solo avvezione)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

print("\nVerifica del profilo di velocità completata.")
