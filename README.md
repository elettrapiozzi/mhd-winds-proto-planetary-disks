# The Impact of MHD Winds on Dust Morphology in Protoplanetary Disks

**Bachelor Thesis Project in Physics - Università degli Studi di Milano** 
**Author:** Elettra Piozzi  

# About This Project
This repository contains the custom source code, setups, and final report for my Bachelor's thesis. 
The project investigates the impact of forming planets on dust distribution in protoplanetary disks, comparing the standard model of a turbolent disk with a magneto-hydrodynamic (MHD) wind-driven accretion scenario. 

# Custom Modifications to FARGO3D
To run these simulations, I used the open-source hydrodynamical code [FARGO3D](https://github.com/FARGO3D/fargo3d). However, the standard version only accounts for viscous accretion. 
**I custom-modified the C source code to implement the physics of MHD winds.** Key modifications include:
* **`src/update_density_wind.c`**: Added a custom C function called at each timestep to compute the mass loss term. This explicitly updates the gas density field by integrating the wind-driven density decay over the active grid.
* **`src/update_velocity_winds.c`**: Implemented the advection term by directly modifying the azimuthal velocity of the gas. This successfully simulates the negative torque exerted by the MHD winds, removing angular momentum and forcing the gas to accrete inwards.
* **`setups/fargo_multifluid/`**: Extended the parameter files to include the necessary wind parameters: ALPHADW (angular momentum extraction efficiency) and LAMBDA (magnetic lever arm). Additionally, I implemented custom STEADY_STATE boundary conditions to evaluate the analytical steady-state solutions.

# Repository Structure
* `src/`: The modified C source code of FARGO3D.
* `setups/`: Parameter files and initial conditions used for the simulations.
* `report.pdf`: My final thesis document in PDF format (in Italian).

# Main Results
The simulations demonstrated that MHD winds are significantly more efficient than viscous models in forming deep gaps and multiple narrow, dense dust rings, greatly expanding the parameter space capable of reproducing observed disk substructures.

<img width="1420" height="550" alt="dischi_protoplanetari" src="https://github.com/user-attachments/assets/b8e7ccfd-b98a-4a88-a397-f88540f8c704" />
*Figure: 2D maps of the surface density distribution for gas (left) and dust (right) in a wind-driven disk scenario.*

# Original FARGO3D
For general information on how to compile and run the base version of the code, please refer to the official [FARGO3D website and documentation](https://github.com/FARGO3D/fargo3d).

