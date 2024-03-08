def reverse_tuples_order(tuple_list):
    try:
        reversed_list = [tuple(reversed(tpl)) for tpl in tuple_list]
        return reversed_list
    except (SyntaxError, TypeError) as e:
        return f"Error: {e}"
