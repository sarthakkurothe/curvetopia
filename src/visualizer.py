import numpy as np
import matplotlib.pyplot as plt

def plot(paths_XYs):
    fig, ax = plt.subplots(tight_layout=True, figsize=(8, 8))
    colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    for i, XYs in enumerate(paths_XYs):
        c = colors[i % len(colors)]
        for XY in XYs:
            XY = np.array(XY)
            if XY.ndim == 1:
                ax.plot(XY[0], XY[1], 'o', c=c)  # Plot a single point
            else:
                ax.plot(XY[:, 0], XY[:, 1], c=c, linewidth=2)
    ax.set_aspect('equal')
    plt.show()
