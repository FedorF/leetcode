select
  a.student_id,
  a.student_name,
  b.subject_name,
  sum(case
        when c.subject_name is Null then 0
        else 1
      end) attended_exams
from Students a
cross join Subjects b
left join Examinations c
on a.student_id = c.student_id
   and b.subject_name = c.subject_name
group by a.student_id, b.subject_name
order by a.student_id, b.subject_name;
