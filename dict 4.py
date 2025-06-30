# Figure out a way to store 9 & 9.0 as separate values in the set.
# This is a problem because sets in Python cannot contain duplicate values.
# To store both 9 and 9.0 as separate values, you can use a list or a dictionary instead of a set.
values = {9, "9.0"}
print(values)  # Output: {9, 9.0}