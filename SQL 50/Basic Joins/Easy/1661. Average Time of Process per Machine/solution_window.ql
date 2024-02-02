-- Better time performance

with a as (
    select
      machine_id,
      timestamp - lag(timestamp) over (partition by machine_id, process_id order by timestamp) as processing_time
    from Activity
)
select a.machine_id, round(avg(a.processing_time), 3) as processing_time
from a
where a.processing_time is not Null
group by a.machine_id;
