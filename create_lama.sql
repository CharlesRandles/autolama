------------------------------------
--- Drop and recreate DB objects ---
------------------------------------

drop table if exists practices;
drop table if exists entry;
drop table if exists lama;

create table lama (
       id integer primary key autoincrement,
       team text,
       dept text,
       date_reported text
);

create table entry (
       id integer primary key autoincrement,
       lama integer,
       practice text,
       maturity text,
       comment text,
       action text,
       foreign key (lama) references lama(id)
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
insert into practices (name) values ('standups');

