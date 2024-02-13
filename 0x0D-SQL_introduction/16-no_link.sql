-- list all records in a table except those with no name value by descending order
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
