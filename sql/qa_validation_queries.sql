-- Sample SQL validation queries for an e-commerce application.
-- Assumed tables: customers, orders, order_items, products, payments.

-- TC-SQL-001:
-- Verify the item total, stored order total, and payment status for one order.
SELECT
    o.order_id,
    o.status,
    o.total_amount AS stored_order_total,
    SUM(oi.quantity * oi.unit_price) AS calculated_item_total,
    p.payment_status
FROM orders o
JOIN order_items oi ON oi.order_id = o.order_id
JOIN payments p ON p.order_id = o.order_id
WHERE o.order_id = 1001
GROUP BY o.order_id, o.status, o.total_amount, p.payment_status;


-- TC-SQL-002:
-- Find completed orders where the saved total does not match item totals.
SELECT
    o.order_id,
    o.total_amount AS stored_order_total,
    SUM(oi.quantity * oi.unit_price) AS calculated_item_total
FROM orders o
JOIN order_items oi ON oi.order_id = o.order_id
WHERE o.status = 'COMPLETED'
GROUP BY o.order_id, o.total_amount
HAVING o.total_amount <> SUM(oi.quantity * oi.unit_price);


-- TC-SQL-003:
-- Find order items whose ordered quantity is greater than stock quantity.
SELECT
    oi.order_id,
    p.product_name,
    oi.quantity AS ordered_quantity,
    p.stock_quantity
FROM order_items oi
JOIN products p ON p.product_id = oi.product_id
WHERE oi.quantity > p.stock_quantity;


-- TC-SQL-004:
-- Find customers with more than one failed payment in the last 30 days.
SELECT
    c.customer_id,
    c.customer_name,
    COUNT(*) AS failed_payment_count
FROM customers c
JOIN orders o ON o.customer_id = c.customer_id
JOIN payments p ON p.order_id = o.order_id
WHERE p.payment_status = 'FAILED'
  AND p.payment_date >= CURRENT_DATE - INTERVAL 30 DAY
GROUP BY c.customer_id, c.customer_name
HAVING COUNT(*) > 1;