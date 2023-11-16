-- list all records in table with valid value for name
SELECT `score`, `name`
FROM `second_table`
WHERE `name` IS NOT NULL && `name` != ''
ORDER BY `score` DESC;
