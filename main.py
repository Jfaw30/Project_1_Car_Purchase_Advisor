# coding: utf-8

__author__ = "Sachin Shivaramaiah"
__creation_date__ = "9th September"
__last_modified_date__ = "25th September"

# your imports go here
import random
import string
from car_retailer import CarRetailer
import re


def main_menu():
    # Main Interface with the User
    print("---------------------------------------")
    print("Main Menu: Select your preferred options:")
    print("_______________________________________")
    print("1.Look for the nearest car retailer")
    print("2.Get car purchase advice")
    print("3.Place a car order")
    print("4.Exit")


def generate_test_data():  # Used to generate test Data

    # Empty list to load retailer details
    entry_retailers = []

    # Retailer Details being loaded
    for stock in range(3):
        rid = generate_random_id()
        rna = random.choice(["KAR& CO", "RACE ID", "MAGC CO", "SUPA CO", "RIDE V8", "SPAR CO"])
        r_address = random.choice(["Oakleig Rd MEL", "SouthYa Rd MEL", "BlackBu Rd MEL", "Murrumb Rd MEL"])
        r_code = random.choice([" VIC3168", " VIC3172", " VIC3186", " VIC3187", " VIC3175", " VIC3148"])
        time = (10.9, 24.0)

        # Empty list to load car details
        entry_cars = []

        # Car details of a specific retailer being loaded inside the loop.
        for stock1 in range(4):
            cid = generate_random_id()
            cna = generate_random_name()
            seat = random.randint(1, 8)
            hp = random.randint(100, 200)
            weight = random.randint(1000, 1100)
            mode = random.choice(['FWD', 'RWD', 'AWD'])

            entry_cars.append([cid, cna, seat, hp, weight, mode])  # Car list being appended.

        entry_retailers.append([rid, rna, f"{r_address}, {r_code}", time, entry_cars])
        # retailer list being appended with car details at the end

    with open("stock1.txt", 'w', encoding="utf-8") as file:  # Write Operation
        for details in entry_retailers:
            rid, rna, r_address, time, entry_cars = details  # Unpacking the read Details
            car_details = [f"'{car_id}, {car_name}, {seat}, {hp}, {weight1}, {mode}'" for
                           car_id, car_name, seat, hp, weight1, mode in entry_cars]  # List comprehension
            car_str = ','.join(car_details)
            line = f"{rid}, {rna}, {r_address}, {time}, [{car_str}]"
            # splitting and concatenation of the read details into the file
            file.write(line + '\n')


def generate_random_id():
    prefix = ''.join(random.choices(string.ascii_uppercase, k=2))
    return prefix + ''.join(random.choices(string.digits, k=6))
    # Buffer car_id generation for the test file.


def generate_random_name():
    c_name = ["Ferrari ", "Suzukii ", "Hondarr ", "Maserat ", "Mazdala ", "Fordeco ", "TeslaXY ", "Hyundai "]
    c_type = ["Premium", "Class A", "Class B", "Class C", "Sportty", "Cruiser", "Ecospor"]
    return random.choice(c_name) + ''.join(random.choice(c_type))
    # Buffer car_name and car_type generation for the test file.


def generate_random_rid():
    return ''.join(random.choices(string.digits, k=8))
    # Buffer random retailer id for test file.


