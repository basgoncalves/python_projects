import numpy as np
from stl import mesh
from bops import bops as bp
from mpl_toolkits import mplot3d

def load_stl_file(file_path):
    # Load the STL file
    stl_mesh = mesh.Mesh.from_file(file_path)

    # Get the vertices of the mesh
    vertices = stl_mesh.vectors

    # Calculate the local coordinate system
    min_x, min_y, min_z = np.min(vertices, axis=(0, 1))
    max_x, max_y, max_z = np.max(vertices, axis=(0, 1))
    center_x, center_y, center_z = (min_x + max_x) / 2, (min_y + max_y) / 2, (min_z + max_z) / 2
    size_x, size_y, size_z = max_x - min_x, max_y - min_y, max_z - min_z

    # Print the local coordinate system
    print("Local Coordinate System:")
    print(f"Center: ({center_x}, {center_y}, {center_z})")
    print(f"Size: ({size_x}, {size_y}, {size_z})")

    import matplotlib.pyplot as plt

    def display_stl_shape(vertices):
        # Create a new figure
        fig = plt.figure()

        # Create a 3D axes object
        ax = plt.axes(projection='3d')

        # Plot the vertices of the mesh
        ax.scatter3D(vertices[:, :, 0], vertices[:, :, 1], vertices[:, :, 2])

        # Set the center of the plot as the origin
        ax.set_xlim3d(center_x - size_x/2, center_x + size_x/2)
        ax.set_ylim3d(center_y - size_y/2, center_y + size_y/2)
        ax.set_zlim3d(center_z - size_z/2, center_z + size_z/2)

        # Set labels for the axes
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        # Show the plot
        plt.show()

    # Example usage
    display_stl_shape(vertices)

# Example usage
file_path = bp.select_file(__file__)
load_stl_file(file_path)
