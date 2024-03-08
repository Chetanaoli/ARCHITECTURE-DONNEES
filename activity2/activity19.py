def iterate_and_increment_bytearray(byte_data):
    for index, value in enumerate(byte_data):
        print(f"Element {index + 1}: {value}")
        byte_data[index] += 1