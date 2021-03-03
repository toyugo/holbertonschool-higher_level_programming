-- Desc
-- Desc
USE hbtn_0d_usa;
SELECT cities.id, cities.name FROM cities
WHERE state_id IN (SELECT id FROM states WHERE name = "California")
ORDER BY cities.id ASC;