with user_cnt as (
    select count(*) total from Users
)
select
  a.contest_id,
  round(100*count(*) / b.total, 2) percentage
from Register a cross join user_cnt b
group by a.contest_id
order by round(100*count(*) / b.total, 2) desc, a.contest_id asc;
