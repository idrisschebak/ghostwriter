WITH sales_data AS (
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
  