--  Lists all records of second_table of hbtn_0c_0 with name value
SELECT score, name
FROM second_table
WHERE name != ""
ORDER BY score DESC
