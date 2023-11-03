import pytest
from divide_in_groups import divide_number, divide_number2

def test_divide_3_in_3():
    x = divide_number(3,3)
    assert x == [1,1,1]

def test_divide_7_in_3():
    x = divide_number(7,3)
    assert x == [3,2,2]

def test_divide_3_in_5():
    x = divide_number(3,5)
    assert x == [1,1,1,0,0]

def test_divide_10_in_4():
    x = divide_number(10,4)
    assert x == [3,3,2,2]

def test_divide_19_in_2():
    x = divide_number(19,2)
    assert x == [10,9]

def test_divide_5_in_4():
    x = divide_number(5,4)
    assert x == [2,1,1,1]

#=================================
# Testing Divide_Number2

def test_divide_3_in_3_New_Method():
    x = divide_number2(3,3)
    assert x == [1,1,1]

def test_divide_7_in_3_New_Method():
    x = divide_number2(7,3)
    assert x == [2,2,3]

def test_divide_3_in_5_New_Method():
    x = divide_number2(3,5)
    assert x == [0,0,1,1,1]

def test_divide_10_in_4_New_Method():
    x = divide_number2(10,4)
    assert x == [2,2,3,3]

def test_divide_19_in_2_New_Method():
    x = divide_number2(19,2)
    assert x == [9,10]

def test_divide_5_in_4_New_Method():
    x = divide_number2(5,4)
    assert x == [1,1,1,2]