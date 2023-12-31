from .vehicle import Vehicle
from .parts.engine import Engine
from .parts.gearbox import Gearbox
from .parts.tire import Tire
from .parts.chassis import Chassis

from ..settings import Settings

class Car(Vehicle):
    # set path for cars directory
    storage_path = Settings.CARS_DIR

    def __init__(self, brand, model, price, color, description, image_path, engine:Engine, gearbox:Gearbox, tire:Tire, chassis:Chassis,  **kwargs):
        super().__init__(brand, model, price, color, description, image_path)
        print(engine)
        print(gearbox)
        print(tire)
        print(chassis)
        self.parts = {
            "engine": engine,
            "gearbox": gearbox,
            "tire": tire,
            "chassis": chassis
        }

