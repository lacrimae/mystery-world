import os
import sys
from src.main_menu import main_menu

# get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# add the parent directory to the Python path
parent_dir = os.path.join(current_dir, '')
sys.path.insert(0, parent_dir)

screen_width = 100

main_menu.start()
