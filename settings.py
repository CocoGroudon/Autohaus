# Description: This file contains the settings for the project
import os

# Path for the the directory of settings.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path for the static files
STATIC_DIR = os.path.join(BASE_DIR, 'static')
LOGS_DIR = os.path.join(STATIC_DIR, 'logs')
CARS_DIR = os.path.join(STATIC_DIR, 'cars')