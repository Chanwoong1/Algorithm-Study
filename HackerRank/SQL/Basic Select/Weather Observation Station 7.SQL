-- https://www.hackerrank.com/challenges/weather-observation-station-7/problem?isFullScreen=true

SELECT DISTINCT(CITY)
FROM STATION
WHERE CITY REGEXP '[aeiou]$'    -- 정규표현식