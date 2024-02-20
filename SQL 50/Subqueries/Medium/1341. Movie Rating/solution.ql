with most_active_user as (
    select
      u.name results
    from MovieRating mr join Users u
    on mr.user_id = u.user_id
    group by u.user_id
    order by count(*) desc, u.name asc
    limit 1
),
highest_rating_movie as (
    select
      m.title results
    from MovieRating mr join Movies m
    on mr.movie_id = m.movie_id
    where
      mr.created_at >= "2020-02-01"
      and mr.created_at < "2020-03-01"
    group by m.movie_id
    order by avg(rating) desc, m.title asc
    limit 1
)
(select * from most_active_user)
union all
(select * from highest_rating_movie)
