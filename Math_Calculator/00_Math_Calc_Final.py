# imports go here
import math
import pandas
from tabulate import tabulate
from datetime import date

# definitions go here
def statement(txt, decor):
    """returns a fancy statement with the inputted txt and decorations"""
    return f"{decor * 3} {txt} {decor * 3}"


def yes_no(question):
    """this function makes users say yes or no to a question"""

    error = "please answer with yes/no"
    # loops code until user enters a valid answer
    while True:
        # ask user answer your yes no question
        response = input(question).lower()

        # lists of valid responses
        yes_list = ['yes', 'y']
        no_list = ['no', 'n']

        # if they answer yes it returns yes
        if response in yes_list:
            return "yes"

        # if they answer no it returns no
        elif response in no_list:
            return "no"

        # if they did not enter yes or no it tells them to and then loops the code
        else:
            print(error)


def pick_shape(question, shapes_list):
    """ This function makes users pick a shape from a list"""

    # error message for if they don't select a valid
    error = f"please enter a valid shape {shapes_list}"

    # while loop to keep asking what shape they want if they don't enter a valid ans
    while True:
        # asks user what shape they want
        choice = input(question).lower()

        if choice in shapes_list:
            return choice

        else:
            if choice == "xxx":
                return choice

            print(error)


def float_check(num):
    """ this function checks if a variable is a float """
    try:
        float(num)

        return "float"

    except ValueError:
        return "not float"


def string_check(question, valid_ans_list, num_letters=1):
    """checks a user"""
    error = f"""
Please choose an option from {valid_ans_list}
    """

    while True:
        response = input(question).lower()

        for ans in valid_ans_list:

            if response == ans:
                return ans

            elif response == ans[:num_letters]:
                return ans

        # if response is not the word / first few letters, output an error
        print(error)


def pick_list(question, valid_ans_list):
    """ this function makes users pick an option from a list """
    # error message to display if the user inputs and invalid response
    error = f"Please enter valid units {valid_ans_list}"

    # while to keep asking until user enters a valid ans
    while True:
        # find user choice
        choice = input(question).lower()

        # if user picks a valid ans
        if choice in valid_ans_list:
            return choice

        #if user enters an invalid ans
        else:
            print(error)


def find_dimension(question):
    """ this function finds a dimension """
    # list of valid units
    valid_units = ["millimeters", "centimeters", "meters", "mm", "cm", "m"]

    # while to make sure the user enters a dimension equal to or less than 9 m
    while True:
        # error message for if they enter an invalid ans
        error = "Please enter a valid number"

        # while to keep asking what the dimension is if they don't enter a valid integer
        while True:
            # finds what the distance is
            dimension = input(question)

            # tests if it is a float
            dimension_float = float_check(dimension)

            # if entered value is not a float
            if dimension_float == "not float":
                print(error)

            # if entered value it a float continue with the code
            else:
                dimension = float(dimension)

                if dimension <= 0:
                    print(error)

                else:
                    break

        # error message for if they enter an invalid ans
        error = f"Please enter a valid unit: {valid_units}"

        # while true to keep asking the units until they enter a valid ans
        while True:
            # asks for units
            units = pick_list("what units of measurements is this length?", valid_units)

            # if they enter valid units
            if units in valid_units:
                break

            # if they don't enter valid units
            else:
                print(error)

        if units == "mm" or "millimeters" and dimension <= 9000:
            break

        elif units == "cm" or "centimeters" and  dimension <= 900:
            break

        elif units == "m" and dimension <= 9:
            break

        else:
            print("please enter a value less than 9000mm (900cm, 9m)")

    return dimension, units


def convert_mm(value, current_unit):
    """this function converts values from cm, m and km to mm"""
    if current_unit == "mm" or "millimeters":
        value = value

    elif current_unit == "cm" or "centimeters":
        value *= 10

    else:
        value *= 1000

    return float(value)


def round_2dp(value):
    """ This function checks if a value is a float and if it is it rounds it to 2dp """
    # try except to check if it is a float
    try:
        value = float(value)

        # if value is float round to 2dp
        value = round(value, 2)
        return value

    except ValueError:
        return value


def add_mm_pwr(old_list, power):
    """ this function adds 'mm' or 'mm^2' to the end of every value/string in a list"""
    new_list = []

    for value in old_list:
        if value != "NA":
            if power == 1:
                new_list.append(f"{value}mm")

            else:
                new_list.append(f"{value}mm\u00b2")

        else:
            new_list.append(value)

    # return the new version of the list
    return new_list


# main routine goes here
# initialize variables
# 2d variables
# variable lists
shapes = []
dimension_2d1 = []
dimension_2d2 = []
dimension_2d3 = []
areas = []
perimeters = []

