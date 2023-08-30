/*
	CSC6302 Database Principles
	Project Three: Intermediate SQL
    Anthony Masse
*/
use mealplanning;
-- 1a
select RecipeName, count(IngredientId) from meal where RecipeName = 'Chicken Stew';

-- 1b 
select r.RecipeName, r.CookbookName, i.IngredientName, i.IngredientType from meal m
join ingredients i on i.id = m.IngredientId
join recipe r on r.RecipeName = m.RecipeName
order by r.RecipeName, i.IngredientName;

-- 1c 
select RecipeName, count(*) as max_count from meal group by RecipeName order by max_count desc LIMIT 1;

/* 
1d . 
- Tried my best and I know it would be stuffing as the recipe but I just couldn't figure it out.
*/
select r.RecipeName, r.CookbookName from recipe r
left outer join meal m on r.RecipeName = m.RecipeName
left outer join ingredients i on m.IngredientId = i.Id
where i.IngredientName like exists (select i.IngredientName from ingredients i where i.IngredientName not like '%Pepper%')
and i.Id not in (1,2);

-- 1e
select IngredientName, IngredientType from ingredients
group by IngredientType, IngredientName 
order by IngredientName asc;

/*-------------------------------------------------------------------------------- */

-- 2a & 2b
insert into cookbook (CookbookName, IsBook) values ('From Crook to Cook', true);
insert into recipe (RecipeName, CookbookName, TotalServings) values ('Next-Level Salmon', 'From Crook to Cook', 4);
insert into ingredients (IngredientName, IngredientType) values ('Salmon', 'meat');
insert into meal (RecipeName, IngredientId) values ('Next-Level Salmon', 15);

-- 3a
use videogamesystems;

update game set Series = null where GameName like '%Yoshi%'; -- to reset the table

select * from game where GameName like '%Yoshi%'; -- to look at the Yoshi games

update game set Series = 2 where GameName like '%Yoshi%'; -- update Yoshi games

select * from game where GameName like '%Yoshi%'; -- to look at the Yoshi games

-- 4 - added to the CreateMealPlanning_edited sql file. 

