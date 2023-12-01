from .autohaus import Autohaus
from .GUI import GUI

def depickel():
    import pickle
    with open("D:\Schule\Info\Autohaus\Autohaus\car.pkl", "rb") as f:
        data = pickle.load(f)
    return data


# if __name__ == '__main__':
autohaus = Autohaus()
# car = depickel()
# print(car)
# print(car.get_data())
# print(car.__dict__)
# autohaus.add_vehicle(car)
gui = GUI(autohaus=autohaus)
gui.mainloop()