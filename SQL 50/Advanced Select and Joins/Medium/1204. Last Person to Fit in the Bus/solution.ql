with a as (
    select
      *,
      sum(weight) over (order by turn asc) cur_weight
    from Queue
),
in_bus as (
    select
      *,
      max(a.turn) over () last_turn  -- define a column with maximum "turn" within people in bus
    from a
    where a.cur_weight <= 1000
)
select in_bus.person_name from in_bus where in_bus.turn = in_bus.last_turn;