# other variables
pi = math.pi

# setting values to "" so they cannot be undefined
shapes_string = ""
shapes_frame = ""

# print the title/welcome message
header_txt = "welcome to 2d shapes calculator"
print(statement(header_txt, "*"), "\n")
# ask if the user wants to see the instructions
instructions_yn = yes_no("Would you like to read the instructions? ")

# if the user wants to se the instructions print them here
if instructions_yn == "yes":
    print("""
    *** Instructions ***
    
    This is 2d shapes calculator where you can find the area and perimeter of your 2d shapes
    
    You will need to select what shape you are calculating area nd perimeter for.
    You can chose from these options rectangle, circle or triangle.
    
    You will then have to chose your known dimension if this option comes up.
    Then you will have to enter your value for distance. then add your units.
    """)

else:
    print()

# while loop to go back to the start if the user accidentally enters 'xxx'
while True:
    # while loop to keep asking for 2d shapes until user enters 'xxx'
    while True:
        # ask what shape they would like to find the area and perimeter for
        shape = string_check("Which shape would you like to calculate area and perimeter for? ",
                           ["rectangle", "circle", "triangle", "xxx"])
        print()

        # set dimensions to "NA"
        dimension_1 = "NA"
        dimension_2 = "NA"
        dimension_3 = "NA"

        # if user enters 'xxx' break while loop
        if shape == "xxx":
            break

        # append chosen shape to a list
        shapes.append(shape)

        # if user choose square
        if shape == "rectangle":
            # ask for dimensions and values
            dimension_1 = find_dimension("What is the length of the rectangle? ")
            dimension_2 = find_dimension("What is the width of the rectangle? ")
            print()

            # Convert length values to mm
            dimension_1 = convert_mm(dimension_1[0], dimension_1[1])
            dimension_2 = convert_mm(dimension_2[0], dimension_2[1])

            # calculate area and perimeter
            area = dimension_1 * dimension_2
            perimeter = 2 * dimension_1 + 2 * dimension_2

        # if user chose circle
        elif shape == "circle":
            known_dimensions_list = ["diameter", "radius", "circumference"]
            known_len = string_check("what is the known dimension? ", known_dimensions_list)
            print()

            # if known dimension is diameter
            if known_len == "diameter":
                # ask for dimensions and values
                dimension_1 = find_dimension("what is the diameter or the circle? ")
                print()

                # covert to millimeters
                dimension_1 = convert_mm(dimension_1[0], dimension_1[1])

                # calculate the sa & perimeter
                area = pi * (dimension_1 / 2) ** 2
                perimeter = 2 * pi * (dimension_1 / 2)

            # if known dimension is radius
            elif known_len == "radius":
                # ask for dimensions and values
                dimension_1 = find_dimension("what is the radius or the circle? ")
                print()

                # covert to millimeters
                dimension_1 = convert_mm(dimension_1[0], dimension_1[1])

                # calculate the sa & perimeter
                area = pi * dimension_1 ** 2
                perimeter = 2 * pi * dimension_1

            # if known dimension is circumference
            else:
                # ask for dimensions and values
                dimension_1 = find_dimension("what is the circumference or the circle? ")
                print()

                # covert to millimeters
                dimension_1 = convert_mm(dimension_1[0], dimension_1[1])

                # calculate the area and perimeter
                area = pi * (dimension_1 / (2 * pi)) ** 2
                perimeter = dimension_1

        # if user chose triangle
        else:
            # list of valid types of triangles
            tri_types = ["right angle", "equilateral", "scalene", "isosceles"]

            # ask user what type of triangle they are calculating area and perimeter for
            tri_type = string_check("What type of triangle are you calculating area and perimeter for? ", tri_types)
            print()

            # if user picks right angle
            if tri_type == "right angle":
                # gets base length and height
                dimension_1 = find_dimension("what is the length of the base of the triangle? ")
                dimension_2 = find_dimension("What is the height of the triangle? ")
                print()

                # convert values to mm
                dimension_1 = convert_mm(dimension_1[0], dimension_1[1])
                dimension_2 = convert_mm(dimension_2[0], dimension_2[1])

                # calculate area and perimeter
                area = 0.5 * dimension_1 * dimension_2
                perimeter = dimension_1 + dimension_2 + (dimension_1 ** 2 + dimension_2 ** 2) ** 0.5

            # if user picks equilateral
            elif tri_type == "equilateral":
                # gets sides length
                dimension_1 = find_dimension("What is the length of the sides of the triangle? ")
                print()

                # convert values to mm
                dimension_1 = convert_mm(dimension_1[0], dimension_1[1])

                # calculate area
                area = ((3 ** (1/2)) / 4) * (dimension_1 ** 2)

                # calculate perimeter
                perimeter = dimension_1 * 3

            # if user picks scalene
            elif tri_type == "scalene":
                # gets sides length
                dimension_1 = find_dimension("What is the length of the first side of the triangle? ")
                dimension_2 = find_dimension("What is the length of the second side of the triangle? ")
                dimension_3 = find_dimension("What is the length of the third side of the triangle? ")
                print()

                # convert values to mm
                dimension_1 = convert_mm(dimension_1[0], dimension_1[1])
                dimension_2 = convert_mm(dimension_2[0], dimension_2[1])
                dimension_3 = convert_mm(dimension_3[0], dimension_3[1])

                # calculate area
                try:
                    s = (dimension_1 + dimension_2 + dimension_3) / 2
                    area = (s * (s - dimension_1) * (s - dimension_2) * (s - dimension_3)) ** 0.5
                    area = float(area)

                # if user enter values that cannot be a triangle
                except TypeError:
                    print("This is not a real triangle\n")
                    continue

                # calculate perimeter
                perimeter = dimension_1 + dimension_2 + dimension_3

            # if user picks isosceles
            else:
                # gets sides length
                dimension_1 = find_dimension("What is the length of the side of different length? ")
                dimension_2 = find_dimension("What is the length of the sides of the same length? ")
                print()

                # convert values to mm
                dimension_1 = convert_mm(dimension_1[0], dimension_1[1])
                dimension_2 = convert_mm(dimension_2[0], dimension_2[1])

                # calculate area
                height = (dimension_2 ** 2 - (dimension_1 / 2) ** 2) ** 0.5
                area = (height * dimension_1) / 2

                # calculate perimeter
                perimeter = dimension_1 + dimension_2 * 2

        # round all values to 2 dp
        dimension_1 = round_2dp(dimension_1)
        dimension_2 = round_2dp(dimension_2)
        dimension_3 = round_2dp(dimension_3)

        area = round_2dp(area)
        perimeter = round_2dp(perimeter)

        # print area and perimeter
        print(f"the area of your {shape} is {area}mm\u00b2")
        print(f"the perimeter of your {shape} is {perimeter}mm")
        print()

        # append dimensions to a list
        dimension_2d1.append(dimension_1)
        dimension_2d2.append(dimension_2)
        dimension_2d3.append(dimension_3)

        # append area and perimeter to a list
        areas.append(area)
        perimeters.append(perimeter)

    # if no 2d shape where entered ask user if they are sure they want no 2d shapes
    if len(shapes) <= 0:
        finished_2d = yes_no("Are you sure you have no shapes? ")

    else:
        finished_2d = yes_no("Are you sure you have no more shapes? ")

    print()

    # if user says yes break the while loop
    if finished_2d == "yes":
        break

