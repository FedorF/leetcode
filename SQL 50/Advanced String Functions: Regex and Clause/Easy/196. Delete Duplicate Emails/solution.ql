with a as (
    select
      *,
      row_number() over  (partition by email order by id) n
    from Person
)
delete Person
from Person
join a on Person.id = a.id
where a.n > 1
