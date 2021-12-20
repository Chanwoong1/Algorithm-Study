-- https://www.hackerrank.com/challenges/average-population/problem?isFullScreen=true

select round(sum(population) / count(population))
from city