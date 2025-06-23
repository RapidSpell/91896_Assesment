# import statements go here
import pandas

# definitions go here
def add_mm(old_list):
    """ this function adds 'mm' to the end of every value/string in a list"""
    new_list = []

    for item in old_list:
        if item != "NA":
            new_list.append(f"{item}mm")

        else:
            new_list.append(item)

    # return the new version of the list
    return new_list


def add_mm2(value):
    """ this function adds 'mm^2' to the end of a value/string """
    return f"{value}mm\u00b2"


# main routine goes here
# lists for pandas
shapes_2d = ["rectangle"]
dimension_2d1 = ["1"]
dimension_2d2 = ["1"]
dimension_2d3 = ["NA"]
areas = ["1"]
perimeters = ["4"]

# add mm and mm^2
dimension_2d1 = add_mm(dimension_2d1)
dimension_2d2 = add_mm(dimension_2d2)
dimension_2d3 = add_mm(dimension_2d3)


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

# display panda
print(shapes_2d_frame)
