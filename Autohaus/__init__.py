from .autohaus import Autohaus
from .GUI import GUI

# if __name__ == '__main__':
autohaus = Autohaus()
gui = GUI(autohaus=autohaus)
gui.mainloop()