WITH sales_data AS (
  SELECT 
    customer_id, 
    SUM(amount) AS total_sales 
  FROM 
    orders 
  WHERE 
    order_d