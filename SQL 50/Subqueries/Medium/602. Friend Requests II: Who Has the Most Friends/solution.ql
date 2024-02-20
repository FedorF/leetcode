with a as (
    (select requester_id id from RequestAccepted)
    union all
    (select accepter_id id from RequestAccepted)
)
select
  id,
  count(*) num
from a
group by id
order by count(*) desc
limit 1
