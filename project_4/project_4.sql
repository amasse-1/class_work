use mealplanning;

-- 1
delimiter $$
DROP FUNCTION IF EXISTS GetIngredientId$$
CREATE FUNCTION GetIngredientId (desiredIngredientName varchar(100)) RETURNS int 
deterministic
BEGIN
declare desiredIngredientId int;
select distinct Id into desiredIngredientId
FROM Ingredients
WHERE IngredientName = desiredIngredientName;
return desiredIngredientId;
END$$

select * from Ingredients where Id = GetIngredientId('Garlic');

-- Procedure from in class exercise
DROP PROCEDURE IF EXISTS InsertNewRecipe;
delimiter $$
CREATE PROCEDURE InsertNewRecipe (
	myRecipeName varchar(100), 
	myCookBookName varchar(200), 
	myTotalServings int,
	myIsBook bool,
	myWebsite varchar(200))
BEGIN
	DECLARE existingCookbookName varchar(200);
	DECLARE existingRecipeName varchar(100);
	SELECT CookbookName INTO existingCookbookName
	FROM Cookbook
	WHERE CookbookName = myCookBookName;
	select RecipeName into existingRecipeName
	from Recipe
	where RecipeName = myRecipeName;
	if (existingCookbookName is null) then
		insert into Cookbook (cookbookName, isBook, Website) values (myCookBookName,
		myIsBook, myWebsite);
	end if;
	if (existingRecipeName is null) then
		insert into Recipe (RecipeName, CookbookName, TotalServings) values (myRecipeName,
		myCookBookName, myTotalServings);
	end if;
END $$
delimiter ;



-- 2a
call InsertNewRecipe('Next-Level Salmon', 'From Crook to Cook', 4, true, null);

-- 2b
DROP PROCEDURE IF EXISTS InsertNewIngredient;
delimiter $$
CREATE PROCEDURE InsertNewIngredient (
	myIngredientName varchar(100), 
	myIngredientType varchar(100), 
	myRecipeName varchar(100))
BEGIN
	DECLARE existingRecipeName varchar(200);
	DECLARE existingIngredientName varchar(100);
	SELECT IngredientName INTO existingIngredientName
	FROM Ingredients
	WHERE IngredientName = existingIngredientName;
	select RecipeName into existingRecipeName
	from Recipe
	where RecipeName = myRecipeName;
	if (existingIngredientName is null) then
		insert into Ingredients (IngredientName, IngredientType) values (myIngredientName,
		myIngredientType);
	end if;
	if (existingRecipeName is null) then
		insert into Meal (RecipeName, IngredientId) values (myRecipeName,GetIngredientId(myIngredientName));
	end if;
END $$
delimiter ;

call InsertNewIngredient('Salmon', 'fish', 'Next-Level Salmon'); -- inserting it in the tables

-- 3
delimiter $$
DROP PROCEDURE IF EXISTS GetRecipeIngredients$$
CREATE PROCEDURE GetRecipeIngredients (desiredRecipe varchar(200))
BEGIN
	select r.RecipeName, i.IngredientName from meal m
	join ingredients i on i.id = m.IngredientId
	join recipe r on r.RecipeName = m.RecipeName
    where r.RecipeName = desiredRecipe
	order by r.RecipeName, i.IngredientName;
END$$
 

call GetRecipeIngredients('Chicken Stew'); -- checks for Chicken Stew ingredients

-- 4
drop view if exists CookbookRecipes;
create view CookbookRecipes as
select r.RecipeName, r.CookbookName, i.IngredientName from meal m
join ingredients i on i.id = m.IngredientId
join recipe r on r.RecipeName = m.RecipeName
order by r.CookbookName, r.RecipeName, i.IngredientName;

select * from CookbookRecipes;

-- 5
select r.RecipeName, count(i.IngredientName) as IngredientCount from meal m
join ingredients i on i.id = m.IngredientId
join recipe r on r.RecipeName = m.RecipeName
group by r.RecipeName
order by IngredientCount desc;

-- 6
select i.IngredientName from meal m
join ingredients i on i.id = m.IngredientId
join recipe r on r.RecipeName = m.RecipeName
where not r.RecipeName = ;