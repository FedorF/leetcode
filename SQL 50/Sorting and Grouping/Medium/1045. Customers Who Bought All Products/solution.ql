with a as (
    select distinct
      customer_id,
      product_key
    from Customer
)
select
  a.customer_id customer_id
from Product p left join a
on p.product_key = a.product_key
group by a.customer_id
having count(*) = (select count(*) from Product)
