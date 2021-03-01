-- displays the average temperature
SELECT state, max(value) AS "max_temp" FROM temperatures
WHERE month = 7 OR month = 8
GROUP BY state ORDER BY state DESC LIMIT 3;