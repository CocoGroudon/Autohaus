from credentialManager import CredentialManager

class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

class Autohaus:
    def __init__(self):
        self.credentialManager = CredentialManager()
        self.cars = []
        self.user = None    


    def add_car(self, car):
        self.cars.append(car)

    def get_cars(self):
        return self.cars
    
    def set_user(self, user):
        self.user = user

    def logout(self):
        self.user = None