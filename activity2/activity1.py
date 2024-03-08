def count_upper_and_lower(input_str):
    upper_count = 0
    lower_count = 0

    for char in input_str:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    return upper_count, lower_count
