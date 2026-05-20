# 1D Steady-State Heat Conduction Solver (with Heat Generation)

## Aim
To solve the 1D steady-state heat conduction equation in a rod with constant thermal conductivity and volumetric heat generation using the Finite Difference Method (FDM).

## Theory
The governing equation for 1D steady-state heat conduction with heat generation is:

$$\frac{d^2T}{dx^2} + \frac{\dot{g}}{k} = 0$$

Where:
- $T$ = Temperature ($^\circ$C)
- $x$ = Axial position (m)
- $\dot{g}$ = Volumetric heat generation (W/m$^3$)
- $k$ = Thermal conductivity (W/mK)

Using a second-order central difference approximation for the spatial derivative:

$$\frac{T_{i-1} - 2T_i + T_{i+1}}{\Delta x^2} + \frac{\dot{g}}{k} = 0 \implies T_{i-1} - 2T_i + T_{i+1} = -\frac{\dot{g} \Delta x^2}{k}$$

This forms a system of linear equations $AT = B$ which is solved directly using direct matrix solvers. Dirichlet boundary conditions are applied at the rod boundaries ($x=0$ and $x=L$).

## File Structure
- `steady_state_conduction_1d.py` - The complete implementation including FDM matrix construction, printing equations, solving, and temperature distribution plotting.
- `output.txt` - Generated logs detailing calculated grid spacing, boundary equations, A/B matrices, and nodal temperatures.
- `Graph.png` - A plot displaying the temperature profile across the rod.

## How to Run
Ensure you have the required dependencies:
```bash
pip install numpy matplotlib
python steady_state_conduction_1d.py
```
