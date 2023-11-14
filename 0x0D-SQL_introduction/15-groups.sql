-- lists the number of recrods with the same score
SELECT score, COUNT(id) FROM second_table GROUP BY score;
