with same_val as (
    select
      distinct a.pid pid
    from Insurance a join Insurance b
    on a.tiv_2015 = b.tiv_2015
    where a.pid <> b.pid
),
unique_loc as (
    select lat, lon
    from Insurance
    group by lat, lon
    having count(*) = 1
)
select
  round(sum(tiv_2016), 2) tiv_2016
from unique_loc a join (
    select
      a.pid,
      a.tiv_2016,
      a.lat,
      a.lon
    from Insurance a join same_val b
    on a.pid = b.pid
) b
on a.lat = b.lat and a.lon = b.lon