def main():
    generate_test_data()

    retailer_list = []

    # Reading from stock1.txt

    with open("stock1.txt", 'r') as file:  # reading the generated test file

        # Conversion of all lines in file to a list of lines
        lines = file.readlines()
        for line in lines:
            data = line.strip().split(", ")  # strip removes white spaces split lines by ', ' to form data
            rid = data[0]
            rna = data[1]
            r_address = data[2]
            r_code = data[3]
            r_address = r_address + "," + r_code  # Split address and code are being read as one

            pattern_parentheses = r'\((.*?)\)'  # regx to identify time parentheses
            match_parentheses = re.search(pattern_parentheses, line)

            if match_parentheses:  # if match found
                # searched pattern is split and stored to match_parentheses
                b_time = match_parentheses.group(1).split(", ")  # Data gets separated at ', '

            # pattern match to read car details.
            pattern = r'\[(.*?)\]'
            match = re.search(pattern, line)
            if match:
                extracted_data = match.group(1)

                # Strips white space and split \' the extracted data into a list
                extracted_list = [item.strip() for item in extracted_data.split('\'')]
            else:
                print("No match found.")

            car_info_list = extracted_list

            # Cleaning or Removing unwanted read characters from the car info list
            car_obj_list = []  # List to keep clean data of car details
            for i in car_info_list:
                if i not in ["", ",", " "]:
                    car_obj_list.append(i)

            # Creation of instance of CarRetailer class object to a retailer list
            car_retailer = CarRetailer(retailer_id=rid, retailer_name=rna, car_retailer_address=r_address,
                                       car_retailer_business_hours=b_time,
                                       car_retailer_stock=car_obj_list)

            # Retail ID generation on car_retailer object to ensure uniqueness
            car_retailer.generate_retailer_id(retailer_list)

            # Created car_retailer object is now successfully loaded into the retailer_list
            retailer_list.append(car_retailer)
            # print(retailer_list[0].get_business_hours())

            # New list to streamline car details with respective retailers.
            new_data = []

            # Outer loop itterates over each index or retailer in the retailer_list
            for retailer in retailer_list:
                car_str_arr = []  # New list to store processed car data

                # The inner loop itterates each car_values in the car_retailer_stock and is printed by calling the __str__
                for car_values in retailer.car_retailer_stock:
                    car_str_arr.append(car_values.filestr())

                # Now the fresh aligned [list of [list]] data is being assigned to a variable.
                result_1 = [retailer.retailer_id,
                            retailer.retailer_name,
                            retailer.car_retailer_address,
                            tuple([float(retailer.car_retailer_business_hours[0]),
                                   float(retailer.car_retailer_business_hours[1])]),
                            car_str_arr
                            ]

                # Finally the structured data of individual retailer is now present in the new_data list
                if result_1 is not None:
                    new_data.append(result_1)

    # Writing processed data into the stock txt file
    with open("stock1.txt", 'w') as file2:

        # Outer loop itterates through each details in the new_data list which will be assigned to a line of strings
        for details in new_data:
            line = ""

            # Inner loop getting access to the index of each word in details list using enumerate
            for index, words in enumerate(details):

                # each word in details list is being converted into string and are being appended to line with commas
                if index == len(details) - 1:
                    line = line + str(words)
                else:
                    line = line + str(words) + ", "

            file2.write(line + '\n')

    while True:
        main_menu()

        try:
            print("---------------------------------")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                inner_loop2 = True
                while inner_loop2:  # To validate the input
                    try:
                        input_code = input("Enter the post code 'Ex 3174' or Type `exit` to go to previous menu  :  ")
                        if str(input_code) == "exit":
                            break
                        else:
                            if len(input_code) != 4 and len(input_code) <= 4:
                                print("Please enter 4 digits to search")
                                continue
                            else:
                                input_code = int(input_code)

                        nearest_retailer = None
                        smallest_distance = float('inf')
                        for retailer in retailer_list:
                            distance = retailer.get_postcode_distance(input_code)
                            if distance is not None and distance < smallest_distance:
                                smallest_distance = distance
                                nearest_retailer = retailer

                        if nearest_retailer:
                            print("_______________________________________")
                            print(
                                f"The nearest car retailer to your location is: {nearest_retailer.retailer_name} at "
                                f"{nearest_retailer.car_retailer_address}")
                            inner_loop2 = False
                        else:
                            print("No retailers found.")
                    except:
                        print("Retry with a different code")

            elif choice == 2:

                print("Current Available Retailer Details.")

                current_objects = [retailer.retailer_name for retailer in retailer_list]

                print(f"Retailer Name\tRetailer ID \tRetailer Address\t ")
                for index, retailer_object in enumerate(retailer_list,

                                                        1):  # iterate through list along with access to index

                    print(f"{index}.\t{retailer_object.retailer_name},\t"
                          f"{retailer_object.retailer_id},\t"
                          f"{retailer_object.car_retailer_address}")  # format string

                    # print(f"{index}. {retailer_object.retailer_id}") #List of objects

                choice2 = int(input("Enter your choice of retailer ID: "))

                if choice2 < 1 or choice2 > len(current_objects):
                    print("Invalid retailer ID. Please choose a valid option.")

                    continue

                inner_loop = True
                while inner_loop:
                    current_car_obj = retailer_list[choice2 - 1]
                    print("_______________________________________")
                    print("Select the options below:")
                    print("1. Recommend a car")
                    print("2. Get all cars in stock")
                    print("3. Get cars in stock by car types eg [AWD,FWD,RWD]")
                    print("4. Get probationary licence permitted cars in stock")
                    print("5. Get car by your licence type, L, P, Full")
                    print("6. Return to previous menu")

                    choice2_inner = input("Enter your choice: ")

                    try:
                        if choice2_inner == "1":
                            print("_______________________________________")
                            print(f"\nHere is the recommended car for the selected retailer \n"
                                  f"Selected Retailer Name: {current_car_obj.retailer_name} \n"
                                  f"Selected Retailer ID: {current_car_obj.retailer_id}")
                            print(current_car_obj.car_recommendation())
                            print("\n -------------------")

                        elif choice2_inner == "2":
                            print("_______________________________________")
                            print(f"\nHere is the of stock available cars for the selected retailer:")
                            all_cars = current_car_obj.get_all_stock()
                            print(f"Selected Retailer Name:{current_car_obj.retailer_name}\n"
                                  f"Selected Retailer ID:{current_car_obj.retailer_id}\n")

                            for index, car in enumerate(all_cars, 1):
                                if car.probationary_licence_prohibited_vehicle():
                                    plpv = "Approved"
                                else:
                                    plpv = "Not Probationary"
                                print(
                                    f"{index}. "
                                    f" Car Name:{car.car_name} | Car capacity seats: {car.car_capacity} |"
                                    f" Car Horsepower:{car.car_horsepower}hp | Car weight: {car.car_weight}kg |"
                                    f" Car Type: {car.car_type} |"
                                    f" probationary licence: {plpv}")

                            print("\n -------------------")

                        elif choice2_inner == "3":
                            while True:
                                car_type = input(f"Enter car type “AWD”, “RWD” or any other else Type exit to "
                                                 f"return to previous menu: ").upper()
                                if car_type == "EXIT":
                                    break
                                # Validate the input
                                if car_type not in ["AWD", "RWD", "FWD"]:
                                    print("Invalid car type. Please enter “AWD”, “RWD”, or “FWD”.")
                                    continue  # this will make the loop prompt the user again

                                filtered_cars = current_car_obj.get_stock_by_car_type([car_type])
                                if not filtered_cars:  # If the list is empty
                                    print(f"No cars available of type: {car_type}. Please try another type.")
                                    continue
                                print("_______________________________________")
                                print(f"Available cars of type: {car_type}")
                                for index, car in enumerate(filtered_cars, 1):
                                    print(f"{index}. {car.car_name}")
                                print("_______________________________________")
                                break

                        elif choice2_inner == "4":
                            print("Available probationary licence cars")
                            count = 0
                            for index, car in enumerate(current_car_obj.car_retailer_stock, 1):
                                if car.probationary_licence_prohibited_vehicle():
                                    print(f"{index}. {car.car_name}")
                                    count += 1
                            if count == 0:
                                print(f"The stock is 0 for probationary licence vehicle for this retailer\n"
                                      f" Retailer Name: {current_car_obj.retailer_name}\n"
                                      f" Retailer ID: {current_car_obj.retailer_id}")
                        elif choice2_inner == "5":
                            print("Enter you licence type to view cars, eg L, P, full")
                            licence_type = input("Enter your licence type here: ").upper()
                            values = current_car_obj.get_stock_by_licence_type(licence_type)
                            for index, car_retailer in enumerate(values, 1):
                                print(f"{index}. {car_retailer.car_name}")

                        elif choice2_inner == "6":
                            inner_loop = False

                        else:
                            print("Invalid choice. Please select a valid option.")

                    except Exception as e:
                        print(f"An error occurred: {e}")

            elif choice == 3:
                while True:  # This loop will ensure that the user keeps providing input until it's valid
                    retailer_input = input("Enter retailer ID and car ID separated by a space: ")

                    try:
                        # Split the input into two parts
                        part1, part2 = retailer_input.split()

                        # Check if part1 is all digits
                        if not part1.isdigit():
                            raise ValueError("The first part of the input should be all digits.")

                        # Check if part2 starts with two alphabets followed by numbers
                        if not (part2[:2].isalpha() and part2[2:].isdigit()):
                            raise ValueError(
                                "The second part of the input should start with two letters followed by numbers.")

                        # If the input is valid, proceed to processing it
                        retailer_id = int(part1)
                        car_id = part2

                        # Get the relevant retailer
                        current_retailer = next(
                            (retailer for retailer in retailer_list if retailer.retailer_id == retailer_id), None)

                        if not current_retailer:
                            print("Retailer not found!")
                            continue

                        # Create the order
                        order = current_retailer.create_order(car_id)

                        if order:
                            print("\nOrder successfully placed:")
                            print(order)

                        else:
                            print("\nOrder could not be placed.")
                        break  # Exit the loop if all operations are successful

                    except ValueError as e:
                        print(e)
                        continue

            elif choice == 4:
                print("Thank you for using our service")
                break

            else:
                print("Invalid main menu choice. Please select a valid option.")

        except ValueError:
            print("------------------------------------------------------------------")
            print("Invalid input. Please enter a number by looking at the below menu.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
