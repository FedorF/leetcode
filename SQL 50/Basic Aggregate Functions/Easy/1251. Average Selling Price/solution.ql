select
  a.product_id,
  coalesce(round(sum(b.units * a.price) / sum(b.units), 2), 0) average_price
from prices a left join UnitsSold b
on a.product_id = b.product_id
and b.purchase_date >= a.start_date
and b.purchase_date <= a.end_date
group by a.product_id;
