-- displays the average temperature by city ordere by temp desc
SELECT city, AVG(value) AS "avg_temp"
FROM temperatures
GROUP BY city
ORDER BY value DESC;
