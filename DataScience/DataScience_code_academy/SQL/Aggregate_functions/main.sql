SELECT * FROM fake_apps LIMIT 5;

SELECT DISTINCT category
FROM fake_apps;

SELECT COUNT(*) FROM fake_apps
WHERE price < 0.01;

SELECT * FROM fake_apps
WHERE price < 0.01;

SELECT SUM(downloads)
FROM fake_apps;

SELECT MAX(price)
FROM fake_apps;

SELECT AVG(price)
FROM fake_apps;

SELECT AVG(downloads)
FROM fake_apps;

SELECT name, ROUND(price, 0)
FROM fake_apps;

SELECT ROUND(AVG(price),2)
FROM fake_apps;

SELECT price, COUNT(*) 
FROM fake_apps
WHERE downloads > 200
GROUP BY price;

SELECT category, SUM(downloads) 
FROM fake_apps
GROUP BY category;

-- Select 
SELECT category, price, 
ROUND(AVG(downloads)) AS round
FROM fake_apps
GROUP BY category,price;

SELECT price, 
    ROUND(AVG(downloads)) AS round,
    COUNT(*) AS 'count_price > 0'
FROM fake_apps
GROUP BY price
HAVING COUNT(price) > 0;

SELECT price,
    COUNT(*) AS 'count_downloads > 10'
FROM fake_apps
GROUP BY price
HAVING COUNT(downloads) > 10;

SELECT price, COUNT(price) 
FROM fake_apps;