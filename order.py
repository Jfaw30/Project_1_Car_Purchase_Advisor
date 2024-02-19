import random
# coding: utf-8

__author__ = "Sachin Shivaramaiah"
__creation_date__ = "9th September"
__last_modified_date__ = "25th September"

import datetime

class Order:
    def __init__(self, order_id=None, order_car=None, order_retailer=None, order_creation_time=None):
        self.order_creation_time = int(datetime.datetime.now().timestamp())
        self.order_id = self.generate_order_id(order_car.car_code)
        self.order_car = order_car
        self.order_retailer = order_retailer

    def __str__(self):
        return f"{self.order_id}, {self.order_car.car_code}, {self.order_retailer.retailer_id}, " \
               f"{self.order_creation_time}"

    def generate_order_id(self, car_code):
        str_1 = "~!@#$%^&*"  # set of special characters used for ID generation

        # Random generation of 6 lower case alphabets
        random_letter = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=6))

        capital_string = ""  # empty string to store capital strings

        # for each index in the random letter
        for i, char in enumerate(random_letter):

            if (i + 1) % 2 == 0:  # even indexes are considered
                capital_string += char.upper()  # even indexes are converted into uppercase
            else:
                capital_string += char

        # Now to generate order id according to functionality, result_string with upper case letter are considered.
        result_string = capital_string

        # for each index of character in the capital_string
        for i, char in enumerate(capital_string):

            # ord Functions assigns the capital string with ascii values
            ascii_values = ord(char)

            # inorder to pick the index from the str_1 special character
            index_of_str_1 = (ascii_values ** 2) % len(str_1)

            # Index picked and character loaded
            outcome_of_str1 = str_1[index_of_str_1]

            # Appending final id to result_string for i+1 times
            result_string += outcome_of_str1 * (i + 1)

        # final appending of car_code with time stamp to the above result_string
        result_string += car_code + str(self.order_creation_time)

        return result_string
