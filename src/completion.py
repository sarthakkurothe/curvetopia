import numpy as np

def complete_curves(paths_XYs):
    completed_paths = []
    for path in paths_XYs:
        completed_path = []
        for points in path:
            points = np.array(points)
            if len(points) < 2:
                completed_path.append(points)
                continue
            if not np.allclose(points[0], points[-1]):
                points = np.vstack([points, points[0]])
            completed_path.append(points)
        completed_paths.append(completed_path)
    return completed_paths
