select
  a.id
from Weather a cross join Weather b
where DATEDIFF(a.recordDate, b.recordDate) = 1 and a.temperature > b.temperature;
