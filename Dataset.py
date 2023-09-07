import pandas as pd
import numpy as np

# Define customer data
customer_data = {
    'customer_id': np.random.randint(1001, 1051, size=50),
    'customer_age': np.random.randint(20, 61, size=50),
}

# Define product data
product_data = {
    'product_name': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E', 'Product F', 'Product G', 'Product H', 'Product I', 'Product J'],
    'product_category': ['Category 1', 'Category 2', 'Category 3'],
}

# Generate order data
order_data = {
    'order_id': np.arange(1, 51),
    'order_date': pd.date_range(start='2022-03-15', end='2022-04-13', periods=50).strftime('%Y-%m-%d'),
    'customer_id': customer_data['customer_id'],
    'product_name': np.random.choice(product_data['product_name'], size=50),
    'product_category': np.random.choice(product_data['product_category'], size=50),
    'order_amount': np.random.randint(80, 251, size=50),
    'payment_method': np.random.choice(['Credit Card', 'PayPal', 'Debit Card'], size=50),
    'shipping_address': np.random.choice(['123 Main St', '456 Maple Ave', '789 Elm St', '345 Oak St', '678 Pine St', '901 Cedar St', '234 Birch Ave', '567 Oak St', '890 Maple Ave', '123 Pine St', '456 Main St', '789 Maple Ave', '345 Cedar St', '678 Elm St', '901 Oak St'], size=50),
    'customer_age': customer_data['customer_age'],
}

# Create DataFrame and save to CSV file
customer_orders = pd.DataFrame(order_data)
customer_orders.to_csv('customer_orders.csv', index=False)
