from src.reader import read_csv
from src.visualizer import plot
from src.regularizer import regularize_shapes
from src.symmetry import find_symmetry
from src.completion import complete_curves

def main():
    # Read the data
    input_path = 'datasets/occlusion1.csv'
    paths_XYs = read_csv(input_path)

    # Regularize the curves
    regularized_paths = regularize_shapes(paths_XYs)
    plot(regularized_paths)  # Visualize the regularized curves

    # Find symmetry in the curves
    symmetric_paths = find_symmetry(regularized_paths)
    plot(symmetric_paths)  # Visualize the symmetric curves

    # Complete the incomplete curves
    completed_paths = complete_curves(symmetric_paths)
    plot(completed_paths)  # Visualize the completed curves

if __name__ == '__main__':
    main()
