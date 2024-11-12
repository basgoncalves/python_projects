from bops2 import bops as bp
import shutil
import os

print(bp.__version__)


exit()

def copy_c3d_files(source_dir, dest_dir):
  """Copies C3D files from source directory to destination directory, preserving directory structure.

  Args:
    source_dir: The path to the source directory.
    dest_dir: The path to the destination directory.
  """

  for root, dirs, files in os.walk(source_dir):
    for file in files:
      if file.endswith('.c3d'):
        # Create the destination directory if it doesn't exist
        dest_root = os.path.join(dest_dir, os.path.relpath(root, source_dir))
        os.makedirs(dest_root, exist_ok=True)

        # Copy the C3D file
        src_file = os.path.join(root, file)
        dst_file = os.path.join(dest_root, file)
        shutil.copy2(src_file, dst_file)

# Example usage:
source_directory = r'E:\3-PhD\Data\MocapData\InputData'
destination_directory = r'C:\Users\Bas\Desktop\C3D_PhD_BG'

copy_c3d_files(source_directory, destination_directory)
