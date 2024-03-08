from activity2.activity15 import find_out_of_stock_products

def test_out_of_stock_products_empty_database():
    result = find_out_of_stock_products({})
    assert result == []

def test_out_of_stock_products_no_out_of_stock_products():
    product_database = {
        1: {'price': 20, 'quantity': 5},
        2: {'price': 15, 'quantity': 10},
        3: {'price': 25, 'quantity': 8}
    }
    result = find_out_of_stock_products(product_database)
    assert result == []

def test_out_of_stock_products_some_out_of_stock_products():
    product_database = {
        1: {'price': 20, 'quantity': 0},
        2: {'price': 15, 'quantity': 10},
        3: {'price': 25, 'quantity': 0}
    }
    result = find_out_of_stock_products(product_database)
    assert result == [3, 1]

def test_out_of_stock_products_all_out_of_stock_products():
    product_database = {
        1: {'price': 20, 'quantity': 0},
        2: {'price': 15, 'quantity': 0},
        3: {'price': 25, 'quantity': 0}
    }
    result = find_out_of_stock_products(product_database)
    assert result == [3, 1, 2]
