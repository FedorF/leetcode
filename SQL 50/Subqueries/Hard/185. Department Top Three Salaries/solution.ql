with a as (
    select
      e.name Employee,
      e.salary Salary,
      d.name Department,
      dense_rank() over (partition by e.departmentId order by e.salary desc) n
    from employee e join department d on e.departmentId = d.id
)
select
  a.Department,
  a.Employee,
  a.Salary
from a
where a.n <= 3;
