# Description: This file contains the settings for the project
import os
import dataclasses

class Settings:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    STATIC_DIR = os.path.join(BASE_DIR, 'static')
    IMAGE_DIR = os.path.join(STATIC_DIR, 'images')
    VEHICLES_DIR = os.path.join(STATIC_DIR, 'vehicles')
    CARS_DIR = os.path.join(VEHICLES_DIR, 'cars')
    MOTORCYCLES_DIR = os.path.join(VEHICLES_DIR, 'motorcycles')
