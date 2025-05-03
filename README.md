# 🎮 Algorithm in Games

> A collection of imaginative algorithms inspired by game mechanics and virtual worlds.

This project explores how real algorithmic thinking can be applied to game-like scenarios — from building efficient railway systems on Mars to generating twisty mazes for dungeon crawlers.

Whether you're a game developer, algorithm enthusiast, or someone who just loves turning brainwaves into code, this repo is for you.

---

## 🌌 Project Philosophy

Games are more than entertainment — they're simulations, puzzles, systems.  
This project asks: **"What if we model them like real problems?"**

We take ideas from games and build:
- Formal problem definitions
- Simulation or optimization code (mostly in Python)
- Visualizations and clear comments
- Occasionally a little worldbuilding for flavor 😄

---

## 🧠 Modules

| Module | Description |
|--------|-------------|
| `surviving-mars-railroads/` | Use Prim’s algorithm to construct a minimal-cost railway network between Mars bases |

---

## 🚀 Example: Surviving Mars Railroads

Inspired by *Surviving Mars*, this module builds a cost-effective railway network between Mars bases.

Each base is a node, and randomly generated edge weights simulate different terrain costs.  
We use **Prim's algorithm** to find a **Minimum Spanning Tree (MST)** — the cheapest way to connect all bases without cycles.

![Prim MST example](surviving-mars-railroads/images/mst_example.png)

---

## 📦 How to Run

### 1. Clone the repo  
```bash
git clone https://github.com/your-username/algorithm-in-games.git
cd algorithm-in-games/surviving-mars-railroads
```

### 2. Install dependencies  
```bash
pip install networkx matplotlib
```

### 3. Run the module  
```bash
python mars_mst.py
```

You will be prompted to enter the number of bases.  
The script will:
- Generate a fully connected graph
- Run Prim’s algorithm
- Visualize the MST using NetworkX + Matplotlib

---

## 💡 Inspiration

This project is inspired by:
- *Surviving Mars* — logistics and infrastructure planning  
- *Dwarf Fortress* — procedural maps and survival logic  
- *Into the Breach* — minimalist, clean simulation mechanics  
- And late-night brainwaves that ask:  
  *"What if this game system were an algorithm?"*

---

## 🛠️ Roadmap

- [x] Mars MST simulation  
---

## 📝 License

This project is released under the MIT License.

---

## ❤️ Feedback Welcome

Have a fun mechanic you want to simulate with code?  
Open an issue, fork the repo, or just drop a ⭐ if this gave you a spark of inspiration!
