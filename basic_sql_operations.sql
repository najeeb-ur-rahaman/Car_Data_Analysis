-- Basic Query:

-- Retrieve all records where msrp is greater than 50,000.

select * from car_data where msrp > 50000

-- Filtering:

-- Get all records for the year 2024 where the make_name is "Acura".

select * from car_data where year = 2023 and make_name = 'Rolls-Royce'

-- Aggregation:

-- Calculate the average msrp for each make_name and return the result with columns make_name and average_msrp.

select make_name,year, avg(msrp) as average_msrp 
from car_data group by(make_name,year) order by avg(msrp)

-- Group By:

-- Find the total invoice amount grouped by year.

select make_name, sum(invoice) as total_invoice
from car_data group by(make_name)

-- Window Functions:

-- Add a rank to each car within its make_name group based on msrp in descending order.

select make_name,msrp,year,
rank() over(order by msrp desc) msrp_rank
from car_data
group by(make_name, msrp, year)

-- display the highest msrp totals in desc in a year 
select make_name,count(1) as cars_sold, sum(msrp) as msrp_sum,year,
rank() over(partition by year order by sum(msrp) desc) msrp_sum_rank
from car_data
group by(make_name, year)
order by year desc,sum(msrp) desc

-- Self join
-- Perform a self-join on the car_data table. Join on make_id and year.
-- Return columns: c1.make_name, c1.year, c1.msrp, c2.msrp (where c2 is the joined table).
-- Filter where c1.msrp is less than c2.msrp. Sort by c1.make_name and c1.year.

select c1.make_name, c1.year, c1.msrp, c2.msrp
from car_data c1,
join  car_data c2
on c1.make_id = c2.make_id and c1.year = c2.yearcar_data c2
where c1.msrp < c2.msrp
order by c1.make_name, c1.year

