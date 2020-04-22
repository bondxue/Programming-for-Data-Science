SELECT Rental_month, Rental_year, Store_ID, COUNT(count_rentals) Count_rentals
FROM 
	(SELECT DATE_PART('month', r.rental_date) as Rental_month, DATE_PART('year', r.rental_date) as Rental_year, i.store_id Store_ID, 
		COUNT(i.film_id) OVER (PARTITION BY DATE_TRUNC('month', r.rental_date) ORDER BY i.store_id) as count_rentals
	FROM rental r
	JOIN inventory i
	ON r.inventory_id = i.inventory_id) AS t1
GROUP BY 1, 2, 3
ORDER BY Count_rentals DESC


