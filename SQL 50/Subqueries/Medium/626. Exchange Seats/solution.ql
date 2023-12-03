with a as (
    select
      *,
      lag(student) over (order by id asc) prev_stud,
      lead(student) over (order by id asc) next_stud
    from seat
)
select
  id,
  (case
    when id % 2 = 0 then a.prev_stud
    when a.next_stud is Null then a.student
    else a.next_stud
    end) student
from a;
