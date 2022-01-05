select * from sakila.customer;
select distinct(store_id) from sakila.customer;
select * from sakila.payment;
select distinct(customer_id) from sakila.payment;
#
select * from sakila.country order by country DESC;
select * from sakila.country order by country ASC;
#
select * from sakila.customer order by first_name asc;
###
select store_id as Tienda, first_name as Nombre, last_name as Apellido
from sakila.customer
order by Apellido desc;
###
select distinct amount from sakila.payment order by amount 
asc;
##################################################################
#####CLAUSULA WHERE##################
select * from sakila.actor where first_name = 'DAN';
select * from sakila.city where country_id = 102; 
select * from sakila.customer where store_id=1; 
#
select * from sakila.inventory where film_id >50;
select * from sakila.payment where amount < 3;
select distinct amount from sakila.payment where amount < 3;
####
select * from sakila.staff;
select * from sakila.staff where staff_id <> 2;
select * from sakila.language where name <> 'German';
#
select description, release_year  from sakila.film
where title = 'IMPACT ALADDIN';
#
select * from sakila.payment
where amount > 0.99;
########################################################
##### AND ; OR ; NOT ####################
select * from sakila.country
where country = "Algeria" and country_id = 12;
select * from sakila.country
where country = 'Algeria' and country_id = 2;
select * from sakila.country where country = "Algeria" or country_id = 12;
select * from sakila.language where language_id = 1 or name = "German";
select * from sakila.category where name= "Action";
select * from sakila.category where not name= "Action";
select * from sakila.film where rating = "PG";
select * from sakila.film where not rating = "PG";
select distinct(rating) from sakila.film where not rating = "R";
####
select * from sakila.payment
where customer_id = 36
and amount > 0.99
and staff_id = 1;
###
select * from sakila.rental
where not staff_id = 1;
#########################################################################
################## IN ###########################
select * from sakila.customer where first_name = "MARY" and first_name = "PATRICIA";
select * from sakila.customer where first_name = "MARY" or first_name = "PATRICIA";
select * from sakila.customer where first_name in ("MARY","PATRICIA");
#
select * from sakila.film where special_features in ("Trailers","Trailers,Deleted Scenes");
select * from sakila.film where special_features in ("Trailers","Trailers,Deleted Scenes") and rating in ("G","NC-17");
select * from sakila.film where special_features in ("Trailers","Trailers,Deleted Scenes") and rating in ("G","NC-17")
and length > 100;
select * from sakila.category where name not in ("Action","Animation","Children");
####
select * from sakila.film_text where title in ('ZORRO ARK', 'VIRGIN DAISY', 'UNITED PILOT');
##
select * from sakila.city where city in ('Chiayi', 'Dongying', 'Fukuyama', 'Kilis');
###########################################################################
#### BETWEEN ###########
select * from sakila.rental; 
select * from sakila.rental where customer_id between 300 and 350;
select * from sakila.rental where (customer_id between 300 and 350) and staff_id =1; 
select * from sakila.payment where amount between 3 and 5;
select * from sakila.payment where amount not between 3 and 5;
#
select * from sakila. payment where (amount  between 2.99 and 4.99 ) and staff_id = 2 and customer_id in (1,2);
select * from sakila.address where city_id between 300 and 350;
select * from sakila.film where (rental_rate between 0.99 and 2.99 )and length <=50 and replacement_cost < 20;
#####################################################################################
########## LIKE #####################
select * from sakila.actor 
where first_name like "A%";
select * from sakila.actor 
where first_name like "A%" and last_name like "B%";
#
select * from sakila.actor 
where first_name like "%A" and last_name like "%L";
#
select * from sakila.actor 
where first_name like "%NE%";
#
select * from sakila.actor 
where first_name like "C%N" and last_name like "G%";
##
select * from sakila.film where release_year = 2006 and title like 'ALI%';
#########################################################################################
######## INNER JOIN, LEFT JOIN, RIGHT JOIN ###################
#inner los que tienen en comun
#left los de la tabla de izquierda mantiene todos los datos
#right tabla der. mantiene todos los datos;

select *
from sakila.film f
inner join sakila.language l on (f.language_id = l.language_id);

