import numpy as np
import matplotlib.pyplot as plt
import os


# --- Percorso dei dati di Fargo3D ---
input_dir = '../massloss_wind/fargo_multifluid'

# --- Parametri della griglia ---
nr = 256
rmin, rmax = 0.4, 2.5

# --- Range di orbite da analizzare ---
start_orbit = 0
end_orbit = 1000
orbit_step = 10

# --- Parametri per il modello TEORICO ---
SIGMA0 = 1e-4
SIGMASLOPE = 0.75
C_EXP = (0.03/8.0) * 0.0025


# --- Preparazione della griglia radiale ---
r_centers = np.linspace(rmin, rmax, nr)
delta_r = (rmax - rmin) / nr
area_anelli = 2 * np.pi * r_centers * delta_r

# --- Calcolo del profilo di densità iniziale teorico ---
initial_sigma_theoretical = SIGMA0 * (r_centers**(-SIGMASLOPE))

# --- Liste per salvare i risultati ---
time_points = []
simulated_mass_points = []
theoretical_mass_points = []

# --- Loop principale su tutte le orbite ---
for orbit in range(start_orbit, end_orbit + 1, orbit_step):
    
    # --- A) Calcolo Massa Simulata ---
    filename = f'gasdens{orbit}.dat'
    filepath = os.path.join(input_dir, filename)
    
    try:
        simulated_sigma = np.fromfile(filepath, dtype=np.float64)
        simulated_mass = np.sum(simulated_sigma * area_anelli)
    except FileNotFoundError:
        print(f"File {filename} non trovato. Interrompo l'analisi.")
        break
        

    current_time = orbit * 2 * np.pi
    
    exponential_term = np.exp(-C_EXP * current_time / r_centers)
    sigma_t_theoretical = initial_sigma_theoretical * exponential_term
    theoretical_mass = np.sum(sigma_t_theoretical * area_anelli)
    
 
    time_points.append(current_time) 
    simulated_mass_points.append(simulated_mass)
    theoretical_mass_points.append(theoretical_mass)

time_array = np.array(time_points)
mass_sim_array = np.array(simulated_mass_points)
mass_th_array = np.array(theoretical_mass_points)


plt.figure(figsize=(8,5))


# Curva 1: Dati dalla simulazione (punti)
plt.plot(time_array, mass_sim_array, color = 'red', linestyle = '-', label='Massa Simulata', linewidth = 3)

# Curva 2: Modello teorico (linea continua)
plt.plot(time_array, mass_th_array, color = 'black', linestyle = '--', label='Massa Attesa', linewidth = 3)

plt.xlabel('Tempo [unità Fargo]', fontsize=14)
plt.ylabel('Massa [unità Fargo]', fontsize=14)
#plt.xlim(0.4,5.0)
#plt.grid(True)
plt.legend(fontsize=14)
#plt.tight_layout()
plt.show()


