# MAT282 – Simulación del Sistema Solar / Solar System Simulation

**[Español](#español) · [English](#english)**

---

## Español

Proyecto del ramo MAT282 (UTFSM). Simulamos el problema de N cuerpos gravitacional: primero el problema de dos cuerpos Tierra–Sol, comparando métodos numéricos contra la solución analítica de Kepler, y después el sistema solar completo (Sol + 8 planetas) con Störmer–Verlet, usando condiciones iniciales de JPL Horizons.

### Contenido del repositorio

```
main_N_Cuerpos.ipynb   Notebook principal con todo el código
resultados/            Gráficos y tablas obtenidos con el notebook
environment.yml        Entorno de conda con las librerías necesarias
```

### Métodos implementados

- Euler explícito
- Euler implícito (con `scipy.optimize.root`)
- Euler simpléctico
- Störmer–Verlet
- Solución analítica de Kepler (ecuación de Kepler resuelta con Newton–Raphson vectorizado)

### Cómo usarlo

**Opción 1: Google Colab (la más simple)**
1. Abre `main_N_Cuerpos.ipynb` en [Google Colab](https://colab.research.google.com/) (Archivo → Subir notebook, o desde GitHub).
2. Ejecuta las celdas de arriba hacia abajo.

**Opción 2: en tu computador**
```bash
git clone https://github.com/tobi557/MAT282_SystemaSolar.git
cd MAT282_SystemaSolar
conda env create -f environment.yml
conda activate orbit
jupyter notebook main_N_Cuerpos.ipynb
```
Si después se agregan librerías al entorno: `conda env update --file environment.yml --prune`.

### Orden de ejecución

El notebook está dividido en secciones. La mayoría de las celdas son independientes, salvo estas:

- **Verificación del Euler implícito:** necesita haber corrido antes la celda *SIMULACIÓN CON 40 ÓRBITAS + STÖRMER-VERLET* y la celda de `solve_implicit_step_2d`.
- **Log error del sistema solar** y **Error contra JPL Horizons:** necesitan haber corrido antes la celda *SIMULACIÓN DEL SISTEMA SOLAR CON STÖRMER-VERLET*.
- **Error contra JPL Horizons:** descarga datos desde la API de Horizons, así que necesita internet.

Las simulaciones con muchas órbitas (sobre todo por el Euler implícito) pueden tardar algunos minutos.

### Carpeta `resultados/`

| Carpeta | Qué contiene |
|---|---|
| `01_dos_cuerpos_20_orbitas` … `04_dos_cuerpos_50_orbitas` | Dos cuerpos con 20, 30, 40 y 50 órbitas: órbitas, cada método vs la analítica, error vs tiempo, colapso del semieje mayor del Euler implícito y tabla de error por órbita |
| `05_verlet_20_orbitas`, `06_verlet_40_orbitas` | Lo mismo, agregando Störmer–Verlet |
| `07_euler_implicito` | Tiempos de `scipy.optimize.root` vs Newton propio, y verificación de que el paso implícito se queda sin solución |
| `08_sistema_solar` | Órbitas del sistema solar, error relativo de energía, log error, log-log y error de posición contra JPL Horizons |

### Datos

Condiciones iniciales de [JPL Horizons](https://ssd.jpl.nasa.gov/horizons/) (efemérides DE441): vectores de estado en el plano de la eclíptica, en AU y AU/día, para la época 2026-09-09 00:00 TDB.

---

## English

Project for the MAT282 course (UTFSM). We simulate the gravitational N-body problem: first the Earth–Sun two-body problem, comparing numerical methods against Kepler's analytical solution, and then the full solar system (Sun + 8 planets) with Störmer–Verlet, using initial conditions from JPL Horizons.

### Repository contents

```
main_N_Cuerpos.ipynb   Main notebook with all the code
resultados/            Plots and tables produced by the notebook
environment.yml        Conda environment with the required libraries
```

### Implemented methods

- Explicit Euler
- Implicit Euler (using `scipy.optimize.root`)
- Symplectic Euler
- Störmer–Verlet
- Kepler's analytical solution (Kepler's equation solved with vectorized Newton–Raphson)

### How to use it

**Option 1: Google Colab (easiest)**
1. Open `main_N_Cuerpos.ipynb` in [Google Colab](https://colab.research.google.com/) (File → Upload notebook, or from GitHub).
2. Run the cells from top to bottom.

**Option 2: on your computer**
```bash
git clone https://github.com/tobi557/MAT282_SystemaSolar.git
cd MAT282_SystemaSolar
conda env create -f environment.yml
conda activate orbit
jupyter notebook main_N_Cuerpos.ipynb
```
If libraries are added to the environment later: `conda env update --file environment.yml --prune`.

### Execution order

The notebook is split into sections. Most cells are independent, except these:

- **Implicit Euler verification:** requires running the *SIMULACIÓN CON 40 ÓRBITAS + STÖRMER-VERLET* cell and the `solve_implicit_step_2d` cell first.
- **Solar system log error** and **Error against JPL Horizons:** require running the *SIMULACIÓN DEL SISTEMA SOLAR CON STÖRMER-VERLET* cell first.
- **Error against JPL Horizons:** downloads data from the Horizons API, so it needs an internet connection.

Simulations with many orbits (mainly because of implicit Euler) can take a few minutes.

### `resultados/` folder

| Folder | Contents |
|---|---|
| `01_dos_cuerpos_20_orbitas` … `04_dos_cuerpos_50_orbitas` | Two-body problem with 20, 30, 40 and 50 orbits: orbits, each method vs the analytical solution, error vs time, collapse of the implicit Euler semi-major axis, and error table per orbit |
| `05_verlet_20_orbitas`, `06_verlet_40_orbitas` | Same as above, adding Störmer–Verlet |
| `07_euler_implicito` | Run times of `scipy.optimize.root` vs our own Newton solver, and verification that the implicit step runs out of solutions |
| `08_sistema_solar` | Solar system orbits, relative energy error, log error, log-log plot, and position error against JPL Horizons |

### Data

Initial conditions from [JPL Horizons](https://ssd.jpl.nasa.gov/horizons/) (DE441 ephemerides): state vectors in the ecliptic plane, in AU and AU/day, at epoch 2026-09-09 00:00 TDB.
