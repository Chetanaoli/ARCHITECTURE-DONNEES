def print_triangle_pattern(pyramid_height):
    for row in range(1, pyramid_height + 1):
        spaces = ' ' * (pyramid_height - row)
        stars = '*' * (2 * row - 1)
        print(spaces + stars)
