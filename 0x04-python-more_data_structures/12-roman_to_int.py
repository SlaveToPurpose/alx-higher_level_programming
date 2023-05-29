#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or type(roman_string) != str:
        return 0
    roman_vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    final_int_val = 0
    for char in range(len(roman_string)):
        value = roman_vals[roman_string[char]]
        if char < len(roman_string) - 1 and value < roman_vals[roman_string[char + 1]]:
            final_int_val -= value
        else:
            final_int_val += value
    return final_int_val
