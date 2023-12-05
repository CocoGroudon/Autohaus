# from . import chassis
# from .engine import *
# from .gearbox import *
# from .tire import *
import os

#import every part from this dierctory dynamicaly
for part in os.listdir(os.path.dirname(__file__)):
    if part != "__init__.py" and not part.endswith(".py"):
        myimport = f"from . import {part}"
        exec(myimport)


from .base import Part


# get every part
known_types = {}

def add_subclasses(myclas):
    for myclas in myclas.__subclasses__():
        known_types[myclas.__name__] = myclas
        add_subclasses(myclas)

add_subclasses(Part)
    
