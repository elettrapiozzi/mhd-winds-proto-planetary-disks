import numpy as np
import matplotlib.pyplot as plt
import os

# Dati GW Lup
gwlup_filename = 'GWLup_profile.txt'
gwlup_radius_col = 0
gwlup_luminosity_col = 2

# Dati Simulazione
sim_input_dir = '../wind3_nepur' 
sim_frame_to_plot = 1500              

# Parametri della griglia della simulazione 
sim_nr, sim_nphi = 256, 512
sim_rmin, sim_rmax = 0.4, 5.0 

# Fattore di conversione: 1 unità Fargo = 74 AU 
FARGO_TO_AU_CONVERSION = 74
R_MIN_AU = sim_rmin * FARGO_TO_AU_CONVERSION

try:
    gwlup_data = np.loadtxt(gwlup_filename)
    r_gwlup = gwlup_data[:, gwlup_radius_col]
    val_gwlup = gwlup_data[:, gwlup_luminosity_col]

    # per mettere il raggio minimo di gwlup = raggio minimo fargo
    filter_mask_gwlup = r_gwlup >= R_MIN_AU
    r_gwlup_filtered = r_gwlup[filter_mask_gwlup]
    val_gwlup_filtered = val_gwlup[filter_mask_gwlup]
    
    print(f"Dati GW Lup caricati da: {gwlup_filename}")
except FileNotFoundError:
    print(f"Errore: File GW Lup non trovato. Assicurati che '{gwlup_filename}' sia nel percorso corretto.")
    exit()


r_sim_fargo = np.linspace(sim_rmin, sim_rmax, sim_nr) 
sim_filename = f'dust3dens{sim_frame_to_plot}.dat'
sim_filepath = os.path.join(sim_input_dir, sim_filename)

try:
    sim_raw_data = np.fromfile(sim_filepath, dtype=np.float64)
    if sim_raw_data.size != sim_nr * sim_nphi:
        print(f"File {sim_filename} ha una dimensione inattesa: {sim_raw_data.size}")
        exit()

    sim_reshaped_data = sim_raw_data.reshape((sim_nr, sim_nphi))
    val_sim = np.mean(sim_reshaped_data, axis=1)
    print(f"Dati Simulazione caricati da: {sim_filepath}")
except FileNotFoundError:
    print(f"Errore: File Simulazione non trovato. Assicurati che '{sim_filepath}' sia nel percorso corretto.")
    exit()

# --- Conversione Raggio Simulazione da unità Fargo a AU ---
r_sim_au = r_sim_fargo * FARGO_TO_AU_CONVERSION

# --- Normalizzazione dei Valori sull'asse Y (per confrontare le forme su scala lineare) ---
val_gwlup_normalized = val_gwlup_filtered / np.max(val_gwlup_filtered)
val_sim_normalized = val_sim / np.max(val_sim)

plt.figure(figsize=(12, 7))

# Plot GW Lup
plt.plot(r_gwlup_filtered, val_gwlup_normalized, label='GW Lup (Normalizzato)', color='blue', linewidth=2)

# Plot Simulazione
plt.plot(r_sim_au, val_sim_normalized, label=f'Simulazione (Frame {sim_frame_to_plot}, Normalizzata)', color='orange', linestyle='--', linewidth=2)

# --- Impostazioni del Grafico ---

plt.title('Confronto dei Profili Radiali (Scala Lineare)')
plt.xlabel('Raggio [AU]')
plt.ylabel('Valore Normalizzato (Luminosità / Densità)')
#plt.yscale('log')
plt.grid(True) # Griglia
plt.legend()   # Legenda
#plt.xlim(0, max(np.max(r_gwlup), np.max(r_sim_au))) 
#plt.ylim(0, 1.1) 
plt.xlim(30, 175)
plt.tight_layout() 
plt.show()
