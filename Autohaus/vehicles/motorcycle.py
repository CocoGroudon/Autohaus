from .vehicle import Vehicle
from .parts.engine import Engine
from .parts.gearbox import Gearbox
from .parts.tire import Tire
from .parts.chassis import Chassis

from ..settings import Settings

class Motorcycle(Vehicle):
    # set path for motorcycles directory
    storage_path = Settings.MOTORCYCLES_DIR

    def __init__(self, brand, model, price, **kwargs):
        super().__init__(brand, model, price, **kwargs)