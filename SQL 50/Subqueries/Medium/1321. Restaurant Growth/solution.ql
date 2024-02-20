with a as (
    select
      visited_on,
      sum(amount) amount
    from Customer
    group by visited_on
),
b as (
    select
      a.visited_on visited_on,
      row_number() over (order by a.visited_on) row_n,
      sum(a.amount) over (order by a.visited_on rows between 6 preceding and current row) amount,
      avg(a.amount) over (order by a.visited_on rows between 6 preceding and current row) average_amount
    from a
)
select
  visited_on,
  round(amount, 2) amount,
  round(average_amount, 2) average_amount
from b
where row_n >= 7
