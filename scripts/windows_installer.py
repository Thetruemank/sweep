import os
import sys
from PyInstaller.__main__ import run

def create_installer():
    try:
        # Define the application directory
        app_dir = os.path.dirname(os.path.abspath(__file__))
        app_dir = os.path.join(app_dir, '..')

        # Define the output directory
        output_dir = os.path.join(app_dir, 'dist')

        # Define the main application file
        main_file = os.path.join(app_dir, 'sweepai', 'api.py')

        # Create the PyInstaller command
        pyinstaller_cmd = [
            '--name=sweepai',
            '--onefile',
            '--windowed',
            f'--distpath={output_dir}',
            main_file,
        ]

        # Run PyInstaller
        run(pyinstaller_cmd)

    except Exception as e:
        print(f'Error creating installer: {e}')
        sys.exit(1)

if __name__ == '__main__':
    create_installer()
