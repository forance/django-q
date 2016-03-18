COPY order_reminder_orders(order_id,order_amount,customer,ship_date) 
FROM '/Users/nicktang/Documents/2016Talk-Django-Q-master/orders.csv' DELIMITER ',' CSV HEADER;
