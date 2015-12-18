------------------------------------
--- Drop and recreate DB objects ---
------------------------------------

drop table if exists lama;

create table lama (
       id int primary key autoincrement,
       team text,
       date_reported text
);