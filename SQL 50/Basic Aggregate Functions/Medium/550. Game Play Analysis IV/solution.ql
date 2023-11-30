with a as (
    select
      *,
      row_number() over (partition by player_id order by event_date asc) n_day,
      lag(event_date) over (partition by player_id order by event_date asc) prev_date
    from Activity
)
select
  round(
      sum(
          case
            when n_day = 2 and DATEDIFF(event_date, prev_date) = 1 then 1
            else 0
          end
      ) / (select count(distinct player_id) from a), 2
  ) fraction
from a;
