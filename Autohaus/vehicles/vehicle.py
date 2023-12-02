import json
import os
import time

from .parts.chassis import Chassis
from .parts.engine import Engine
from .parts.gearbox import Gearbox
from .parts.tire import Tire
from ..settings import Settings


class Vehicle:
    storage_path = None

    def __init__(self, brand, model, price, color, description, image_path, **kwargs):
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
        self.image_path = image_path

        self.description = description
        self.sold = False

        self.vehicle_enum = None
        if "vehicle_enum" in kwargs:
            self.vehicle_enum = kwargs["vehicle_enum"]

        
    def save_json(self, file):
        json.dump(self.__dict__, file)

    def load_json(self, json_string):
        data = json.loads(json_string)
        self.__dict__.update(data)
        return self
    
    def get_image(self):
        if not self.image:
            return None
        path = os.path.join(Settings.IMAGE_DIR, f"{self.vehicle_enum}-{self.brand}-{self.model}.png")
        return path




