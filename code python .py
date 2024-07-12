import os
import shutil

# Define the paths
extraction_directory_2 = '/mnt/data/FNF_Remake_Extracted_2/'
web_directory_2 = '/mnt/data/FNF_Remake_Web_2/'

# Create the web directory structure
os.makedirs(web_directory_2, exist_ok=True)
os.makedirs(os.path.join(web_directory_2, 'Assets'), exist_ok=True)
os.makedirs(os.path.join(web_directory_2, 'levels'), exist_ok=True)

# Copy the assets and levels to the web directory
shutil.copytree(os.path.join(extraction_directory_2, 'Assets'), os.path.join(web_directory_2, 'Assets'), dirs_exist_ok=True)
shutil.copytree(os.path.join(extraction_directory_2, 'levels'), os.path.join(web_directory_2, 'levels'), dirs_exist_ok=True)

# Copy other necessary files to the web directory
for file in ['icon.png', 'icon@2x.png', 'colourPickerMemory.plist', 'objectDock.plist', 'gameDetails.plist']:
    shutil.copy(os.path.join(extraction_directory_2, file), os.path.join(web_directory_2, file))

# Create index.html
index_html_path_2 = os.path.join(web_directory_2, 'index.html')
with open(index_html_path_2, 'w') as index_html_file_2:
    index_html_file_2.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FNF Remake</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div id="game-container">
        <!-- Game content will go here -->
    </div>
    <script>
        document.addEventListener('DOMContentLoaded', () => {
            const gameContainer = document.getElementById('game-container');
            
            // Example code to load and display an asset
            const img = document.createElement('img');
            img.src = 'Assets/icon.png';  // Replace with the actual path to your asset
            gameContainer.appendChild(img);

            // Add your game logic here
        });
    </script>
</body>
</html>
""")

# Create README.md
readme_path_2 = os.path.join(web_directory_2, 'README.md')
with open(readme_path_2, 'w') as readme_file_2:
    readme_file_2.write("""# FNF Remake

This is a remake of Friday Night Funkin' made using HyperPad.

## Project Structure

- `Assets/`: Contains all the assets used in the game (images, sounds, etc.).
- `levels/`: Contains the levels or scenes of the game.
- `icon.png` and `icon@2x.png`: Icons for the project.
- `colourPickerMemory.plist`: Configuration for color picking.
- `objectDock.plist`: Information about objects in the project.
- `gameDetails.plist`: Metadata and configuration details about the game.

## How to Play

(Include instructions on how to play or use your project if applicable.)

## Credits

(Include credits if applicable.)
""")

# List the web files to confirm
web_files_2 = os.listdir(web_directory_2)
web_files_2