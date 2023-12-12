SELECT * FROM nomnom;

SELECT * FROM nomnom LIMIT 2;

SELECT DISTINCT neighborhood FROM nomnom;

SELECT DISTINCT cusine FROM nomnom;

SELECT name FROM nomnom WHERE cusine == 'Chinese';

SELECT name FROM nomnom WHERE rating >= 4;

SELECT name FROM nomnom 
WHERE cusine == 'Italian' AND price LIKE '$$$%';

SELECT name FROM nomnom 
WHERE name LIKE '%meatball%';

SELECT name FROM nomnom 
WHERE neighborhood == 'Midtown' OR neighborhood == 'Downtown' 
OR neighborhood == 'Chinatown';

SELECT name FROM nomnom 
WHERE health == 'NULL';

SELECT * FROM nomnom 
WHERE rating <= 5 ORDER BY rating DESC
LIMIT 10;

SELECT *,
 CASE
  WHEN rating > 4.5 THEN 'Extraordinary'    
  WHEN rating > 4 THEN 'Excellent'    
  WHEN rating > 3 THEN 'Good'    
  WHEN rating > 2 THEN 'Fair'    
  ELSE 'Poor'
 END AS 'quality_rating'
FROM nomnom;