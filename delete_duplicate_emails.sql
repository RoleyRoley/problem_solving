-- Delete rows from t1
DELETE t1 FROM Person t1

-- Create two versions of the table
INNER JOIN Person t2

-- Compare every row, find duplicates
WHERE t1.id > t2.id AND t1.email = t2.email;