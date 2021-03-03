-- Desc
-- Desc
USE hbtn_0d_usa;
SELECT states.id, states.name, cities.id, cities.state_id, cities.name FROM states, cities
WHERE states.id = cities.state_id;