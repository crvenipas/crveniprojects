select teacher
from Schedule s join Class c
on s.class = c.id
where c.name like '11%'
group by teacher
having count(distinct c.name) =
(
select count(id) from Class
where name like '11%'
);