from .autohaus import Autohaus
from .GUI import GUI

def main():
    autohaus = Autohaus()
    gui = GUI(autohaus=autohaus)
    gui.mainloop()


main()
