-- create table with all possible categories in order to have all categories in final table
with all_categories as (
    select "Low Salary" category
    union
    select "Average Salary" category
    union
    select "High Salary" category
),
accounts_category as (
    select
      *,
      case
        when income < 20000 then "Low Salary"
        when income > 50000 then "High Salary"
        else "Average Salary"
      end category
    from Accounts
)
select
  a.category category,
  sum(case when b.income is Null then 0 else 1 end) accounts_count
from all_categories a left join accounts_category b
on a.category = b.category
group by a.category;
