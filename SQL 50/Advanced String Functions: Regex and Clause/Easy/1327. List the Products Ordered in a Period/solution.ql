select
  p.product_name,
  sum(o.unit) unit
from Orders o left join Products p
on o.product_id = p.product_id
where o.order_date >= "2020-02-01" and o.order_date < "2020-03-01"
group by p.product_id, p.product_name
having sum(o.unit) >= 100
