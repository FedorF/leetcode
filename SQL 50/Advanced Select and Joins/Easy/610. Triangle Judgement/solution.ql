select
  *,
  (case
    when a.x + a.y <= a.z then "No"
    when a.x + a.z <= a.y then "No"
    when a.y + a.z <= a.x then "No"
    else "Yes" end) triangle
from Triangle a;
