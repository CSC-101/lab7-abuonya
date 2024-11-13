import convert
from convert import str_to_float


# TASK 2
# DESIGN RECIPE
    # Purpose of Function: takes no parameters and returns a list of numbers (list[float]) and can only contain properly converted floats.
        # Function will end if the user types "done".
    # Input: "72.2" "meow" "64" "Done" --> str  #Ouput Given Input: [72.2, 64] --> list[float]

def gather_numbers():
    user_input = ""     # initializing it empty so it can be someplace in my distant memory...
    temp_list = []
    while not user_input == "Done":
        user_input = input("Input ONE number. Or Done, if you're finished: ")
        temp_number = str_to_float(user_input)
        if temp_number is not None:
            temp_list.append(temp_number)

    print("All Done! Here is your list of VALID numbers.")
    return temp_list

if __name__ == '__main__':
    test = gather_numbers()
    print(test)

