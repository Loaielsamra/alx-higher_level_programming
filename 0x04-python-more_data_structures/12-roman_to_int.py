#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    result = 0
    n = len(roman_string)

    for i in range(n - 1, -1, -1):
        current_value = roman_values[roman_string[i]]
        if i < n - 1 and current_value < roman_values[roman_string[i + 1]]:
            result -= current_value
        else:
            result += current_value

    return result
