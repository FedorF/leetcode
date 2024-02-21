select
  user_id,
  concat(upper(substr(name, 1, 1)), lower(substr(name, 2, length(name)))) name
from Users
order by user_id
