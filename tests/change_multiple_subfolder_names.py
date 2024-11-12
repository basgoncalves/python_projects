import os

def change_subfolder_names(directory):
    for root, dirs, files in os.walk(directory):
        for dir_name in dirs:
            if dir_name == "Meshlab":
                old_path = os.path.join(root, dir_name)
                new_path = os.path.join(root, "Meshlab_BG")
                os.rename(old_path, new_path)

# Replace the directory path with the desired directory
directory = r"C:\Users\Bas\ucloud\MRI_segmentation_BG\acetabular_coverage"
change_subfolder_names(directory)