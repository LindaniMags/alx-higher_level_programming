-- Displays the average temperature by city ordered by temperature (descending).
SELECT city, ROUND(AVG(temperature), 2) AS average_temperature
FROM temperatures
GROUP BY city
ORDER BY average_temperature DESC;
