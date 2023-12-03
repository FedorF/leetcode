with intervals as (
    select
      *,
      id - row_number() over (partition by num order by id asc) interval_id
    from Logs
),
intervals_len as (
    select
      avg(num) num,
      count(*) cnt
    from intervals
    group by num, interval_id
)
select
  distinct(num) ConsecutiveNums
from intervals_len
where cnt >= 3;
