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
    error = "bad dont do that"

    # while to keep asking until user enters a valid ans
    while True:
        # find user choice
        choice = input(question)

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

    # error message for if they enter an invalid ans
    error = "Please enter a valid number"

    # while to make sure the user enters a dimension equal to or less than 9 m
    while True:
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
            units = pick_list("what units of measurements is this length", valid_units)

            # if they enter valid units
            if units in valid_units:
                break

            # if they don't enter valid units
            else:
                print(error)

        if units == "mm" and dimension <= 9000:
            break

        elif units == "cm" and  dimension <= 900:
            break

        elif units == "m" and dimension <= 9:
            break

        else:
            print("please enter a value less than 9000mm (900cm, 9m)")

    return dimension, units


def convert_mm(value, current_unit):
    """this function converts values from cm, m and km to mm"""
    if current_unit == "mm":
        value = value

    elif current_unit == "cm":
        value *= 10

    else:
        value *= 1000

    return int(value)


def yes(question, valid_ans):
    """ this function make users pick an option in a list """

    # error message to be displayed if the user enter an invalid ans
    error = f"please enter a valid ans {valid_ans}"

    # while true to keep asking until user enter a valid ans
    while True:
        # asks user what they chose
        ans = input(question)

        if ans in valid_ans:
            return ans

        else:
            print(error)


def add_mm(value):
    """ this function adds 'mm' to the end of a value/string """
    return f"{value}mm"


def add_mm2(value):
    """ this function adds 'mm^2' to the end of a value/string """
    return f"{value}mm\u00b2"


def add_mm3(value):
    """ this function adds 'mm^3' to the end of a value/string """
    return f"{value}mm\u00b3"


# main routine goes here
# initialize variables
# 2d variables
shapes_2d = []
dimension_2d1 = []
dimension_2d2 = []
dimension_2d3 = []
areas = []
perimeters = []
shapes_2d_string = ""

# 3d variables
shapes_3d = []
dimension_3d1 = []
dimension_3d2 = []
dimension_3d3 = []
surface_areas = []
volumes = []
shapes_3d_string = ""

# other variables
pi = math.pi

# print the title/welcome message
header_txt = "welcome to geometry calculator"
print(statement(header_txt, "*"), "\n")
# ask if the user wants to see the instructions
instructions_yn = yes_no("Would you like to read the instructions? ")

# if the user wants to se the instructions print them here
if instructions_yn == "yes":
    print("""
    *instructions go here*
    
    and something about only equilateral triangles for the base of the triangular based pyramid
    """)

else:
    print()

