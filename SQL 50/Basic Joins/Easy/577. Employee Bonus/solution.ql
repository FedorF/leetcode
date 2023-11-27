select name, bonus from Employee a
left join Bonus b on a.empId = b.empId
where coalesce(b.bonus, 0) < 1000;
