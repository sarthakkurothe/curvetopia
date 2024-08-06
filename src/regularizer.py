import numpy as np

def is_straight_line(points):
    if len(points) < 2:
        return False
    points = np.array(points)
    x_coords, y_coords = points[:, 0], points[:, 1]
    return np.all(np.isclose(np.diff(y_coords) / np.diff(x_coords), (y_coords[-1] - y_coords[0]) / (x_coords[-1] - x_coords[0])))

def is_circle(points):
    if len(points) < 3:
        return False
    points = np.array(points)
    center = np.mean(points, axis=0)
    radius = np.linalg.norm(points[0] - center)
    return np.all(np.isclose(np.linalg.norm(points - center, axis=1), radius))

def regularize_shapes(paths_XYs):
    regularized_paths = []
    for path in paths_XYs:
        regularized_path = []
        for points in path:
            points = np.array(points)
            if is_straight_line(points):
                regularized_path.append([points[0], points[-1]])
            elif is_circle(points):
                center = np.mean(points, axis=0)
                radius = np.linalg.norm(points[0] - center)
                circle_points = np.array([[center[0] + radius * np.cos(t), center[1] + radius * np.sin(t)] for t in np.linspace(0, 2 * np.pi, 100)])
                regularized_path.append(circle_points)
            else:
                regularized_path.append(points)
        regularized_paths.append(regularized_path)
    return regularized_paths
