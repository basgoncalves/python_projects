--- https://www.youtube.com/watch?v=IBgWKTaG_Bs&ab_channel=CodingWithMike

-- SELECT * FROM USERS;

CREATE TABLE IF NOT EXISTS USERS (id INTEGER NOT NULL PRIMARY KEY,
username TEXT NOT NULL,
 passoword NOT NULL, email NOT NULL);

INSERT INTO USERS (id, username, passoword, email)          -- the CREATE and INSERT (username) can only be done once
SELECT 1, 'mike', 'mypassowrd', 'mike@gmail.com'          -- unless inserting a different username
WHERE NOT EXISTS (SELECT 1 FROM USERS);

INSERT INTO USERS (id, username, passoword, email)
SELECT 2, 'peter', '1234', 'peter@gmail.com'
WHERE NOT EXISTS (SELECT 2 FROM USERS WHERE id = 2);

INSERT INTO USERS (id, username, passoword, email)
SELECT 3, 'bas', 'basman', 'bas@gmail.com'
WHERE NOT EXISTS (SELECT 3 FROM USERS WHERE id = 3);

-- SELECT passoword FROM USERS
-- WHERE username = 'mike'; --- the ";" is needed in the end

-- SELECT USERS,
--     COUNT(DISTINCT, username) AS num_users;

ALTER TABLE USERS
ADD COLUMN twitter_handle TEXT;

SELECT * FROM USERS;

-- SELECT * FROM USERS;    -- show all table

-- UPDATE USERS
-- SET twitter_handle = '@basgoncalves'
-- WHERE id = 3;

-- SELECT * FROM USERS;

-- DELETE FROM USERS               -- delete rows that have NULL in twitter handle
-- WHERE twitter_handle IS NULL;

-- SELECT * FROM USERS;

-- CREATE TABLE PRAKNS (id INTEGER NOT NULL PRIMARY KEY,
-- username TEXT NOT NULL,
--  prank NOT NULL, email NOT NULL);

-- SELECT * FROM PRAKNS;

-- INSERT INTO PRAKNS (id, username, prank,email)          -- the CREATE and INSERT (username) can only be done once
-- VALUES (1, 'mike', 'flour','@');

-- ALTER TABLE PRAKNS
-- ADD COLUMN twitter_handle TEXT;

-- UPDATE PRAKNS
-- SET twitter_handle = '@mike'
-- WHERE id = 1;

-- SELECT * FROM PRAKNS;

-- SELECT * FROM firends;

-- CREATE TABLE friends(
--     id INTEGER,
--     name  TEXT,
--     birthday DATE
-- );

-- INSERT INTO friends(id,name,birthday)
-- VALUES(1, 'Ororo Munroe', '1940-05-30');

-- SELECT * FROM friends;

-- INSERT INTO friends(id,name,birthday)
-- VALUES(2, 'Davs', '1940-05-27');

-- INSERT INTO friends(id,name,birthday)
-- VALUES(3, 'Tamara', '1940-05-29');

-- UPDATE friends
-- SET name = 'Ororo Storm'
-- WHERE id = 1;

-- ALTER TABLE friends
-- ADD COLUMN email TEXT;

-- UPDATE friends
-- SET email = 'storm@codecademy.com'
-- WHERE id = 1;

-- UPDATE friends
-- SET email = 'davs@codecademy.com'
-- WHERE id = 2;

-- UPDATE friends
-- SET email = 'tamara@codecademy.com'
-- WHERE id = 3;

-- DELETE FROM friends               -- delete rows that have NULL in twitter handle
-- WHERE name = 'Ororo Storm';

-- SELECT * FROM friends;