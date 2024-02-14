-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- List all cities of California
SELECT * FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id;
