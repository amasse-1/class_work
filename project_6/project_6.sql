drop database if exists FamilyPlanning;

create database FamilyPlanning;

use FamilyPlanning;

drop table if exists Family;

create table if not exists Family(
	Id int not null auto_increment, 
    MemberName varchar(50) not null,
    primary key (Id, MemberName)
);

drop table if exists Tasks;

create table if not exists Tasks(
	Id int not null auto_increment,
	MemberId int not null, 
    Priority int default 3 check (Priority between 1 and 3), 
    TaskName varchar(100) not null, 
    primary key (Id, MemberId), 
    foreign key (MemberId) references Family(Id) on update cascade on delete cascade
);

drop table if exists TaskDueDate;

create table TaskDueDate(
	Task_id int not null,
    DueDate Date,
    primary key(Task_id, DueDate),
    foreign key (Task_id) references Tasks(Id) on update cascade on delete cascade
);