# if there is 1 or more 2d shapes crate dictionary and frame
if len(shapes) >= 1:

    # add mm and mm^2
    dimension_2d1 = add_mm_pwr(dimension_2d1, 1)
    dimension_2d2 = add_mm_pwr(dimension_2d2, 1)
    dimension_2d3 = add_mm_pwr(dimension_2d3, 1)
    perimeters = add_mm_pwr(perimeters, 1)
    areas = add_mm_pwr(areas, 2)

    # creates dictionary
    shapes_dict = {
        'Shape': shapes,
        'Dimension 1': dimension_2d1,
        'Dimension 2': dimension_2d2,
        'Dimension 3': dimension_2d3,
        'Area': areas,
        'Perimeter': perimeters
    }

    # create frame
    shapes_frame = pandas.DataFrame(shapes_dict)

    shapes_string = tabulate(shapes_frame, headers='keys', tablefmt='psql', showindex=False)

# get current date for heading and file name
today = date.today()

# get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%y")

# make header here
header = statement(f"{header_txt} {day}/{month}/{year}", "*")

# make 2d shapes header
header_2d = statement("2d shapes", "-")

# print 2d shapes header
print(header_2d, "\n")

# set 2d results to "no 2d shapes were calculated"
if len(shapes) <= 0:
    result_2d = "no 2d shapes were calculated"

# set 2d result to the tabulated string
else:
    result_2d = shapes_string

# print the 2d result
print(result_2d, "\n\n")

# create file
file_name = "Math_Calc_Final_Output"
write_to = "{}.txt".format(file_name)
text_file = open(write_to, "w+")

# what to write to file list
to_write = [f"{header}\n", header_2d, f"{result_2d}\n\n", "thank you for using the geometry calculator"]

# write everything in the list to file
for item in to_write:
    text_file.write(item)
    text_file.write("\n")
