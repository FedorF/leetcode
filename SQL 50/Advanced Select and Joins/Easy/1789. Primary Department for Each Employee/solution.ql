with a as (
    select
      *,
      count(*) over (partition by employee_id) dep_cnt
    from Employee
)

(
    select
      employee_id,
      department_id
    from a
    where a.dep_cnt = 1
) union (
    select
      employee_id,
      department_id
    from a
    where a.dep_cnt > 1 and a.primary_flag = "Y"
);
