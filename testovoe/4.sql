create table my_table (
  a int,
  b int
);
insert into my_table values (1, 1), (1, 2), (1, 3), (2, 4), (2, 5), (2, 6), (3, 2), (3, 3), (3, 4);

select a, max(b) over (partition by a) as b
from my_table;
