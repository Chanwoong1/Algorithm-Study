-- https://www.hackerrank.com/challenges/weather-observation-station-6/problem?isFullScreen=true

SELECT CITY
FROM STATION
WHERE CITY LIKE 'a%' 
    or CITY LIKE 'e%' 
    or CITY LIKE 'i%' 
    or CITY LIKE 'o%' 
    or CITY LIKE 'u%'