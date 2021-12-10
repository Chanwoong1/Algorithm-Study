-- https://www.hackerrank.com/challenges/weather-observation-station-3/problem

select distinct(city) -- distinct : 중복제거
from station
where id % 2 = 0