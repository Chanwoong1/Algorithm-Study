-- https://www.hackerrank.com/challenges/more-than-75-marks/problem

SELECT NAME
FROM STUDENTS
WHERE MARKS > 75
ORDER BY RIGHT(NAME, 3), ID

/*RIGHT(컬럼명 또는 문자열, 문자열의 길이)
    SELECT RIGHT("20140323, 4) => 0323
*/