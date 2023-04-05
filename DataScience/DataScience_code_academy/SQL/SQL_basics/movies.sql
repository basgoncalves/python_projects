SELECT * FROM movies;

SELECT name, genre 
FROM movies;

SELECT imdb_rating AS 'IMDb' --load with different name
FROM movies;

SELECT * FROM movies;

SELECT *
FROM movies
WHERE imdb_rating < 5;

SELECT * 
FROM movies
WHERE name LIKE 'Se_en'; -- serach for elements with 'Se_en' and '_' means anything can bether

SELECT * 
FROM movies
WHERE name LIKE 'A%'; -- A% = with 'A' in the beginning

SELECT * 
FROM movies
WHERE name LIKE '%a'; -- a% = with 'a' in the end

SELECT * 
FROM movies
WHERE name LIKE '%man%'; -- %man% = with 'man' in the middle

SELECT * 
FROM movies
WHERE name LIKE 'The %'; -- The% = with 'The ' in the beginning

SELECT *
FROM movies
WHERE name BETWEEN 'D%' AND 'G%'; -- movies starting with D(inclusive) to G (not inclusive)

SELECT *
FROM movies
WHERE year BETWEEN 1970 AND 1979; -- with numbers the UPPER bound is INCLUSIVE

SELECT *
FROM movies
WHERE year < 1985 AND genre = 'horror'; -- before 1985 AND horror

SELECT *
FROM movies
WHERE genre = 'romance'  OR genre = 'comedy';

SELECT name, year,imdb_rating
FROM movies
WHERE imdb_rating IS NOT 'NULL'         -- where comes before order ALWAYS
ORDER BY imdb_rating DESC               -- 
LIMIT 3;                                -- show only 3 entries

SELECT name,
 CASE
  WHEN genre = 'romance' THEN 'Chill'       -- if ... then statement
  WHEN genre = 'comedy'  THEN 'Chill'
  ELSE 'Intense'
 END AS 'Mood'
FROM movies;

-- RENAME COLUMN
SELECT name, year,
AVG(imdb_rating) AS avg_downloads
FROM MOVIES
GROUP BY year