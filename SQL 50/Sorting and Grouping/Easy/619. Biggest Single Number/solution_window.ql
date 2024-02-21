with a as (
    select 
      num,
      count(*) over (partition by num) cnt
    from MyNumbers
)
select 
  max(num) num
from a 
where a.cnt = 1