# ask the user if the want to find the information for any 2d shapes
shape_yn_2d = yes_no("do you have any 2D shape you would like calculate area and perimeter for? ")
print()
# if user picks yes run 2d code
if shape_yn_2d == "yes":
    # 2d code goes here
    # while loop to go back to the start if the user accidentally enters 'xxx'
    while True:
        # while loop to keep asking for 2d shapes until user enters 'xxx'
        while True:
            # ask what shape they would like to find the area and perimeter for
            shape = string_check("Which 2d shapes would you like to calculate area and perimeter for? ",
                               ["rectangle", "circle", "triangles", "xxx"])
            print()

            # set dimensions to "NA"
            dimension_1 = "NA"
            dimension_2 = "NA"
            dimension_3 = "NA"

            # if user enters 'xxx' break while loop
            if shape == "xxx":
                break

            # append chosen shape to a list
            shapes_2d.append(shape)

            # if user choose square
            if shape == "rectangle":
                # ask for dimensions and values
                length = find_dimension("What is the length of the rectangle? ")
                height = find_dimension("What is the height of the rectangle? ")
                print()

                # Convert length values to mm
                length = convert_mm(length[0], length[1])
                height = convert_mm(height[0], height[1])

                # calculate area and perimeter
                area = length * height
                perimeter = 2 * length + 2 * height

            # if user chose circle
            elif shape == "circle":
                known_dimensions_list = ["diameter", "radius", "circumference"]
                known_len = string_check("what is the known dimension? ", known_dimensions_list)
                print()

                # if known dimension is diameter
                if known_len == "diameter":
                    # ask for dimensions and values
                    diameter = find_dimension("what is the diameter or the circle? ")
                    print()

                    # covert to millimeters
                    diameter = convert_mm(diameter[0], diameter[1])
                    dimension_1 = diameter

                    # calculate the sa & perimeter
                    area = pi * (diameter / 2) ** 2
                    perimeter = 2 * pi * (diameter / 2)

                # if known dimension is radius
                elif known_len == "radius":
                    # ask for dimensions and values
                    radius = find_dimension("what is the radius or the circle? ")
                    print()

                    # covert to millimeters
                    radius = convert_mm(radius[0], radius[1])
                    dimension_1 = radius

                    # calculate the sa & perimeter
                    area = pi * radius ** 2
                    perimeter = 2 * pi * radius

                # if known dimension is circumference
                else:
                    # ask for dimensions and values
                    circumference = find_dimension("what is the circumference or the circle? ")
                    print()

                    # covert to millimeters
                    circumference = convert_mm(circumference[0], circumference[1])
                    dimension_1 = circumference

                    # calculate the area and perimeter
                    area = 2 * pi * (circumference / (2 * pi))
                    perimeter = circumference

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
                    s = (dimension_1 * 3) / 2
                    area = (s * 3 * (s - dimension_1)) ** 0.5

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
                    s = (dimension_1 + dimension_2 + dimension_3) / 2
                    area = (s * (s - dimension_1) * (s - dimension_2) * (s - dimension_3)) ** 0.5

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
                    s = (dimension_1 + dimension_2 * 2) / 2
                    area = (s * (s - dimension_1) * ((s - dimension_2) * 2)) ** 0.5

                    # calculate perimeter
                    perimeter = dimension_1 + dimension_2 * 2

            # round area and perimeter to 2 dp
            area = round(area, 2)
            perimeter = round(perimeter, 2)

            # print area and perimeter
            print(f"the area of this rectangle is {area}mm")
            print(f"the perimeter of this rectangle is {perimeter}mm")
            print()

            # append dimensions to a list
            dimension_2d1.append(dimension_1)
            dimension_2d2.append(dimension_2)
            dimension_2d3.append(dimension_3)

            # append area and perimeter to a list
            areas.append(area)
            perimeters.append(perimeter)

        # if no 2d shape where entered ask user if they are sure they want no 2d shapes
        finished_2d = yes_no("Are you sure you have no more 2d shapes? ")
        print()

        # if user says yes break the while loop
        if finished_2d == "yes":
            break

    # if there is 1 or more 2d shapes crate dictionary and frame
    if len(shapes_2d) >= 1:
        # creates dictionary
        shapes_2d_dict = {
            'Shape': shapes_2d,
            'Dimension 1': dimension_2d1,
            'Dimension 2': dimension_2d2,
            'Dimension 3': dimension_2d3,
            'Area': areas,
            'Perimeter': perimeters
        }

        # create frame
        shapes_2d_frame = pandas.DataFrame(shapes_2d_dict)

        # add mm
        add_millimeters = ['Dimension 1', 'Dimension 2', 'Dimension 3', 'Perimeter']
        add_millimeters_squared = ['Area']

        for var_item in add_millimeters:
            shapes_2d_frame[var_item] = add_mm(shapes_2d_frame[var_item])

        for var_item in add_millimeters_squared:
            shapes_2d_frame[var_item] = add_mm2(shapes_2d_frame[var_item])

        shapes_2d_string = shapes_2d_frame
        # shapes_2d_string = tabulate(shapes_2d_frame, headers='keys', tablefmt='psql', showindex=False)

