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





use familyplanning;

insert into Family(MemberName) values('John');
insert into Family(MemberName) values('Mary');
insert into Family(MemberName) values('Jacob');

select * from TaskDueDate;

insert into Tasks(MemberId, TaskName) values (1, 'Take out the trash');
insert into Tasks(MemberId, TaskName) values (2, 'Clean the dishes');
insert into Tasks(MemberId, Priority, TaskName) values (1, 1,'Fix the faucet');
insert into Tasks(MemberId, TaskName) values (3, 'Do homework');
insert into Tasks(MemberId, TaskName) values (3, 'clean your room');


insert into TaskDueDate(Task_Id, DueDate) values (4, '2023-08-27');
insert into TaskDueDate(Task_Id, DueDate) values (3, '2023-08-29');

delimiter $$
DROP PROCEDURE IF EXISTS getTasks$$
CREATE PROCEDURE getTasks (desiredMemeberName varchar(200))
BEGIN
	select t.TaskName from Tasks t
    inner join Family f on t.MemberId = f.Id
    where f.MemberName = desiredMemeberName
    order by t.Id;
END$$

call getTasks("John");

delimiter $$
DROP PROCEDURE IF EXISTS getTaskDueDates$$
CREATE PROCEDURE getTaskDueDates (desiredMemeberName varchar(200))
BEGIN
	select td.DueDate from TaskDueDate td
    inner join Tasks t on t.Id = td.Task_id
    inner join Family f on t.MemberId = f.Id
    where f.MemberName = desiredMemeberName
    order by t.Id;
END$$

call getTaskDueDates("John");