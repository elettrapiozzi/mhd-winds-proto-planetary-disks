import numpy as np
import matplotlib.pyplot as plt
import os

# === Parametri della simulazione ===
nr, nphi = 256, 512        # griglia (r, phi)
rmin, rmax = 0.4, 5.0      # dominio radiale
frame = 5000               # frame da analizzare

# === Percorsi delle due cartelle ===
dir1 = '../set3_visc/'
dir2 = '../set3_wind/'


# === Costruisci i nomi dei file ===
filename = f'dust1dens{frame}.dat'
file1 = os.path.join(dir1, filename)
file2 = os.path.join(dir2, filename)


# === Asse dei raggi ===
radii = np.linspace(rmin, rmax, nr)

def load_profile(filepath):
    data = np.fromfile(filepath, dtype=np.float64)
    if data.size != nr * nphi:
        raise ValueError(f"File {filepath} ha dimensione inattesa: {data.size}")
    data = data.reshape((nr, nphi))
    return np.mean(data, axis=1)

# === Carica e calcola i profili ===
profile1 = load_profile(file1)
profile2 = load_profile(file2)

# === Plot ===
plt.figure(figsize=(8,5))
plt.plot(radii, profile1, color='black', linestyle='--', label='Disco Viscoso')
plt.plot(radii, profile2, color='purple', linestyle='-', label='Disco Wind Driven')    

plt.xlabel('Raggio [unità Fargo]', fontsize=14)
plt.ylabel('Densità media su φ', fontsize=14)
plt.xlim(0.4,5.0)

#plt.title(f'Disco svasato vs Disco piatto')
#plt.grid(True)
plt.legend(fontsize=14)
#plt.tight_layout()
plt.show()
