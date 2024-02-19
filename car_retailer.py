# coding: utf-8

__author__ = "Sachin Shivaramaiah"
__creation_date__ = "9th September"
__last_modified_date__ = "25th September"

from retailer import Retailer
from car import Car
import re
import random
import datetime
from order import Order


# path = "stock.txt"


# Multiple Inheritance inherits retailer class and car class
class CarRetailer(Retailer, Car):
    list_retailer_id = []  # Class level variable shared by all instances of the class

    def __init__(self, retailer_id=-1, retailer_name=None, car_retailer_address=" ",  # Car Retailer Class Constructor
                 car_retailer_business_hours=None,
                 car_retailer_stock=None):
        super().__init__(retailer_id, retailer_name)  # Initializing base class constructor

        # Processing car details by iterating through each entry separated by ,
        values_car_arr = []
        for values in car_retailer_stock:
            arr = values.split(",")
            car_obj = Car(*arr)
            values_car_arr.append(car_obj)  # car object now appended to values_car_arr

        # Assigning class attribute car_retailer_stock with car object (instance variable)
        self.car_retailer_stock = values_car_arr
        self.car_retailer_business_hours = car_retailer_business_hours
        self.car_retailer_address = car_retailer_address

        # self.generate_retailer_id(CarRetailer.list_retailer_id)
        # CarRetailer.list_retailer_id.append(self.retailer_id)

    # __str__ representation of retailer class and car class stored to a variable
    def __str__(self):
        car_retailer_info = super().__str__()
        car_retailer_info += f", {self.car_retailer_address}, {self.car_retailer_business_hours}"  # appending

        # when not empty, concatenate retailer details and car details (comprehensive string representation)
        if self.car_retailer_stock:
            # convert each item into string separated by ,
            car_stock = ", ".join(map(str, self.car_retailer_stock))
            car_retailer_info += f", {car_stock}"

        return car_retailer_info  # combined information

    # def getbussiness_hours(self):
    #     print(self.car_retailer_business_hours)

    # Loading stock details from the txt file
    def load_current_stock(self, stock_path="stock1.txt"):
        if not self.retailer_id:  # Checking for retailer ID
            print("Retailer ID is not set.")
            return

        with open(stock_path, "r") as file:  # Read operation on the file
            lines = file.readlines()
            extracted_list = []

        for line in lines:  # going through each line of the file
            data = line.strip().split(", ")

            if data[0] == str(self.retailer_id):  # Checks for matching retailer ID

                # if matched updates the retailer data from the list
                self.retailer_name = data[1]
                self.car_retailer_address = data[2] + ", " + data[3]

                pattern_parentheses = r'\((.*?)\)'  # regx for business hours
                match_parentheses = re.search(pattern_parentheses, line)

                if match_parentheses:
                    value = match_parentheses.group(1).split(", ")
                    self.car_retailer_business_hours = str(tuple([value[0], value[1]]))

                pattern = r'\[(.*?)\]'  # regx for car details inside []
                match = re.search(pattern, line)
                if match:
                    extracted_data = match.group(1)
                    # Split the extracted data into a list
                    extracted_list = [item.strip() for item in extracted_data.split('\'')]
                else:
                    print("No match found.")

                car_info_list = extracted_list  # current data now loaded to car_info_list

                self.car_retailer_stock = []  # Initialize as an empty list

                # extracting from car_info_list car attributes assigned to a new car object
                for car_info in car_info_list:
                    if car_info and car_info not in [',', ', ', '']:
                        car_data = car_info.split(", ")
                        car_code = car_data[0]
                        car_name = car_data[1]
                        car_capacity = car_data[2]
                        car_horsepower = int(car_data[3].strip())
                        car_weight = int(car_data[4].strip())
                        car_type = car_data[5]

                        car_obj = Car(car_code, car_name, car_capacity, car_horsepower, car_weight, car_type)
                        self.car_retailer_stock.append(car_obj)  # current data now in car_retailer_stock

                return

    def is_operating(self, cur_hour):
        try:
            # List comprehension converts each value in the list to float separated by ,
            start_hr, end_hr = [float(x) for x in self.car_retailer_business_hours.strip("[]").split(",")]
            if start_hr <= float(cur_hour) <= end_hr:
                return False
        except (ValueError, IndexError, AttributeError):
            return True

    def get_all_stock(self):
        return self.car_retailer_stock  # Returns the updated or present stock

    def extract_postcode(self):
        postcode = re.search(r'VIC(\d+)', self.car_retailer_address)
        # Regx to extract post code from the retailer address
        if postcode:
            return int(postcode.group(1))
        else:
            return None

    # Returns difference between retailer post code and user post code
    def get_postcode_distance(self, user_post_code):
        retailer_postcode = self.extract_postcode()
        if retailer_postcode:  # validity check
            return abs(user_post_code - retailer_postcode)
        else:
            return None

    def remove_from_stock(self, car_code):

        if not self.retailer_id:  # if retailer ID is not set
            return False

        # Read the updated information from stock.txt file
        with open("stock1.txt", "r") as file:
            lines = file.readlines()

        for line in lines:  # Reading lines
            data = line.strip().split(", ")
            if data[0] == str(self.retailer_id):  # Check for retailer id match

                self.retailer_name = data[1]
                self.car_retailer_address = data[2] + ", " + data[3]

                pattern_parentheses = r'\((.*?)\)'
                match_parentheses = re.search(pattern_parentheses, line)

                if match_parentheses:
                    value = match_parentheses.group(1).split(", ")
                    self.car_retailer_business_hours = str(tuple([value[0], value[1]]))

                pattern = r'\[(.*?)\]'
                match = re.search(pattern, line)
                if match:
                    extracted_data = match.group(1)
                    # Split the extracted data into a list
                    extracted_list = [item.strip() for item in extracted_data.split('\'')]
                else:
                    print("No match found.")

                car_info_list = extracted_list

                car_codes = []
                car_info_data = []

                # Data Filtering

                for car_info in car_info_list:
                    if car_info and car_info not in [',', ', ', '']:
                        car_info_data.append("'" + str(car_info) + "'")
                        car_data = car_info.split(", ")
                        car_codes.append(car_data[0])  # car codes extracted and stored

                # Replacing everything other than car_code
                add_list = []
                for i in extracted_list:
                    if i and i not in [',', ', ', ''] and i.split(", ")[0] not in [car_code]:
                        add_list.append(i)

                # Rewrite everything to the stock file
                with open("stock1.txt", "r") as file:
                    lines = file.readlines()

                output_lines = []

                for line in lines:
                    data = line.strip().split(", ")

                    if data[0] == str(self.retailer_id):
                        modified_line = re.sub(r'\[.*?\]', str(add_list), line)
                        output_lines.append(modified_line)
                    else:
                        output_lines.append(line)

                # Write the modified lines to a new file
                with open("stock1.txt", "w") as output_file:
                    output_file.writelines(output_lines)
                return True
            else:
                return False

    def add_to_stock(self, car):
        pass

    # returns matched type by checking the current car_retailer_stock
    def get_stock_by_car_type(self, car_types):
        matched_type = []
        for car in self.car_retailer_stock:
            if car.car_type in car_types:
                matched_type.append(car)
        return matched_type

    # Filters car based on licence type
    def get_stock_by_licence_type(self, licence_type):
        if licence_type == "P":  # Probationary Licence
            return [car for car in self.car_retailer_stock if not car.probationary_licence_prohibited_vehicle()]
        elif licence_type in ["L", "FULL"]:  # Learner Licence or Full Licence
            return [car for car in self.car_retailer_stock if car.probationary_licence_prohibited_vehicle()]
        else:
            print(f"Invalid licence type: {licence_type}")
            return []

    def car_recommendation(self):
        return random.choice(self.car_retailer_stock)  # random car selection from the current stock

    def create_order(self, car_code):

        # matching user input car code with the current car_retailer_stock
        car = next((car for car in self.car_retailer_stock if car.car_code == car_code), None)

        if not car:
            print("Car not found in stock.")
            return

        # Check if within business hours
        current_hour = 22
        if not self.is_operating(current_hour):
            print("Cannot place order outside of business hours.")
            return

        # Creating instance of order class and passing the parameters
        order = Order(order_car=car, order_retailer=self)

        # appending the order file with the updated details
        with open("order.txt", "a") as file:
            file.write(str(order) + "\n")

        # Remove selected car code from the stock
        self.remove_from_stock(car_code)

        # After removing the current stock is reloaded
        self.load_current_stock("stock1.txt")

        return order
