import numpy as np
import matplotlib.pyplot as plt

def plot_paths(paths_XYs, title='Curves'):
    print(f"Plotting {len(paths_XYs)} paths in '{title}'")
    fig, ax = plt.subplots(tight_layout=True, figsize=(8, 8))
    for path in paths_XYs:
        print(f"Plotting path with {len(path)} points.")
        ax.plot(path[:, 0], path[:, 1], linewidth=2)
    ax.set_aspect('equal')
    ax.set_title(title)
    plt.show()

def plot_two_windows(original_paths, regularized_paths):
    print(f"Original paths: {len(original_paths)}, Regularized paths: {len(regularized_paths)}")
    
    plt.figure(figsize=(16, 8))
    
    plt.subplot(1, 2, 1)
    for path in original_paths:
        plt.plot(path[:, 0], path[:, 1], linewidth=2)
    plt.title('Original Curves')
    plt.gca().set_aspect('equal', adjustable='box')
    
    plt.subplot(1, 2, 2)
    for path in regularized_paths:
        plt.plot(path[:, 0], path[:, 1], linewidth=2)
    plt.title('Regularized Curves')
    plt.gca().set_aspect('equal', adjustable='box')
    
    plt.show()
