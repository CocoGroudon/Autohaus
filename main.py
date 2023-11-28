import logging
import datetime

import settings
from autohaus import Autohaus
from GUI import GUI

def __init_logger():
    logging.basicConfig(level=logging.DEBUG, filename=f"{settings.BASE_DIR}/{datetime.datetime.now().strftime('%Y-%m-%d---%H-%M-%S')}.log")
    logger = logging.getLogger("Autohaus")
    logger.setLevel("INFO")

__init_logger()
_logger = logging.getLogger("Autohaus")

if __name__ == '__main__':
    autohaus = Autohaus()
    gui = GUI(autohaus=autohaus)
    gui.mainloop()