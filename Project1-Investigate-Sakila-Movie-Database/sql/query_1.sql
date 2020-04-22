SELECT film_title, category_name, COUNT(film_title) rental_count 
FROM 
	(SELECT f.title film_title, c.name category_name 
	FROM category c
	JOIN film_category fc
	ON c.category_id = fc.category_id
	JOIN film f
	ON fc.film_id = f.film_id
	JOIN inventory i
	ON i.film_id = f.film_id 
	JOIN rental r
	ON r.inventory_id = i.inventory_id 
	WHERE c.name IN ('Animation', 'Children', 'Classics', 'Comedy', 'Family','Music')) AS t1
GROUP BY 1, 2
ORDER BY 2, 1


