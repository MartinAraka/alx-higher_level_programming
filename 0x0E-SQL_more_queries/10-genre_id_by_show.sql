-- Script that lists shows with genre_id

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres
ON tv_show.id=tv_show_genres.show_id
ORDER BY tv_show.title, tv_show_genres.genre_id;
