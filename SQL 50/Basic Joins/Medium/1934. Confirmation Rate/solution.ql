with users as (
    select distinct user_id from signups
), agg as (
    select
      a.user_id,
      sum(case when b.action = 'confirmed' then 1 else 0 end) confirmed,
      count(*) total
    from users a left join confirmations b
    on a.user_id = b.user_id
    group by a.user_id
)
select
  user_id,
  round(confirmed / total, 2) confirmation_rate
from agg;
