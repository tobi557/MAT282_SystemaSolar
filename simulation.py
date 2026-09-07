import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, root

# --- Parameters and initial conditions / Parámetros y condiciones iniciales---
G = 1.0 # gravitational constant / constante gravitacional
m1 = 1.0 # mass 1
m2 = 1.0 # mass 2
M = m1 + m2 # Total mass / Masa total

# Start at perihelion on the x-axis / Inicio en el perihelio en el eje x
r0 = np.array([1.0, 0.0]) # Initial position / Position initala
v_kreis = np.sqrt(G * M / np.linalg.norm(r0)) # velocity for a circle / velocidad para un circulo
# For a flatter ellipse, use e.g., 1.35 / Para una elipse más plana, usa p.ej. 1.35
v0 = np.array([0.0, 1.1 * v_kreis])

# --- Calculate orbital prameters / Calcular parámetros orbitales ---
r0_norm = np.linalg.norm(r0)
v0_norm = np.linalg.norm(v0)

E_spec = 0.5 * v0_norm**2 - (G * M) / r0_norm # specific energy / energia especifica
a = - (G * M) / (2.0 * E_spec)
h = r0[0] * v0[1] - r0[0] * v0[0] # momentum / momento
epsilon = np.sqrt(1.0 - (h**2) / (G * M * a))

T_orbit = 2.0 * np.pi * np.sqrt(a**3 / (G * M)) #orbital period / periodo orbital
n = np.sqrt(G * M / a**2) # mean motion / movimiento medio

# --- Calculate analytical solution / calcualr solución analitica ---
# evaluate one full orbit t \in [0,T_orbit]
t_eval = np.linspace(0,T_orbit, 200)
r_analytical = np.zeros((len(t_eval),2))

for i, t in enumerate(t_eval):
    M_anom = n * t # mean anomaly / anomalia media
    
    # define Kepler's equation / definir ecuacíon de Kepler: f(E) = E-e*sin(E)-M(t) = 0
    def kepler_eq(E):
        return E - epsilon *np.sin(E) - M_anom
    # Derivatvie of Kepler's equation for faster Newton's method/
    # Derivida para el método de Newton
    def kepler_prime(E):
        return 1.0 - epsilon * np.cos(E)
    
    # Newton's method (M_anom is a good initial guess) / Método de Newton (M_anom es una buena estimación inicial)
    E_sol = newton(kepler_eq, x0=M_anom, fprime=kepler_prime)
    
    # Calculate de position in the x,y-plane / Calcular posición en el plano x,y
    x = a * (np.cos(E_sol) - epsilon)
    y = a * np.sqrt(1.0 - epsilon**2) * np.sin(E_sol)
    
    r_analytical[i] = [x,y]
    
    
# --- Visualización ---
plt.figure(figsize=(8, 6))
plt.plot(r_analytical[:, 0], r_analytical[:, 1], label="Analytische Lösung", color="black")
plt.plot(0, 0, 'ro', label="Schwerpunkt")
plt.xlabel("x")
plt.ylabel("y")
plt.title(f"Zweikörperproblem - Analytische Bahn (ε = {epsilon:.2f})")
plt.axis("equal")
plt.legend()
plt.grid(True)
plt.show()