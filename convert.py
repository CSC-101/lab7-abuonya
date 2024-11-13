from typing import Optional


# TASK 1
# DESIGN RECIPE
    # Purpose of Function: takes a single parameter of type str and that returns an Optional[float]. If the argument string represents a float value, then this function will convert the string into a float and return that value.  If such a conversion is not possible, then the function will return None.
    # Input: "72.2" --> str  #Ouput Given Input: 72.2 --> Optional[float]

def str_to_float(string:str) -> Optional[float]:

