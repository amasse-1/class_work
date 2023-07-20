drop database if exists beach_vacation; -- drop db

create database if not exists beach_vacation;

use beach_vacation;

create table if not exists trip(
destination varchar(50) not null,
season varchar(20) not null check (season in ('Fall', 'Winter', 'Spring', 'Summer')),
suitcase_count int not null check (suitcase_count > 0), 
primary key(destination, season)
);

insert into trip values 
('Hawaii', 'Summer', 2), 
('Florida', 'Fall', 4), 
('Aruba', 'Winter', 1);

create table if not exists suitcase(
suitcase_id int not null,
owner_name varchar(50) not null,  
destination varchar(50) not null,
primary key (suitcase_id, owner_name), 
foreign key (destination) references trip(destination) 
);

insert into suitcase values
(1, 'Anthony', 'Hawaii'), 
(2, 'Kaylee', 'Hawaii'), 
(4, 'Bob', 'Florida'), 
(7, 'Bob', 'Florida'), 
(5, 'Jane', 'Aruba');

create table if not exists item(
item_name varchar(20) not null,
suitcase_id int not null, 
destination varchar(50) not null,
primary key (item_name, suitcase_id), 
foreign key (suitcase_id) references suitcase(suitcase_id) on update cascade on delete cascade, 
foreign key (destination) references trip(destination) on update cascade on delete cascade
);

insert into item values
('Hat', 1, 'Hawaii'), 
('Toothpaste', 7, 'Florida'), 
('Aloe Vera', 7, 'Florida'), 
('Sweater', 4, 'Florida'),
('Hat', 5, 'Aruba'), 
('Shorts', 2, 'Hawaii');

