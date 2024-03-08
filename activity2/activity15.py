def find_out_of_stock_products(product_data):
    out_of_stock_ids = [product_id for product_id, info in product_data.items() if info['quantity'] == 0]

    sorted_out_of_stock = sorted(out_of_stock_ids, key=lambda x: (product_data[x]['price'], x), reverse=True)
    return sorted_out_of_stock
