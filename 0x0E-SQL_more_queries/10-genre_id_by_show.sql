-- List all shows contained in DB hbtn_0d_tvshows
SELECT tv_shows.title, tv_shows_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NOT NULL
order by tv_shows.title ASC, tv_show_genre_id ASC;
