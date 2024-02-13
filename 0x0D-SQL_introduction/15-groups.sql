-- Lists the number of records with the same score in the table second_table in my MySQL server
-- Records are ordered by descending count

SELECT score, COUNT('score') as number
FROM second_table
GROUP BY score
ORDER BY score DESC;
