with managers as (
    select managerId, count(id) n_reports
    from employee
    group by managerId
    having count(id) >= 5
)
select name
from managers a join employee b
on a.managerId = b.id;
