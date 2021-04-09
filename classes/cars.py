# 03/28/2021
class Car():
    """This class describes model of the car"""

    def __init__(self, brand, model, color):
        """this is the constructor, with required parameters"""
        self.brand = brand
        self.model = model
        self.color = color
        self.odo_reader = 0

    def set_odometer_reader(self, miles):
        """Function to update the value of the odometer_reader global variable"""
        self.odo_reader = miles

    def drive(self):
        """driving action"""
        if self.brand.lower() == "bmw":
            print(f"You are driving FAST car even without DL! isn't it awesome!")
        else:
            print(f"You are driving the car even without DL! isn't it awesome!")

    def do_something(self):
        print("I want to do something:....")
        print("Let me drive:....")
        self.drive()
        # motor = Motorcycle()
        # motor.drive()

    def get_description(self):
        """"""
        greet_user()
        print(f"Model of the car is : {self.model}")
        print(f"Color of the car is : {self.color}")
        print(f"Brand of the car is : {self.brand}")
        print(f"You have {self.odo_reader} miles")




def greet_user():
    print("hello master")


mycar = Car("BMW", "530xi", "black")  # mycar is object, car is the class , this action is instantiation
yourcar = Car("Lexus", "Lexus IS", "silver")

mycar.get_description()
mycar.drive()
mycar.set_odometer_reader(50)
mycar.odo_reader = 20
mycar.color = 'Red'  # direct access to the instance variables
mycar.get_description()
print("-----------------------------------")
yourcar.get_description()
yourcar.drive()
yourcar.set_odometer_reader(30)
yourcar.get_description()


# yourcar.do_something()


class ElectricCar(Car):
    """child class"""

    def __init__(self, brand, model, color):
        """"""
        super().__init__(brand, model, color)
