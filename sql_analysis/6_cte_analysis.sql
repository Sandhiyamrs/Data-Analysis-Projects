WITH sales_cte AS (
    SELECT region, SUM(amount) AS total_sales
    FROM sales
    GROUP BY region
)
SELECT * FROM sales_cte WHERE total_sales > 100000;
