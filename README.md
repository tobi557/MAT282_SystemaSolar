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

Lo recomendado es ejecutar todo el notebook de una vez, de arriba hacia abajo: en Colab con *Entorno de ejecución → Ejecutar todas*, y en Jupyter con *Run → Run All Cells*.

Si se quiere correr solo una parte, hay que tener en cuenta que algunas celdas dependen de otras:

- **Verificación del Euler implícito:** necesita haber corrido antes la celda *SIMULACIÓN CON 40 ÓRBITAS + STÖRMER-VERLET* y la celda de `solve_implicit_step_2d`.
- **Log error del sistema solar** y **Error contra JPL Horizons:** necesitan haber corrido antes la celda *SIMULACIÓN DEL SISTEMA SOLAR CON STÖRMER-VERLET*.
- **Error contra JPL Horizons:** descarga datos desde la API de Horizons, así que necesita internet.
- **Verificación del orden de convergencia de Störmer–Verlet:** es independiente; se puede ejecutar sola.

Tiempos aproximados en Colab: las simulaciones de dos cuerpos ~1–2 min cada una (sobre todo por el Euler implícito), los `%%timeit` ~4 min, la simulación del sistema solar (10.000 años) ~12–15 min y la descarga de Horizons ~1–2 min.

### Carpeta `resultados/`

| Carpeta | Qué contiene |
|---|---|
| `01_dos_cuerpos_20_orbitas` … `04_dos_cuerpos_50_orbitas` | Dos cuerpos con 20, 30, 40 y 50 órbitas: órbitas, cada método vs la analítica, error vs tiempo, colapso del semieje mayor del Euler implícito y tabla de error por órbita |
| `05_verlet_20_orbitas`, `06_verlet_40_orbitas` | Lo mismo, agregando Störmer–Verlet |
| `07_euler_implicito` | Tiempos de `scipy.optimize.root` vs Newton propio, y verificación de que el paso implícito se queda sin solución |
| `08_sistema_solar` | Sistema solar simulado durante 10.000 años ($\Delta t$ = 0.25 días): órbitas, error relativo de energía, log error, log-log y error de posición contra JPL Horizons durante 7000 años |
| `09_orden_convergencia` | Verificación del orden de convergencia de Störmer–Verlet: error máximo vs $\Delta t$ en log-log (pendiente $p = 2$) |

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

The recommended way is to run the whole notebook at once, from top to bottom: in Colab with *Runtime → Run all*, and in Jupyter with *Run → Run All Cells*.

If you only want to run part of it, keep in mind that some cells depend on others:

- **Implicit Euler verification:** requires running the *SIMULACIÓN CON 40 ÓRBITAS + STÖRMER-VERLET* cell and the `solve_implicit_step_2d` cell first.
- **Solar system log error** and **Error against JPL Horizons:** require running the *SIMULACIÓN DEL SISTEMA SOLAR CON STÖRMER-VERLET* cell first.
- **Error against JPL Horizons:** downloads data from the Horizons API, so it needs an internet connection.
- **Störmer–Verlet order of convergence check:** independent; it can be run on its own.

Approximate run times in Colab: each two-body simulation ~1–2 min (mainly because of implicit Euler), the `%%timeit` cells ~4 min, the solar system simulation (10,000 years) ~12–15 min, and the Horizons download ~1–2 min.

### `resultados/` folder

| Folder | Contents |
|---|---|
| `01_dos_cuerpos_20_orbitas` … `04_dos_cuerpos_50_orbitas` | Two-body problem with 20, 30, 40 and 50 orbits: orbits, each method vs the analytical solution, error vs time, collapse of the implicit Euler semi-major axis, and error table per orbit |
| `05_verlet_20_orbitas`, `06_verlet_40_orbitas` | Same as above, adding Störmer–Verlet |
| `07_euler_implicito` | Run times of `scipy.optimize.root` vs our own Newton solver, and verification that the implicit step runs out of solutions |
| `08_sistema_solar` | Solar system simulated over 10,000 years ($\Delta t$ = 0.25 days): orbits, relative energy error, log error, log-log plot, and position error against JPL Horizons over 7000 years |
| `09_orden_convergencia` | Störmer–Verlet order of convergence check: maximum error vs $\Delta t$ in log-log (slope $p = 2$) |

### Data

Initial conditions from [JPL Horizons](https://ssd.jpl.nasa.gov/horizons/) (DE441 ephemerides): state vectors in the ecliptic plane, in AU and AU/day, at epoch 2026-09-09 00:00 TDB.
