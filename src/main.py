import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def load_coordinates_from_csv(file_path):
    df = pd.read_csv(file_path, header=None)
    
    if df.shape[1] == 3:
        x_coords, y_coords, z_coords = df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2]
    elif df.shape[1] == 4:
        x_coords, y_coords, z_coords, _ = df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2], df.iloc[:, 3]
    else:
        raise ValueError("Unexpected number of columns in the CSV file")
    
    coordinates = np.vstack((x_coords, y_coords, z_coords)).T
    return coordinates

def process_coordinates(coordinates):
    print(f"Processing {coordinates.shape[0]} coordinates...")
    
    # Example: Print the first 5 coordinates
    print("First 5 coordinates:")
    print(coordinates[:5])
    
    # Example: Visualize the coordinates in 2D or 3D space
    plt.figure(figsize=(8, 6))
    
    # If the points are in 3D
    if coordinates.shape[1] == 3:
        ax = plt.axes(projection='3d')
        ax.scatter3D(coordinates[:, 0], coordinates[:, 1], coordinates[:, 2], c=coordinates[:, 2], cmap='viridis')
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.set_zlabel('Z axis')
    else:
        plt.scatter(coordinates[:, 0], coordinates[:, 1], c=coordinates[:, 1], cmap='viridis')
        plt.xlabel('X axis')
        plt.ylabel('Y axis')
    
    plt.title('Coordinate Visualization')
    plt.show()

def main():
    csv_file_path = 'path_to_your_csv_file.csv'
    coordinates = load_coordinates_from_csv(csv_file_path)
    process_coordinates(coordinates)

if __name__ == '__main__':
    main()
