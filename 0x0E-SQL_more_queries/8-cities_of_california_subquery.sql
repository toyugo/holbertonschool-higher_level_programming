-- Desc
-- Desc
USE hbtn_0d_usa;
SELECT id, name FROM states, cities
WHERE states.name = cities.id
ORDER BY ASC;