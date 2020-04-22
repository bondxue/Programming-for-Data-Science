SELECT name, stanard_quartile, COUNT(*)
FROM
	(SELECT title, name, rental_duration, NTILE(4) OVER (ORDER BY rental_duration) AS stanard_quartile
	FROM
		(SELECT f.title, c.name, f.rental_duration
		FROM category c
		JOIN film_category fc
		ON c.category_id = fc.category_id
		JOIN film f
		ON f.film_id = fc.film_id
		WHERE c.name IN ('Animation', 'Children','Classics','Comedy','Family','Music')) AS t1
	ORDER BY 4) AS t2
GROUP BY 1, 2
ORDER BY 1, 2
	


