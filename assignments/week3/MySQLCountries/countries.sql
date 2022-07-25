SELECT * FROM world.countries;
SELECT countries.name, languages.language, languages.percentage
FROM countries JOIN languages ON countries.id = languages.country_id
WHERE language = 'Slovene' ORDER BY percentage DESC;
SELECT countries.name, COUNT(cities.name) AS number_of_cities
FROM countries JOIN cities ON countries.id = cities.country_id
GROUP BY countries.name
ORDER BY COUNT(cities.name) DESC;
SELECT cities.name, cities.population
FROM countries JOIN cities ON countries.id = cities.country_id
WHERE countries.name = 'Mexico'AND cities.population > 500000
ORDER BY cities.population DESC;
SELECT countries.name, languages.language, languages.percentage
FROM countries JOIN languages ON countries.id = languages.country_id
WHERE percentage > 89
ORDER BY percentage DESC;
SELECT name, surface_area, population FROM countries
WHERE surface_area < 501 AND population > 100000;
SELECT name, government_form, capital, life_expectancy FROM countries
WHERE government_form = 'Constitutional Monarchy'
AND life_expectancy > 75 AND capital > 200;
SELECT countries.name, cities.name, cities.district, cities.population
FROM countries JOIN cities ON countries.id = cities.country_id
WHERE countries.name = 'Argentina' AND cities.district = 'Buenos Aires' AND cities.population > 500000;
SELECT region, COUNT(name) AS countries FROM countries
GROUP BY region
ORDER BY COUNT(name) DESC;
