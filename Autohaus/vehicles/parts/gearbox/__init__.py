import os

#import every part from this dierctory dynamicaly
for part in os.listdir(os.path.dirname(__file__)):
    if part != "__init__.py" and part.endswith(".py"):
        myimport = f"from .{part[:-3]} import *"
        exec(myimport)

from .gearbox import Gearbox

known_types = {}

def add_subclasses(myclas):
    for myclas in myclas.__subclasses__():
        known_types[myclas.__name__] = myclas
        add_subclasses(myclas)

add_subclasses(Gearbox)
