import convert
from convert import str_to_float


# TASK 2
# DESIGN RECIPE
    # Purpose of Function: takes no parameters and returns a list of numbers (list[float]) and can only contain properly converted floats.
        # Function will end if the user types "done".
    # Input: "72.2" "meow" "64" "Done" --> str  #Ouput Given Input: [72.2, 64] --> list[float]

def gather_numbers():
    user_input = input("Input ONE number.")
    temp_list = []

    try:
        str_to_float(user_input)
        temp_list.append(user_input)
        return temp_list
    except ValueError:
        print("That was not an acceptable input. Numbers only, please. ")

if __name__ == '__main__':
    test = gather_numbers()
    print(test)