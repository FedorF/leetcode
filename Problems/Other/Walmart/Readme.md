```

membership table:  
+--------------+---------+  
| Column Name  | Type    |  
+--------------+---------+  
| member_id    | int     |  
| program_id   | int     |  
| start_date   | date    |  
| end_date     | date    |  
+--------------+---------+  

+-----------+-----------+------------+--------------+  
| member_id | program_id| start_date | end_date     |  
+-----------+-----------+------------+--------------+  
| 1         | 2         | 2022-02-01 |              |  
| 2         | 3         | 2022-02-01 |2022-02-10    |  
| 3         | 1         | 2022-02-01 |2022-04-01    |  
| 4         | 1         | 2022-02-02 |2022-06-07    |  
| 5         | 4         | 2022-02-02 |              |  
| 6         | 2         | 2022-02-02 |              |  
| 7         | 1         | 2022-02-02 |2022-02-10    |  
| 8         | 1         | 2022-02-02 |              |  
| 9         | 1         | 2022-02-03 |2022-02-05    |  
| 10        | 3         | 2022-02-03 |              |  
+-----------+-----------+------------+--------------+ 

This table shows the activity of members in membership program.  
Each row is a record of a payer who signed up through acquisition program and retention behaviors.  

The start date of a member is the signup day of that member.  
The end date of a member is the churn day of that member. 
If end date is null then this member remain active.  

We define 30 day retention of some date x to be the number of member whose start date is x and they remain active 30 days after x, divided by the number of members whose signup date is x, rounded to 2 decimal places.   


-- Write an SQL query to report for each signup date, the number of members that signup through program 1. 
select 
  start_date,
  count(*) cnt
from membership
where program_id = 1
group by start_date


-- Write a SQL query to display the top program name (acquisition signups) and it’s contribution in 2020.  
with a as (
select 
  program_id,
  count(distinct member_id) as cnt
from membership
where start_date between "2020-01-01" and "2020-12-31"
group by program_id
)
select 
  a.program_id,
  a.cnt / (select sum(a.cnt) from a)
from a 
order by a.cnt desc
limit 1



-- Write a SQL query to report on each programID 30 day retention rate 
-- We define 30 day retention of some date x to be the number of member whose start date is x and they remain active 30 days after x, divided by the number of members whose signup date is x, rounded to 2 decimal places.
with a as (
  select 
    *,
    coalesce(date_diff(end_date, start_date), 31) duration
  from membership
),
b as (
select 
   a.program_id,
   a.start_date,
   case when(a.duration >= 30) then 1 else 0 end active_users,
from a
)

select 
   b.program_id,
   b.start_date,
   sum(b.active_users) / cnt(*) retention_rate
from b
group by b.program_id, b.start_date



-- Write a SQL query to identify what percentage of the churned users join back within 3 months in 2020.
with a as (
select 
 * 
from membership 
where start_date between "2020-01-01" and "2020-12-31"
)
select 
  date_diff(t1.end_date, t2.start_date) 
from a t1 join a t2
on t1.member_id = t2.member_id
where t1.start_date > t2.start_date

-- Write a SQL query to identify what percentage of the churned users from program 1 joined back through program 2. 


```