# coding: utf-8

__author__ = "Sachin Shivaramaiah"
__creation_date__ = "9th September"
__last_modified_date__ = "25th September"


class Car:
    # Initializing constructor with arguments = default values for the class Car
    def __init__(self, car_code="AB123456",
                 car_name="Name of Car",
                 car_capacity=4,
                 car_horsepower=100,
                 car_weight=1000,
                 car_type="FWD"):

        # Setting attributes
        self.car_code = car_code
        self.car_name = car_name
        self.car_capacity = car_capacity
        self.car_horsepower = car_horsepower
        self.car_weight = car_weight
        self.car_type = car_type.strip()

    # Python Magic method to print the out format

    def filestr(self):
        return f"{self.car_code}, {self.car_name}, {self.car_capacity}," \
               f"{self.car_horsepower}, {self.car_weight}, {self.car_type}"

    def __str__(self):
        return f"Car Code: {self.car_code}\nCar Name: {self.car_name}\nCapacity: {self.car_capacity}\nHorsepower: " \
               f"{self.car_horsepower} hp\nWeight: {self.car_weight} KG\nType: {self.car_type}"

    # Method to check probationary licence
    def probationary_licence_prohibited_vehicle(self):
        hp = round((float(self.car_horsepower) / float(self.car_weight)) * 1000)
        # print(self.car_horsepower)
        # print(self.car_weight)
        #
        # print(hp)
        if hp > 130:
            return False
        else:
            return True
        # pass

    def found_matching_car(self, search_car_code):
        if self.car_code == search_car_code:
            return True
        else:
            return False

    def get_car_type(self):
        return self.car_type

# Test Data check
# print("car object")

# Checks the validity of the car_code using regular expressions before setting the attributes
# if not re.match(r'^[A-Z]{2}\d{6}$', car_code):
# raise ValueError("The car code format is invalid, please enter in this format:MB456666")

# Checks the validity for the car_type before setting the attributes
# if car_type not in ["FWD", "RWD", "AWD"]:
# raise ValueError("Please enter valid car type among : FWD, RWD, AWD")

# test = Car("AM452466", "SKODA", 6, 130, 700, "AWD")
# print(test)
# print(test.probationary_licence_prohibited_vehicle())
# print(test.found_matching_car("AM452466"))
# print(test.get_car_type())
# pass
