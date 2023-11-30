import logging
import datetime

import settings
from autohaus import Autohaus, Car
from GUI import GUI

def __init_logger():
    logging.basicConfig(level=logging.DEBUG, filename=f"{settings.BASE_DIR}/{datetime.datetime.now().strftime('%Y-%m-%d---%H-%M-%S')}.log")
    logger = logging.getLogger("Autohaus")
    logger.setLevel("INFO")

__init_logger()
_logger = logging.getLogger("Autohaus")

cars = [
    Car("BMW", "M3", 100000),
    Car("BMW", "M5", 120000),
    Car("BMW", "M6", 140000),
    Car("BMW", "M8", 160000),
    Car("BMW", "X3", 80000),
    Car("BMW", "X5", 100000),
    Car("BMW", "X6", 120000),
    Car("BMW", "X7", 140000),
    Car("BMW", "Z4", 80000),
    Car("BMW", "i8", 160000),
    Car("BMW", "i3", 60000),
    Car("BMW", "1er", 40000),
    Car("BMW", "2er", 50000),
    Car("BMW", "3er", 60000),
    Car("BMW", "4er", 70000),
    Car("BMW", "5er", 80000),
    Car("BMW", "6er", 90000),
    Car("BMW", "7er", 100000),
    Car("BMW", "8er", 110000),
    Car("BMW", "X1", 60000),
    Car("BMW", "X2", 70000),
    Car("BMW", "X3", 80000),
    Car("BMW", "X4", 90000),
    Car("BMW", "X5", 100000),
    Car("BMW", "X6", 110000),
    Car("BMW", "X7", 120000),
    Car("BMW", "Z1", 50000),
    Car("BMW", "Z3", 60000),
    Car("BMW", "Z4", 70000),
    Car("BMW", "M3", 100000),
    Car("BMW", "M5", 120000),
    Car("BMW", "M6", 140000),
    Car("BMW", "M8", 160000),
    Car("BMW", "X3", 80000),
    Car("BMW", "X5", 100000),
    Car("BMW", "X6", 120000),
    Car("BMW", "X7", 140000),
    Car("BMW", "Z4", 80000),
    Car("BMW", "i8", 160000),
    Car("BMW", "i3", 60000),
    Car("BMW", "1er", 40000),
    Car("BMW", "2er", 50000),
    Car("BMW", "3er", 60000),
    Car("BMW", "4er", 70000),
    Car("BMW", "5er", 80000),
    Car("BMW", "6er", 90000),
    Car("BMW", "7er", 100000),
    Car("BMW", "8er", 110000),
    Car("BMW", "X1", 60000),
    Car("BMW", "X2", 70000),
    Car("BMW", "X3", 80000),
    Car("BMW", "X4", 90000),
    Car("BMW", "X5", 100000),
    Car("BMW", "X6", 110000),
    Car("BMW", "X7", 120000),
    Car("BMW", "Z1", 50000),
    Car("BMW", "Z3", 60000),
    Car("BMW", "Z4", 70000),
    Car("BMW", "Z8", 80000)        
]

if __name__ == '__main__':
    autohaus = Autohaus()
    for car in cars:
        autohaus.add_car(car)
    gui = GUI(autohaus=autohaus)
    gui.mainloop()