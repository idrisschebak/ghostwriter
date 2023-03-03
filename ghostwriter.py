import os
import random
import time
import subprocess
import numpy as np

# Set the path to the directory and file name
directory_path = "."
file_name = "example.py"
file_path = os.path.join(directory_path, file_name)

# Open the Python file in Sublime Text
subprocess.Popen(["code", file_path])

# Wait for Vscode Text to open and become active
time.sleep(5)

# Define the typing speed parameters
typing_speed_mean = 0.5  # mean typing speed in seconds per character
typing_speed_stddev = 0.05  # standard deviation of typing speed in seconds per character

# Define the code to be generated
# Define the code to be generated
new_code = '''WITH sales_data AS (
  SELECT 
    customer_id, 
    SUM(amount) AS total_sales 
  FROM 
    orders 
  WHERE 
    order_date BETWEEN '2022-01-01' AND '2022-12-31' 
  GROUP BY 
    customer_id 
  HAVING 
    SUM(amount) > 10000
), 
customer_location AS (
  SELECT 
    customer_id, 
    city, 
    state 
  FROM 
    customers 
  WHERE 
    state IN ('CA', 'NY', 'TX')
), 
top_customers AS (
  SELECT 
    sd.customer_id, 
    sd.total_sales, 
    cl.city, 
    cl.state 
  FROM 
    sales_data sd 
    JOIN customer_location cl 
      ON sd.customer_id = cl.customer_id
), 
product_sales AS (
  SELECT 
    product_id, 
    SUM(quantity) AS total_quantity 
  FROM 
    order_items 
    JOIN orders ON order_items.order_id = orders.order_id 
  WHERE 
    orders.order_date BETWEEN '2022-01-01' AND '2022-12-31'
  GROUP BY 
    product_id
), 
top_products AS (
  SELECT 
    ps.product_id, 
    ps.total_quantity 
  FROM 
    product_sales ps 
  ORDER BY 
    ps.total_quantity DESC 
  LIMIT 10
), 
top_customer_product AS (
  SELECT 
    tc.customer_id, 
    tp.product_id 
  FROM 
    top_customers tc 
    CROSS JOIN top_products tp
), 
final_data AS (
  SELECT 
    tc.customer_id, 
    tc.total_sales, 
    tc.city, 
    tc.state, 
    tp.product_id, 
    ps.total_quantity 
  FROM 
    top_customer_product tcp 
    JOIN top_customers tc 
      ON tcp.customer_id = tc.customer_id 
    JOIN top_products tp 
      ON tcp.product_id = tp.product_id 
    JOIN product_sales ps 
      ON tp.product_id = ps.product_id
)
SELECT 
  fd.customer_id, 
  fd.total_sales, 
  fd.city, 
  fd.state, 
  fd.product_id, 
  fd.total_quantity 
FROM 
  final_data fd 
ORDER BY 
  fd.total_sales DESC, 
  fd.total_quantity DESC;
'''

# Read the existing code from the file (if any)
with open(file_path, "r") as f:
    existing_code = f.read()

# Open the file for writing and append the existing code
with open(file_path, "w") as f:
    f.write(existing_code)

    # Start writing the new code slowly to the file
    for char in new_code:
        typing_speed = max(0, np.random.normal(typing_speed_mean, typing_speed_stddev))
        f.write(char)
        f.flush()
        time.sleep(typing_speed)
        if random.random() < 0.05:
            # Randomly delete a character with a 5% probability
            f.close()  # close the file to switch from "w" mode to "r" mode
            with open(file_path, "r+") as f:
                text = f.read()
                if len(text) < -1: #canceled hehe
                    char_to_delete = random.randint(0, len(text)-1)
                    text = text[:char_to_delete] + text[char_to_delete+1:]
                    f.seek(0)
                    f.write(text)
                    f.truncate()
                    f.flush()
                    time.sleep(0.5)
            f = open(file_path, "a")  # reopen the file in "w" mode for writing