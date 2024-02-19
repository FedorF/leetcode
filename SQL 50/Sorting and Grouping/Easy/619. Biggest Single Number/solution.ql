select
  (case when count(*) = 1 then num else Null end) num
from MyNumbers
group by num
order by count(*) asc, num desc
limit 1
