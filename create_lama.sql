------------------------------------
--- Drop and recreate DB objects ---
------------------------------------

drop table if exists practices;
drop table if exists lama;

create table lama (
       id integer primary key autoincrement,
       team_name text,
       department_name text,
       date_reported text,
       standups text,
       retrospectives text,
       backlog_management text,
       product_ownership text,
       iteration_management text,
       track_and_visualise_progress text,
       building_quality_in text,
       adaptive_planning text
);

---Config tables

--Practices
create table practices (
       id integer primary key autoincrement,
       name text);

insert into practices (name) values ('standups');
insert into practices (name) values ('retrospectives');
insert into practices (name) values ('backlog_management');
insert into practices (name) values ('product_ownership');
insert into practices (name) values ('iteration_management');
insert into practices (name) values ('track_and_visualise_progress');
insert into practices (name) values ('building_quality_in');
insert into practices (name) values ('adaptive_planning');

