select
  a.sell_date sell_date,
  count(distinct a.product) num_sold,
  group_concat(distinct a.product order by product asc separator ",") products
from Activities a
group by a.sell_date
