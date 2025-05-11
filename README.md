# Algorithm in Games

> A collection of imaginative algorithms inspired by game mechanics and virtual worlds.

This project explores how real algorithmic thinking can be applied to game-like scenarios — from building efficient railway systems on Mars to optimizing police station coverage in city simulators.

Whether you're a game developer, algorithm enthusiast, or someone who just loves turning brainwaves into code, this repo is for you.

---

## Project Philosophy

Games are more than entertainment — they're simulations, puzzles, systems.
This project asks: **"What if we model them like real problems?"**

We take ideas from games and build:

* Formal problem definitions
* Simulation or optimization code (mostly in Python)
* Visualizations and clear comments
* Occasionally a little worldbuilding for flavor 😁

---

## Modules

| Module                             | Description                                                                                                                   |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| `surviving-mars-railroads/`        | Use Prim’s algorithm to construct a minimal-cost railway network between Mars bases                                           |
| `city-police-coverage-simulation/` | Optimize police station placement and radius using BFS, KD-Tree, and interactive visualization inspired by *Cities: Skylines* |

---

## 🚓 Example: City Police Coverage Simulation

Inspired by *Cities: Skylines*' police budget management system,
this module helps you find the **minimum necessary radius** to fully cover a city grid based on:

* **Brute-Force Search**
* **Multi-Source BFS (Chebyshev/Manhattan)**
* **KD-Tree Search (Euclidean/Chebyshev)**

Features:

* Interactive **city grid editor** for placing police stations
* **Slider control** to dynamically visualize radius impact
* **Coverage analytics** based on different distance models

---

## 🚀 Example: Surviving Mars Railroads

Inspired by *Surviving Mars*, this module builds a cost-effective railway network between Mars bases.

Each base is a node, and randomly generated edge weights simulate different terrain costs.
We use **Prim's algorithm** to find a **Minimum Spanning Tree (MST)** — the cheapest way to connect all bases without cycles.

![Prim MST example](surviving-mars-railroads/example.png)

---

## How to Run

### 1. Clone the repo

```bash
git clone https://github.com/your-username/algorithm-in-games.git
```

### 2. Install dependencies

```bash
pip install matplotlib numpy scipy networkx
```

### 3. Run a module

#### 🚤 Mars Railway (MST)

```bash
cd algorithm-in-games/surviving-mars-railroads
python surviving_mars-prim.py
```

#### 🚓 Police Coverage Simulation

```bash
cd algorithm-in-games/city-police-coverage-simulation
python city_police_coverage_simulation.py
```

---

## Inspiration

This project is inspired by:

* *Surviving Mars* — logistics and infrastructure planning
* *Cities: Skylines* — service coverage and budget management

---

## Roadmap

* [x] Mars MST simulation
* [x] City police coverage simulation with interactive controls
* [ ] Add more game-inspired optimization models

---

## License

This project is released under the MIT License.

---

## ❤️ Feedback Welcome

Have a fun mechanic you want to simulate with code?
Open an issue, fork the repo, or just drop a ⭐ if this gave you a spark of inspiration!
