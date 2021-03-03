-- Desc
-- Desc
USE hbtn_0d_usa;
SELECT cities.id, cities.name FROM states, cities
WHERE states.id = cities.state_id
AND states.name = 'California'
ORDER BY cities.id ASC;