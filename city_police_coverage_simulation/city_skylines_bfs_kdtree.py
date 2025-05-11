"""
Police Station Coverage Optimizer – BFS and KD-Tree Based Analysis Inspired by Cities: Skylines

This script simulates budget-aware police station placement optimization on a city grid,
inspired by the city management mechanics in *Cities: Skylines*, where players must balance
police coverage radius against placement cost to ensure citizen safety.

Given a grid representing the city and user-defined police station positions,
the script calculates the **minimum required radius** to fully cover all areas
based on different distance models:
- **Brute-Force Search** (Baseline, O(N) per cell)
- **Multi-Source BFS** (Optimal for grid-based Chebyshev/Manhattan distance, O(Rows × Cols) total)
- **KD-Tree Search** (Optimal for sparse or Euclidean distance scenarios, O(log N) per query)

Features:
- Interactive grid-based placement of police stations via matplotlib
- Three selectable distance models: Brute-Force, BFS, KD-Tree
- Interactive slider to dynamically visualize and adjust police coverage radius
- Heatmap and boundary visualizations for operational clarity

Use Cases:
- Educational demonstration of distance-based coverage algorithms
- Game design tools for balancing service area and cost
- Real-world urban planning or facility placement simulation

Inspired by *Cities: Skylines* budget management and *LeetCode 475* heating coverage challenge.

Author: Tianlang Liu
License: MIT
"""

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.widgets import Slider
import numpy as np
from scipy.spatial import KDTree


def interactive_radius_control(rows, cols, police_stations, initial_radius):
    """
    Visualize police station coverage with an interactive radius slider.

    Args:
        rows (int): Number of rows in the grid representing the city map.
        cols (int): Number of columns in the grid representing the city map.
        police_stations (List[Tuple[int, int]]): List of police station positions as (row, col) tuples.
        initial_radius (int): Initial radius to visualize coverage when the slider is first displayed.

    Returns:
        None
    """
    colors = list(mcolors.TABLEAU_COLORS.values())
    grid = np.zeros((rows, cols))
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.25)
    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    plt.xticks([])
    plt.yticks([])

    # Draw grid lines
    for x in range(cols + 1):
        ax.vlines(x, 0, rows, colors='black', linewidth=1)
    for y in range(rows + 1):
        ax.hlines(y, 0, cols, colors='black', linewidth=1)

    img = ax.imshow(grid, cmap='Greys', vmin=0, vmax=1,
                    extent=[0, cols, 0, rows], origin='lower', alpha=0.8)

    # Add axis labels
    for x in range(cols):
        ax.text(x + 0.5, -0.5, f'{x}', ha='center', va='center', fontsize=12, color='black')
    for y in range(rows):
        ax.text(-0.5, y + 0.5, f'{y}', ha='center', va='center', fontsize=12, color='black')
    # y->row, x->col
    rectangles = []
    for idx, (py, px) in enumerate(police_stations):
        color_rgb = mcolors.to_rgb(colors[idx % len(colors)])
        rect = plt.Rectangle((px - initial_radius, py - initial_radius),
                             2 * initial_radius + 1,
                             2 * initial_radius + 1,
                             linewidth=2,
                             edgecolor=color_rgb,
                             facecolor=color_rgb,
                             alpha=0.3,
                             clip_on=False)
        ax.add_patch(rect)
        rectangles.append(rect)
        ax.scatter(px + 0.5, py + 0.5, s=200, edgecolor='black', facecolor=color_rgb, zorder=5)

    plt.title(f"Coverage of Police Stations when radius is {initial_radius}")

    ax_radius = plt.axes([0.25, 0.1, 0.5, 0.03])
    radius_slider = Slider(ax_radius, 'Radius', 0, 2 * max(rows, cols), valinit=initial_radius, valstep=1)

    def update(val):
        # y->row, x->col
        r = int(radius_slider.val)
        for idx, (py, px) in enumerate(police_stations):
            rectangles[idx].set_xy((px - r, py - r))
            rectangles[idx].set_width(2 * r + 1)
            rectangles[idx].set_height(2 * r + 1)
        fig.canvas.draw_idle()

    radius_slider.on_changed(update)
    plt.show()


def get_police_positions(rows, cols):
    """
    Interactive tool to manually place police stations on a grid by mouse clicks.

    Args:
        rows (int): Number of rows in the grid.
        cols (int): Number of columns in the grid.

    Returns:
        List[Tuple[int, int]]: List of selected police station positions as (row, col) tuples.
    """
    grid = np.zeros((rows, cols))
    fig, ax = plt.subplots()
    ax.set_xlim(0, cols)
    ax.set_ylim(0, rows)
    plt.xticks([])
    plt.yticks([])

    for x in range(cols + 1):
        ax.vlines(x, 0, rows, colors='black', linewidth=1)
    for y in range(rows + 1):
        ax.hlines(y, 0, cols, colors='black', linewidth=1)

    img = ax.imshow(grid, cmap='Greys', vmin=0, vmax=1,
                    extent=[0, cols, 0, rows], origin='lower', alpha=0.8)

    for x in range(cols):
        ax.text(x + 0.5, -0.5, f'{x}', ha='center', va='center', fontsize=12, color='black')
    for y in range(rows):
        ax.text(-0.5, y + 0.5, f'{y}', ha='center', va='center', fontsize=12, color='black')

    police_positions = []

    def onclick(event):
        if event.inaxes == ax:
            x = int(event.xdata)
            y = int(event.ydata)
            if 0 <= x < cols and 0 <= y < rows:
                ax.scatter(x + 0.5, y + 0.5, s=200, edgecolor='black', facecolor='black', zorder=5)
                plt.draw()
                police_positions.append((y, x))

    fig.canvas.mpl_connect('button_press_event', onclick)
    plt.title("Click to place police stations. Close window when done.")
    plt.show()
    print("Marked positions:", police_positions)
    return police_positions
