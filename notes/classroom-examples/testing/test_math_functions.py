import math_functions as m
# you can change the way python 
# interprets math_functions to just m (m.add())
# import * = import everything (it might overwrite 
# functions that you wrote before)

def test_add():
    assert math_functions.add(1, 1) == 2


def test_subtract():
    assert math_functions.subtract(5, 2) == 3
