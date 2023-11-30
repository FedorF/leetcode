with a as (
    select
      *,
      (case when order_date = customer_pref_delivery_date then 1 else 0 end) is_immidiate,
      row_number() over (partition by customer_id order by order_date asc) n_order
    from Delivery
)
select
  round(100*sum(is_immidiate) / count(*), 2) immediate_percentage
from a
where n_order = 1;
