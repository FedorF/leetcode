-- better performance comparing with cross join approach

with a as (
select
  id,
  temperature - lag(temperature) over (order by recordDate asc) as temp_delta,
  DATEDIFF(recordDate, lag(recordDate) over (order by recordDate asc)) as date_delta
from Weather
)
select a.id from a
where a.temp_delta > 0 and date_delta = 1;