def get_nearest_distance_to_police_stations_brutal_force(i, j, police_stations):
    """
    Calculate the nearest Chebyshev distance using brute-force search.

    Args:
        i (int): Row index of the cell.
        j (int): Column index of the cell.
        police_stations (List[Tuple[int, int]]): List of police station positions.

    Returns:
        float: Chebyshev distance to the nearest police station.
    """
    distance = float('inf')
    for py, px in police_stations:
        distance = min(distance, max(abs(i - py), abs(j - px)))
    return distance

def get_nearest_distance_to_police_stations_bfs(rows, cols, police_stations):
    """
    Calculate the nearest Chebyshev distance using Breadth-First Search (BFS).

    Args:
        i (int): Row index of the cell.
        j (int): Column index of the cell.
        rows (int): Number of rows in the grid.
        cols (int): Number of columns in the grid.
        police_stations (List[Tuple[int, int]]): List of police station positions.

    Returns:
        int: Chebyshev distance to the nearest police station.
    """
    """
    Calculate the nearest Chebyshev distance for all cells using multi-source BFS.

    Args:
        rows (int): Number of rows in the grid.
        cols (int): Number of columns in the grid.
        police_stations (List[Tuple[int, int]]): List of police station positions.

    Returns:
        np.ndarray: 2D array of shape (rows, cols) with nearest distances.
    """
    ##!!Warning, when the number of police stations is small while the row and col, this will be VERY SLOW
    # And will costs a lot of memory
    distance_map = np.full((rows, cols), 0)  # Initialize with infinity
    visited = np.zeros((rows, cols), dtype=bool)  # Track visited cells
    queue = []

    # Initialize BFS with all police stations at distance 0
    for py, px in police_stations:
        if 0 <= py < rows and 0 <= px < cols:
            queue.append((py, px, 0))
            visited[py, px] = True
            distance_map[py, px] = 0

    # 8-connected directions (Chebyshev distance)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1),
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]

    while queue:
        y, x, dist = queue.pop(0)
        for dy, dx in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < rows and 0 <= nx < cols and not visited[ny, nx]:
                visited[ny, nx] = True
                distance_map[ny, nx] = dist + 1
                queue.append((ny, nx, dist + 1))

    return distance_map
    # if (i, j) in police_stations:
    #     return 0
    # queue = [(i, j)]
    # visited = set(queue)
    # distance = 0
    # while queue:
    #     next_layer = []
    #     while queue:
    #         ci, cj = queue.pop(0)
    #         for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
    #             ni, nj = ci + dx, cj + dy
    #             if 0 <= ni < rows and 0 <= nj < cols and (ni, nj) not in visited:
    #                 if (ni, nj) in police_stations:
    #                     return distance + 1
    #                 visited.add((ni, nj))
    #                 next_layer.append((ni, nj))
    #     queue = next_layer
    #     distance += 1
    # return distance  # Unreachable case, but functionally complete

def get_nearest_distance_to_police_stations_kd_tree(i, j, police_stations):
    """
    Calculate the nearest Chebyshev distance from a grid cell to any police station using KD-Tree.

    Args:
        i (int): Row index of the cell.
        j (int): Column index of the cell.
        police_stations (List[Tuple[int, int]]): List of police station positions.

    Returns:
        float: Chebyshev distance to the nearest police station.
    """
    tree = KDTree(police_stations)
    distance, _ = tree.query((i, j), p=np.inf)
    return distance


def get_largest_nearest_distance_to_police_stations(rows, cols, police_stations):
    """
    Calculate the maximum nearest Chebyshev distance from any grid cell to the nearest police station.

    Args:
        rows (int): Number of rows in the grid.
        cols (int): Number of columns in the grid.
        police_stations (List[Tuple[int, int]]): List of police station positions.

    Returns:
        float: The largest nearest Chebyshev distance across all grid cells.11
    """
    max_distance = 0
    #distance_map = get_nearest_distance_to_police_stations_bfs(rows, cols, police_stations)
    for i in range(rows):
        for j in range(cols):
            distance = get_nearest_distance_to_police_stations_kd_tree(i, j, police_stations)
            max_distance = max(max_distance, distance)
    #max_distance = np.max(distance_map)
    return max_distance


if __name__ == "__main__":
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
    except ValueError:
        print("Invalid input. Please enter integers for rows and columns.")
        raise SystemExit

    police_stations = get_police_positions(rows, cols)
    smallest_radius = get_largest_nearest_distance_to_police_stations(rows, cols, police_stations)
    print("The smallest radius of police stations is:", smallest_radius)
    interactive_radius_control(rows, cols, police_stations, smallest_radius)
