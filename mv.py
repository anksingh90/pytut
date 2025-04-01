import os
import shutil

# Define the root directory and the target directory
root_dir = "/workspaces/pytut"
target_dir = os.path.join(root_dir, "cs_11")

# Iterate through all items in the root directory
for item in os.listdir(root_dir):
    item_path = os.path.join(root_dir, item)
    
    # Skip the target directory itself
    if item == "cs_11":
        continue
    
    # Move the item to the target directory
    shutil.move(item_path, target_dir)

print("All files and directories have been moved into 'cs_11'.")
