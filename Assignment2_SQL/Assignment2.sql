#Wu Shuyang 1730026119

-- Q1
SELECT year
FROM book NATURAL JOIN rating
WHERE stars = 3 OR stars = 2
ORDER BY year DESC;

-- Q2
SELECT DISTINCT rname
FROM reviewer NATURAL JOIN rating
WHERE stars IS NOT NULL and rDate IS NULL;

-- Q3
SELECT rname, bname
FROM book, reviewer, rating, rating AS rating2
WHERE rating.bid = book.bid AND reviewer.rid = rating.rid AND
      rating.rid = rating2.rid AND rating2.bid = book.bid AND
      rating.stars < rating2.stars AND rating.rdate < rating2.rdate;

-- Q4
SELECT bname, avg(stars)
FROM book NATURAL JOIN rating
GROUP BY bname
ORDER BY avg(stars) DESC, bName ASC;

-- Q5
SELECT rname
FROM reviewer NATURAL JOIN rating
GROUP BY rname
HAVING COUNT(rating.stars) >= 3;

-- Q6
SELECT rname, bname, stars, rdate
FROM reviewer NATURAL JOIN rating NATURAL JOIN book
ORDER BY rname, bname, stars;

-- Q7
SELECT bname, MAX(stars)
FROM book NATURAL JOIN rating
GROUP BY bname;

-- Q8
SELECT bname, MAX(stars)-MIN(stars) as stars_spread
FROM book NATURAL JOIN rating
GROUP BY bname
ORDER BY stars_spread DESC