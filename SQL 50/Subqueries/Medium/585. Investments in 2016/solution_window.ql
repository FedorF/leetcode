with a as (
    select
      tiv_2016,
      count(*) over (partition by tiv_2015) val_cnt,
      count(*) over (partition by lat, lon) loc_cnt
    from Insurance
)
select
  round(sum(tiv_2016), 2) tiv_2016
from a
where a.val_cnt >= 2 and loc_cnt = 1
