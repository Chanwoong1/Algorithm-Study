-- https://www.hackerrank.com/challenges/the-blunder/problem?isFullScreen=true

select ceil((sum(salary) / count(salary)) - (sum(regexp_replace(salary,'[0]','')) / count(salary)))
from employees