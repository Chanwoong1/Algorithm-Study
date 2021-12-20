-- https://www.hackerrank.com/challenges/revising-aggregations-the-average-function/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

select sum(population) / count(population)
from city
where district = 'California';