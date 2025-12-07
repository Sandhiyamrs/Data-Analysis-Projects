-- Sales growth by year
SELECT YEAR(order_date) AS yr,
       SUM(revenue) AS total_revenue,
       LAG(SUM(revenue)) OVER (ORDER BY YEAR(order_date)) AS prev_rev
FROM orders
GROUP BY YEAR(order_date)
ORDER BY yr;
