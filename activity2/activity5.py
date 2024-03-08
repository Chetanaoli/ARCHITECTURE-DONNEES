def rotate_list_right(input_data, rotate_amount):
    try:
        list_length = len(input_data)
        rotate_amount = rotate_amount % list_length
        rotated_list = input_data[-rotate_amount:] + input_data[:-rotate_amount]
        return rotated_list
    except Exception as e:
        return f"Error: {e}"
