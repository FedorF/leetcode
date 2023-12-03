with a as (
    select
      s.product_id,
      s.year,
      s.quantity,
      s.price,
      rank() over (partition by s.product_id order by s.year asc) n
    from sales s right join product p on s.product_id = p.product_id
    where s.product_id is not Null
)
select
  product_id,
  year first_year,
  quantity,
  price
from a
where n = 1;
