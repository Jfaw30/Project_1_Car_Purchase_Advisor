# coding: utf-8

__author__ = "Sachin Shivaramaiah"
__creation_date__ = "9th September"
__last_modified_date__ = "25th September"


import random


class Retailer:

    def __init__(self,
                 retailer_id=-1,
                 retailer_name="First Name Last Name"):

        self.retailer_id = retailer_id
        self.retailer_name = retailer_name

    def __str__(self):
        return f"Retailer ID: {self.retailer_id}\nRetailer Name: {self.retailer_name}\n"

    def generate_retailer_id(self, list_retailer):
        current_list = list_retailer
        # present_list = [self.retailer_id for retailer in list_retailer]  # List comprehension

        while True:
            generated_id = random.randint(10000000, 99999999)
            if generated_id not in current_list:
                self.retailer_id = generated_id
                break

# Test Data Check
# test1 = Retailer(12344444, "Grocery house")
# test2 = Retailer(12348444, "Grocery hpuse")

# list_retailer = [test1, test2]

# test3 = Retailer(12348444, "Grocery hpwse")
# test3.generate_retailer_id(list_retailer)

# print(test1)
# print(test2)
# print(test3)
# Checks the validity of the retailer_id using regular expressions before setting the attributes
# if not re.match(r'^\d{8}$', str(retailer_id)):
# raise ValueError("Please Enter valid retailer ID with with 8 digits")

# Checks the validity of the retailer name using regular expressions before setting the attributes
# if not re.match(r'^[a-zA-Z\s]*$', retailer_name):
# raise ValueError("Retailer Name can only consists of alphabets and white spaces")
# pass
