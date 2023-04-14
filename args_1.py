# A function named concatenate_args that takes 
# any number of string arguments in positional arguments 
# format and concatenates them into a single string

def concatenate_args(*string):
    result = " "
    for str in string:
        result += str
        
    return result

# A function named concatenate_kwargs that 
# takes any number of string arguments in keyword 
# arguments  format and concatenates them into a single string
def concatenate_kwargs(**kwargs):
    result = " "
    for kwa in kwargs.values():
        result += kwa
    return result

