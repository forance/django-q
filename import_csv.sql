COPY order_reminder_Orders(order_id,ship_date,customer,currency,creater,order_amount,create_date) 
FROM '/Users/nicktang/Documents/2016Talk-Django-Q-master/sc_simple.csv' DELIMITER ',' CSV HEADER;
