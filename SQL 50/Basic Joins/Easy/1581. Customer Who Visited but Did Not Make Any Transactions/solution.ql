select a.customer_id, count(a.visit_id) as count_no_trans
from Visits a left join Transactions b on a.visit_id = b.visit_id
where b.transaction_id is Null
group by a.customer_id;
