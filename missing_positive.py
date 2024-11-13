"""Missing Positive Project

Used to get the first missing positive
"""
def first_missing_positive(numbers):
    """
    :param numbers: list of integers
    :return: the missing positive
    """
    numbers.sort()
    missing = 1  # starting from integer 1
    for i in numbers:
        if i == missing:
            missing += 1  # the variable will continue updating when it's equal to the list
        else:
            if i > missing:  # variable with stop updating
                break
    return missing


Numbers = [1,2,4,-1]
print("The missing positive number in this list : "+str(first_missing_positive(Numbers)))
