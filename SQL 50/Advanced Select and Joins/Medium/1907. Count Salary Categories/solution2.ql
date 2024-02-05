(
    select
      "Low Salary" category,
      sum(income < 20000) accounts_count
    from Accounts
)
union
(
    select
      "Average Salary" category,
      sum(income between 20000 and 50000) accounts_count
    from Accounts
)
union
(
    select
      "High Salary" category,
      sum(income > 50000) accounts_count
from Accounts
)