# ask the user if the want to find the information for any 3d shapes
shape_yn_3d = yes_no("Do you have any 3d shapes you would like to calculate surface area and volume for? ")
print()

# if user picks yes run 3d code
if shape_yn_3d == "yes":
    # 3d code goes here
    # while loop to go back to the start if the user accidentally enters 'xxx'
    while True:
        # while loop to keep asking for 3d shapes until user enters 'xxx'
        while True:
            # ask what shape they would like to find the surface area and volume for
            shape = string_check("Which 3d shapes would you like to calculate surface area and volume for? ",
                               ["cuboid", "cylinder", "cone", "sphere", "pyramid", "xxx"])
            print()

            # if user enters 'xxx' break while loop
            if shape == "xxx":
                break

            # append chosen shape to a list
            shapes_3d.append(shape)

            # set dimensions to "NA" as a default
            dimension_1 = "NA"
            dimension_2 = "NA"
            dimension_3 = "NA"



            # if user choose cuboid
            if shape == "cuboid":
                # ask for dimensions and values
                dimension_1 = find_dimension("What is the length of the cuboid? ")
                dimension_2 = find_dimension("What is the height of the cuboid? ")
                dimension_3 = find_dimension("What is the width of the cuboid? ")
                print()

                # Convert length values to mm
                dimension_1 = convert_mm(dimension_1[0], dimension_1[1])
                dimension_2 = convert_mm(dimension_2[0], dimension_2[1])
                dimension_3 = convert_mm(dimension_3[0], dimension_3[1])

                # calculate area and perimeter
                sa = (dimension_1 * dimension_2 * 2) + (dimension_3 * dimension_2 * 2) + (dimension_3 * dimension_2 * 2)
                volume = dimension_1 * dimension_2 * dimension_3

            # if user picks cylinder
            elif shape == "cylinder":
                known_dimensions_list = ["diameter", "radius", "circumference"]
                known_len = string_check("what is the known dimension of the base? ", known_dimensions_list)
                print()

                # if known dimension is diameter
                if known_len == "diameter":
                    # ask for dimensions and values
                    dimension_1 = find_dimension("what is the diameter of the base? ")
                    print()

                    # covert to millimeters
                    dimension_1 = convert_mm(dimension_1[0], dimension_1[1])

                    # calculate the area and perimeter
                    area = pi * (dimension_1 / 2) ** 2
                    perimeter = 2 * pi * (dimension_1 / 2)

                # if known dimension is radius
                elif known_len == "radius":
                    # ask for dimensions and values
                    dimension_1 = find_dimension("what is the radius of the base? ")
                    print()

                    # covert to millimeters
                    dimension_1 = convert_mm(dimension_1[0], dimension_1[1])

                    # calculate the area and perimeter
                    area = pi * dimension_1 ** 2
                    perimeter = 2 * pi * dimension_1

                # if known dimension is circumference
                else:
                    # ask for dimensions and values
                    dimension_1 = find_dimension("what is the circumference or the base? ")
                    print()

                    # covert to millimeters
                    dimension_1 = convert_mm(dimension_1[0], dimension_1[1])

                    # calculate the area and perimeter
                    area = 2 * pi * (dimension_1 / (2 * pi))
                    perimeter = dimension_1

                # asks user for height
                height = find_dimension("what is the height of the cylinder? ")
                print()

                # convert height to mm
                height = convert_mm(height[0], height[1])

                # calculate sa & volume
                sa = area * 2 + perimeter * height
                volume = area * height

            # if user picks cone
            elif shape == "cone":
                known_dimensions_list = ["diameter", "radius", "circumference"]
                known_len = string_check("what is the known dimension of the base? ", known_dimensions_list)
                print()

                # if known dimension is diameter
                if known_len == "diameter":
                    # ask for dimensions and values
                    dimension_1 = find_dimension("what is the diameter of the base? ")
                    print()

                    # covert to millimeters
                    dimension_1 = convert_mm(dimension_1[0], dimension_1[1])

                    # calculate the area and perimeter
                    area = pi * (dimension_1 / 2) ** 2
                    perimeter = 2 * pi * (dimension_1 / 2)

                # if known dimension is radius
                elif known_len == "radius":
                    # ask for dimensions and values
                    dimension_1 = find_dimension("what is the radius of the base? ")
                    print()

                    # covert to millimeters
                    dimension_1 = convert_mm(dimension_1[0], dimension_1[1])

                    # calculate the area and perimeter
                    area = pi * dimension_1 ** 2
                    perimeter = 2 * pi * dimension_1

                # if known dimension is circumference
                else:
                    # ask for dimensions and values
                    dimension_1 = find_dimension("what is the circumference or the base? ")
                    print()

                    # covert to millimeters
                    dimension_1 = convert_mm(dimension_1[0], dimension_1[1])

                    # calculate the area and perimeter
                    area = 2 * pi * (dimension_1 / (2 * pi))
                    perimeter = dimension_1

                # asks user for height
                height = find_dimension("what is the height of the cone? ")
                print()

                # convert height to mm
                height = convert_mm(height[0], height[1])

                # find radius of cone
                r = perimeter / (2 * pi)

                # find slant height of cone
                s = ((r ** 2) + height ** 2) ** (1 / 2)

                # calculate sa & volume
                sa = pi * (r ** 2) + pi * r * s
                volume = (1/3) * height * (r ** 2)

            # if user picks sphere
            elif shape == "sphere":
                known_dimensions_list = ["diameter", "radius", "circumference"]
                known_len = string_check("what is the known dimension of the base? ", known_dimensions_list)
                print()

                # if known dimension is diameter
                if known_len == "diameter":
                    # ask for dimensions and values
                    dimension_1 = find_dimension("what is the diameter of the base? ")
                    print()

                    # covert to millimeters
                    dimension_1 = convert_mm(dimension_1[0], dimension_1[1])

                    radius = 0.5 * dimension_1

                # if known dimension is radius
                elif known_len == "radius":
                    # ask for dimensions and values
                    radius = find_dimension("what is the radius of the base? ")
                    print()

                    # covert to millimeters
                    radius = convert_mm(radius[0], radius[1])
                    dimension_1 = radius

                # if known dimension is circumference
                else:
                    # ask for dimensions and values
                    dimension_1 = find_dimension("what is the circumference or the base? ")
                    print()

                    # covert to millimeters
                    dimension_1 = convert_mm(dimension_1[0], dimension_1[1])
                    radius = dimension_1 / (2 * pi)

                # calculate sa & volume
                sa = 4 * pi * radius ** 2
                volume = (4 / 3) * pi * radius ** 3

            # if user picks pyramid
            else:
                # finds what shape the base of the pyramid is
                base = string_check("what shape is the base of the pyramid? ",
                                  ["square", "triangle"])
                print()

                # if user picks square
                if base == "square":
                    dimension_1 = find_dimension("What is the height of the pyramid? ")
                    dimension_2 = find_dimension("What is the width of the base? ")
                    print()

                    # convert dimensions to mm
                    dimension_1 = convert_mm(dimension_1[0], dimension_1[1])
                    dimension_2 = convert_mm(dimension_2[0], dimension_2[1])

                    # calculate area of the base
                    base_sa = dimension_2 * dimension_2

                    # find the slant height for the pyramid
                    s_height = ((0.5 * dimension_2) ** 2 + dimension_1 ** 2) ** 0.5

                    # calculate area of sides
                    s_area = s_height * 0.5 * dimension_2

                    # calculate total sa and volume
                    sa = base_sa + s_area * 4
                    volume = (dimension_2 ** 2) * (dimension_1 / 3)

                # if user picks triangle
                else:
                    # gets base length and height
                    dimension_1 = find_dimension("what is the length of the base of the base triangle? ")
                    dimension_2 = find_dimension("What is the height of the base triangle? ")
                    print()

                    # convert values to mm
                    dimension_1 = convert_mm(dimension_1[0], dimension_1[1])
                    dimension_2 = convert_mm(dimension_2[0], dimension_2[1])

                    # calculate area
                    s = (dimension_1 * 3) / 2
                    b_area = (s * 3 * (s - dimension_1)) ** 0.5

                    # calculate minimum distance between the edge of the base triangle to the centre
                    distance_to_centre = ((dimension_1 * (3 ** 0.5)) / 2) / 3

                    # calculate slant height
                    s_height = ((distance_to_centre ** 2) + (dimension_2 ** 2)) ** 1/2

                    # calculate the area of the side faces
                    s_area = (s_height * dimension_1) / 2

                    # calculate surface area
                    sa = b_area + (s_area * 3)

                    # calculate volume
                    volume = 1/3 * b_area * dimension_2

            # print sa and volume
            print(f"the surface area of your 3d shape is {sa}")
            print(f"the volume of your 3d shape is {volume}")

            # append dimensions to a list
            dimension_3d1.append(dimension_1)
            dimension_3d2.append(dimension_2)
            dimension_3d3.append(dimension_3)

            # append area and perimeter to lists
            surface_areas.append(sa)
            volumes.append(volume)

        # if no 3d shape where entered ask user if they are sure they want no 3d shapes
        finished_yn = yes_no("Are you sure you have no more 3d shapes")
        print()

        # if user says yes break the while loop
        if finished_yn == "yes":
            break

    # if there is 1 or more 3d shapes crate dictionary and frame
    if len(shapes_3d) >= 1:
        # creates dictionary
        shapes_3d_dict = {
            'Shape': shapes_3d,
            'Dimension 1': dimension_3d1,
            'Dimension 2': dimension_3d2,
            'Dimension 3': dimension_3d3,
            'Surface Area': areas,
            'Volume': perimeters
        }

        # create frame
        shapes_3d_frame = pandas.DataFrame(shapes_3d_dict)

        # add mm
        add_millimeters = ['Dimension 1', 'Dimension 2', 'Dimension 3', 'Perimeter']
        add_millimeters_squared = ['Surface Area']
        add_millimeters_cubed = ['Volume']

        for var_item in add_millimeters:
            shapes_3d_frame[var_item] = add_mm(shapes_3d_frame[var_item])

        for var_item in add_millimeters_squared:
            shapes_3d_frame[var_item] = add_mm2(shapes_3d_frame[var_item])

        for var_item in add_millimeters_cubed:
            shapes_3d_frame[var_item] = add_mm3(shapes_3d_frame[var_item])

        shapes_3d_string = tabulate(shapes_3d_frame, headers='keys', tablefmt='psql', showindex=False)

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
if len(shapes_2d) < 1:
    result_2d = "no 2d shapes were calculated"

# set 2d result to the tabulated string
else:
    result_2d = shapes_2d_string

# print the 2d result
print(result_2d, "\n\n")

# make 3d shapes header
header_3d = statement("3d shapes", "-")

# print 3d shapes header
print(header_3d, "\n")

# set 2d results to "no 3d shapes were calculated"
if len(shapes_3d) < 1:
    result_3d = "no 3d shapes were calculated"

# set 3d result to the tabulated string
else:
    result_3d = shapes_3d_string

# print the 3d result
print(result_3d, "\n\n")

# create file
file_name = "Math_Calc_Final_Output"
write_to = "{}.txt".format(file_name)
text_file = open(write_to, "w+")

# what to write to file list
to_write = [f"{header}\n", header_2d, f"{result_2d}\n\n", header_3d, f"{result_3d}\n\n", "thank you for using the geometry calculator"]

# write everything in the list to file
for item in to_write:
    text_file.write(item)
    text_file.write("\n")
