with a as (
    select
      *,
      dense_rank() over (order by salary desc) n
    from Employee
)
select
  max(a.salary) SecondHighestSalary
from a
where a.n = 2
