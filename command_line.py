import sys

# TASK 3
# DESIGN RECIPE:
    # Purpose of Function: processes the command-line arguments by converting each into a float (skipping any that cannot be converted), adding them all together, and then printing the sum.
    # Input: "72.2" "meow" --> str  #Ouput Given Input: 72.2 --> float

def take_sum_of_numbers():
    sum = 0.0
    number_of_inputs = len(sys.argv)
    for i in range(1,number_of_inputs):
        try:
            temp = float(sys.argv[i])
            sum += temp
        except ValueError:
            print(sys.argv[i], "is not a valid input. Skipped.")
    print(sum)

if __name__ == '__main__':
   take_sum_of_numbers()