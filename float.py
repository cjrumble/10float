# FLOAT LESSON
# float() Syntax
# float([number or string])
# Parameters  First, the parameter is optional.If you don’t pass a value, then it returns 0.0.
# Also, the valid argument can only be a number or a string containing some numeric value.
# You  can give both + ve and -ve numeric values.
# if you supply a string with a number with leading or trailing spaces, then it ignores the spaces and returns a float value.

# Return Values
# The float() function returns a floating - point value equivalent to the number passed as is or in the form of a string.
# Errors - It raises the following exceptions when it receives invalid input data.
# ValueError – When you pass a wrong argument such as a string that doesn’t contain a number
# TypeError – When you pass a type argument that it doesn’t allow such as a complex number or NoneType
# float() Examples

# 1 - float() function with +ve number values
# pass +ve values in the float() call.So, it will simply convert them to an equivalent floating - point number.
"""
Desc:
Python example to demonstrate float() function
"""
# Test Input
testInput = [0, 1, 10000, 0.0, 1.1001, 1.000000000000001, 1.0000000000000001, 1.0000]
for eachItem in testInput:
    print("float({}) = {}".format(eachItem, float(eachItem)))
# result:
# float(0) = 0.0
# float(1) = 1.0
# float(10000) = 10000.0
# float(0.0) = 0.0
# float(1.1001) = 1.1001
# float(1.000000000000001) = 1.000000000000001
# float(1.0) = 1.0
# float(1.0) = 1.0
# float(1.0) = 1.0

# 2 - float() function with -ve numbers
"""
Desc:
Python example to demonstrate float() function on -ve numbers
"""
# Test Input
testInput = [-1, -10000, -0.0, -1.1001, -1.000000000000001, -1.0000000000000001, -1.0000]
for eachItem in testInput:
    print("float({}) = {}".format(eachItem, float(eachItem)))
# result:
# float(-1) = -1.0
# float(-10000) = -10000.0
# float(-0.0) = -0.0
# float(-1.1001) = -1.1001
# float(-1.000000000000001) = -1.000000000000001
# float(-1.0) = -1.0
# float(-1.0) = -1.0

# 3 - float() function with a string containing numbers
# When you pass a number in string format( in quotes), then float() converts the value to float type and returns the result.
"""
Desc:
Python example to demonstrate float() function on strings
"""
# Test Input
testInput = ["-1", "-10000", "0.0", "1.1001", "1.000000000000001", "-1.0000000000000001", " 1.0000 "]
for eachItem in testInput:
    print("float({}) = {}".format(eachItem, float(eachItem)))
# output:
# float('-1') = -1.0
# float('-10000') = -10000.0
# float('0.0') = 0.0
# float('1.1001') = 1.1001
# float('1.000000000000001') = 1.000000000000001
# float('-1.0000000000000001') = -1.0
# float(' 1.0000 ') = 1.0

# Python float() function also accepts words like NaN, Infinity, inf( in lower and upper cases).Let’s check this fact with an example.
"""
Desc:
Python float() exmaple for NaN, Infinity, inf
"""
# Test Input
testInput = ["nan", "NaN", "inf", "InF", "InFiNiTy", "infinity"]
# Let's test float()
for eachItem in testInput:
    if isinstance(eachItem, str):
        print("float('{}') = {}".format(eachItem, float(eachItem)))
    else:
        print("float({}) = {}".format(eachItem, float(eachItem)))
# output:
# float('nan') = nan
# float('NaN') = nan
# float('inf') = inf
# float('InF') = inf
# float('InFiNiTy') = inf
# float('infinity') = inf

# float() function with invalid inputs
"""
Desc:
Python float() exmaple for invalid input values
"""

# Test Input with all possible invalid values
testInput = [None, "Python", "0,1", "0 1", 1+2j]

# We'll use exception handling to continue even if some error occurs
for eachItem in testInput:
   try:
      if isinstance(eachItem, str):
        print("float('{}') = {}".format(eachItem, float(eachItem)))
      else:
        print("float({}) = {}".format(eachItem, float(eachItem)))
   except Exception as ex:
        print("float({}) = {}".format(eachItem, ex))

# Also, check for 1/0
try:
  print("float(1/0) = {}".format(float(1/0)))
except Exception as ex:
  print("float(1/0) = {}".format(ex))
# float(None) = float() argument must be a string or a number, not 'NoneType'
# float(Python) = could not convert string to float: 'Python'
# float(0, 1) = could not convert string to float: '0,1'
# float(01) = could not convert string to float: '0 1'
# float((1 + 2j)) = can't convert complex to float
# float(1 / 0) = division by zero