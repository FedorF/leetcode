with all_product as (
    select distinct product_id from Products
),
a as (
    select
      *
    from Products
    where Products.change_date <= "2019-08-16"
),
b as (
    select
      *,
      row_number() over (partition by a.product_id order by a.change_date desc) row_num
    from a
),
new_price_products as (
    select
      b.product_id,
      b.new_price price
    from b
    where b.row_num = 1
)
select
  A.product_id product_id,
  coalesce(B.price, 10) price
from all_product A left join new_price_products B
on A.product_id = B.product_id;
