--  top 3 cities' temperatures 
SELECT city, AVG(temperature) as avg_temp
FROM temperatures
WHERE MONTH(date) IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
