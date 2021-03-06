-- Desc
-- Desc
-- SELECT tv_genres.name AS genre, COUNT(tv_shows.title) as number_of_shows
-- FROM tv_genres
-- LEFT JOIN tv_show_genres
-- ON tv_show_genres.genre_id = tv_genres.id
-- LEFT JOIN tv_shows
-- ON tv_shows.id = tv_show_genres.show_id
-- GROUP BY tv_genres.name
-- ORDER BY number_of_shows DESC;
SELECT tv_genres.name AS "genre", COUNT(tv_show_genres.genre_id) AS "number_of_shows" 
FROM tv_genres
JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id 
GROUP BY genre 
ORDER BY number_of_shows DESC;