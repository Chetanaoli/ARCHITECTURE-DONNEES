def find_unique_elements(input_data):
    unique_data = []
    for item in input_data:
        if item not in unique_data:
            unique_data.append(item)
    return unique_data
