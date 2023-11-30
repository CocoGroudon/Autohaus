import json
import os
import time

from credentialManager import CredentialManager
import settings

class Car:
    def __init__(self, brand, model, price, **kwargs):
        self.cars_enum = -1 # -1 means not enumerated
        self.brand = brand
        self.model = model
        self.price = price


class Autohaus:
    def __init__(self):
        self.credentialManager = CredentialManager()
        self.user = None    

        # preload config in case it doesn't exist
        self.cars = []
        self.cars_enum = 0
        self.known_models = {}

        self.load_config()
        self.load_cars()

    def get_brands(self):
        brands = self.known_models.keys()
        print(brands)
        return brands
    
    def get_models(self, brand):
        try: # incase brand doesn't exist
            return self.known_models[brand]
        except KeyError:
            return []

    def load_config(self):
        # test if config exists
        if not os.path.exists(os.path.join(settings.STATIC_DIR, "config.json")):
            self.save_config()
            return
        with open(os.path.join(settings.STATIC_DIR, "config.json"), "r") as f:
            data = json.load(f)
            if "cars_enum" in data:
                self.cars_enum = data["cars_enum"]
            if "known_models" in data:
                self.known_models = data["known_models"]

    def load_cars(self):
        for car in os.listdir(settings.CARS_DIR):
            with open(os.path.join(settings.CARS_DIR, car), "r") as f:
                data = json.load(f)
                self.cars.append(Car(**data))

    def save_dynamic_config(self):
        config_file = os.path.join(settings.STATIC_DIR, "config.json")

        with open(config_file, "r") as f:
            data = json.load(f)

        data["cars_enum"] = self.cars_enum

        with open(config_file, "w") as f:
            json.dump(data, f)


    def load_cars(self):
        for car in os.listdir(settings.CARS_DIR):
            with open(os.path.join(settings.CARS_DIR, car), "r") as f:
                data = json.load(f)
                self.cars.append(Car(**data))

    def save_car(self, car):
        with open(os.path.join(settings.CARS_DIR, f"{car.cars_enum} {car.brand}-{car.model}.json"), "w") as f:
            json.dump(car.__dict__, f)

    def add_car(self, brand, model, price):
        car = Car(brand=brand, model=model, price=price)
        car.cars_enum = self.cars_enum
        self.cars_enum += 1

        self.cars.append(car)
        self.save_car(car)

    def get_cars(self):
        return self.cars
    
    def set_user(self, user):
        self.user = user

    def close(self):
        self.save_dynamic_config()
        self.logout()

    def logout(self):
        self.user = None