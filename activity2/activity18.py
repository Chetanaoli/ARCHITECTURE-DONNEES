def update_bytearray_element(input_values, element_index, new_element):
    byte_array = bytearray(input_values)
    
    if 0 <= element_index < len(byte_array):
        byte_array[element_index] = new_element
        return byte_array
    else:
        return None

