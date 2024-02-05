with daily_total as (
  select
    date(transaction_time) transaction_date,
    sum(transaction_amount) transaction_total
  from transactions
  group by date(transaction_time)
),
daily_rolling_avg as (
  select
    *,
    avg(a.transaction_total) over (order by a.transaction_date rows between 2 preceding and current row) trans_tot_rol_avg_3d
from daily_total a
)
select a.trans_tot_rol_avg_3d
from daily_rolling_avg a
where a.transaction_date = '2021-01-31';
