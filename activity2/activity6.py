def find_tuple_with_most_elements(tuple_list):
    if not tuple_list:
        return None 

    max_length = 0
    max_tuple = None

    for tpl in tuple_list:
        current_length = len(tpl)
        if current_length > max_length:
            max_length = current_length
            max_tuple = tpl

    return max_tuple
