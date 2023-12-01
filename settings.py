# Description: This file contains the settings for the project
import os

# Path for the the directory of settings.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path for the static files
STATIC_DIR = os.path.join(BASE_DIR, 'static')

LOGS_DIR = os.path.join(STATIC_DIR, 'logs')
IMAGE_DIR = os.path.join(STATIC_DIR, 'images')
VEHICLES_DIR = os.path.join(STATIC_DIR, 'vehicles')

CARS_DIR = os.path.join(VEHICLES_DIR, 'cars')
MOTORCYCLES_DIR = os.path.join(VEHICLES_DIR, 'motorcycles')