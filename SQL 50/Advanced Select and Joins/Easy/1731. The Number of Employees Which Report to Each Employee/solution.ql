with managers as (
    select
      reports_to manager,
      count(*) reports_count,
      round(avg(age)) average_age
    from Employees
    group by reports_to
    having count(*) > 0
)
select
  a.employee_id,
  a.name,
  managers.reports_count reports_count,
  managers.average_age average_age
from Employees a join managers
on a.employee_id = managers.manager
order by a.employee_id asc;
