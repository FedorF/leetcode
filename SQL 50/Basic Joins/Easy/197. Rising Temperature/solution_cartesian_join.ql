-- Another way of making cartesian product (cross join)
select a.id
from Weather a, Weather b
where DATEDIFF(a.recordDate, b.recordDate) = 1 and a.temperature > b.temperature;
