import numpy as np

def find_symmetry(paths_XYs):
    symmetric_paths = []
    for path in paths_XYs:
        symmetric_path = []
        for points in path:
            points = np.array(points)
            if len(points) < 2:
                symmetric_path.append(points)
                continue
            x_coords, y_coords = points[:, 0], points[:, 1]
            if np.all(np.isclose(x_coords, np.mean(x_coords))):  # Vertical symmetry
                symmetric_path.append(points)
            elif np.all(np.isclose(y_coords, np.mean(y_coords))):  # Horizontal symmetry
                symmetric_path.append(points)
            else:
                symmetric_path.append(points)
        symmetric_paths.append(symmetric_path)
    return symmetric_paths
