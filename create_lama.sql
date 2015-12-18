------------------------------------
--- Drop and recreate DB objects ---
------------------------------------

drop table if exists entry;

drop table if exists lama;

create table lama (
       id integer primary key autoincrement,
       team text,
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
