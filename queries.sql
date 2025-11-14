-- Join query: user, orders, order_items, products with line totals
SELECT 
    u.user_id,
    u.name AS user_name,
    o.order_id,
    o.order_date,
    p.name AS product_name,
    oi.quantity,
    p.price,
    (oi.quantity * p.price) AS total_line_value
FROM orders o
JOIN users u ON o.user_id = u.user_id
JOIN order_items oi ON oi.order_id = o.order_id
JOIN products p ON p.product_id = oi.product_id
ORDER BY o.order_date DESC;

-- Revenue per user
SELECT 
    u.user_id,
    u.name,
    SUM(oi.quantity * p.price) AS total_revenue
FROM users u
JOIN orders o ON u.user_id = o.user_id
JOIN order_items oi ON oi.order_id = o.order_id
JOIN products p ON p.product_id = oi.product_id
GROUP BY u.user_id
ORDER BY total_revenue DESC;