#
select f.title, f.description,f.release_year,f.language_id,l.name
from sakila.film f
inner join sakila.language l on (f.language_id = l.language_id);
#
select* from sakila.address;
select * from sakila.city;
select * from sakila.address a
inner join sakila.city c on(a.city_id = c.city_id);
##
select a.address as Direccion, c.city as Ciudad from sakila.address a
inner join sakila.city c on(a.city_id = c.city_id);
#
select * from sakila.customer; 
select * from sakila.actor;
select c.customer_id,c.first_name, c.last_name,a.actor_id, a.first_name , a.last_name from sakila.customer c
inner join sakila.actor a on(c.last_name = a.last_name);
####
select c.customer_id,c.first_name,c.last_name,a.actor_id,a.first_name,a.last_name from sakila.customer c
left join sakila.actor a on(c.last_name = a.last_name);
################
select a.address,c.city,co.country from sakila.address a 
inner join sakila.city c on (a.city_id = c.city_id)
inner join sakila.country co on (c.country_id = co.country_id);
#######
select c.first_name,a.address,s.store_id from sakila.customer c
left join sakila.store s on (c.store_id = s.store_id)
left join sakila.address a on (c.address_id = a.address_id);
################
select r.rental_id,
s.first_name from sakila.rental r
inner join sakila.staff s on (r.staff_id = s.staff_id);
#######################################################
#######################################################
### Count, avg,sum,max,min #######################
select * from sakila.payment;
select sum(amount) from sakila.payment;
#
select * from sakila.inventory;
select inventory_id + film_id + store_id
from sakila.inventory;
#
select * from sakila.actor;
select count(*) from sakila.actor;
select count(first_name) from sakila.actor;
#
select * from sakila.film;
select avg(rental_duration) from sakila.film;
select max(rental_duration) from sakila.film;
#
select max(length) from sakila.film;
select min(length) from sakila.film;
#
select min(replacement_cost) from sakila.film;
select max(replacement_cost) from sakila.film;
#
select count(rental_id) from sakila.rental;
select max(amount) from sakila.payment;
#########################################################################################
############ GROUP BY ###########################
select last_name from sakila.actor
group by last_name;
#
select last_name, count(*) from sakila.actor
group by last_name;
#
select * from sakila.payment;
select * from sakila.customer;
select c.customer_id,c.first_name,c.last_name, sum(p.amount) from sakila.payment p
inner join sakila.customer c on ( c.customer_id=p.customer_id)
group by 1,2,3 ;
######
SELECT customer_id, MAX(rental_date)
FROM sakila.rental
GROUP BY customer_id;
#########################################################################################
############ HAVING ###########################
select last_name, count(*)
from sakila.actor
group by 1
having count(*)>3;
#####
select c.customer_id,c.last_name,c.first_name,sum(p.amount) from sakila.payment p
inner join sakila.customer c on (p.customer_id = c.customer_id) 
group by 1,2,3
having sum(p.amount)<100
order by sum(p.amount) desc;
#
SELECT last_name, COUNT(*)
FROM sakila.actor
GROUP BY last_name
HAVING COUNT(*) > 3;
#########################################################################################
############ Funciones utiles ###########################
SELECT * FROM category;
SELECT name, CHAR_LENGTH(name) as LongitudCadena
from category;
#
SELECT * FROM city;
SELECT city, CHAR_LENGTH(city) as LongitudCity
FROM city;
###
SELECT * FROM customer;
SELECT *,CONCAT(first_name," ",last_name)as "Nombre Completo"
FROM customer;
#####
SELECT * FROM film;
#~Select*, concat(COLUMNA1,COLUMNA2,COLUMNA3)~
Select concat_ws(" - ",title,description,release_year)
from film;
#########
select *,ROUND(amount,0) from payment;
###
Select * from actor;

select*, lcase(concat(first_name," ", last_name)) as "Nombre minuscula" from actor;
#########################################################################################
############ CASE ###########################
SELECT * FROM address;

SELECT address ,address2,
CASE
WHEN address2 is null then "sin direccion 2"
ELSE "con direccion"
END AS Comentario
FROM address;
##
select payment_id,amount,
case
when amount <1 then "Precio minimo"
when amount between 1 and 3 then "precio inter"
else "precio maximo"
end as Comentario
from payment;
#########################################################################################
############ subqueries ###########################
select title
from film
where title like "K%" or title like "Q%" 
and title in
(select title from film where language_id in
(select language_id from language where name = "English"));
#
select 
first_name, 
last_name 
from actor
where actor_id in ( select actor_id from film_actor where film_id in 
(select film_id from film where title = "Alone Trip"));
#
select title from film where film_id in (select film_id from film_category where category_id in (
select category_id from category where name = "Family"));
######## views ###########################
create VIEW ingresos_por_genero AS

select name, sum(amount)
from category 
inner join film_category
on category.category_id = film_category.category_id
inner join inventory
on film_category.film_id = inventory.film_id
inner join rental
on inventory.inventory_id = rental.inventory_id
inner join payment
on rental.rental_id = payment.rental_id
group by name
order by sum(amount) desc limit 5;
select * from ingresos_por_genero ;
drop view ingresos_por_genero ;
################################
### consultas multitablas########
select
a.first_name, a.last_name,sum(b.amount) as "Total amouin" from staff a
inner join payment b on a.staff_id = b.staff_id
and b.payment_date like "2005-08%"
group by a.first_name, a.last_name;
#
select b.title, count(actor_id) as "contador de actores" 
from film_actor a
inner join film b on a.film_id = b.film_id
group by b.title;
#
select title,
count(title) as "copias disp" 
from film 
inner join inventory on film.film_id = inventory.film_id
where title = 'Hunchback impossible' ;
#
select first_name,last_name,sum(amount) as "total pagado pro cli"
from payment inner join customer on payment.customer_id = customer.customer_id
group by first_name,last_name
order by last_name;
########################################################################
############# insert into################################################
select * from city;
insert into city(city ,country_id)
values("prueba","100");
#######################
Select * from actor;
insert into actor(first_name,last_name)
values('CARLOS','BERNAL');
#
SELECT * FROM CATEGORY;
INSERT INTO category(NAME)
values("CIENCIA FICCION")
########################################################################
############# UPDATE ################################################
; select * from city;
update city
set city = "NEW YORK"
where country_id = 87;
##########
select * from actor;
update actor
set first_name = "JUAN"
where actor_id = 1;
##################
select * from staff;
update staff 
set first_name = "PEDRO"
where staff_id = 2;
###############################
#####   alter tabla      ##################
select * from actor;

alter table actor
add column genero_actor char(1);
alter table actor
drop column genero_actor;
########################
select * from actor;
alter table actor
add column genero_actor char(1);
update actor
set genero_actor = "M"
where actor_id = 1;
###########################################
select * from actor where first_name = 'Scarlett';
select * from actor where last_name like 'Johansson';
select count(distinct last_name) from actor;
select last_name from actor group by last_name having count(*) = 1;
select actor.actor_id, actor.first_name, actor.last_name, 
count(actor_id) as film_count
from actor join film_actor using (actor_id)
group by actor_id
order by film_count desc;
select film.film_id, film.title, store.store_id, inventory.inventory_id
from inventory join store using (store_id) join film using (film_id)
where film.title = 'Academy Dinosaur' and store.store_id = 1;