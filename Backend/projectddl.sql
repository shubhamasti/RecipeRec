-- drop database rrs;
create database rrs;

use rrs;

CREATE table users(
    user_id int NOT NULL AUTO_INCREMENT , 
    username varchar(20) not null unique, 
    password varchar(30) not null,
    veg enum('veg','nonveg') DEFAULT 'veg',
    allergen_list varchar(255),
    primary key(user_id)
);

CREATE Table recipe(
    recipe_id INT NOT NULL AUTO_INCREMENT,
    recipe_name VARCHAR(255) NOT NULL UNIQUE,
    ingredients VARCHAR(255) NOT NULL,
    time_to_cook INT NOT NULL,
    cuisine VARCHAR(255) NOT NULL,
    instructions VARCHAR(255) NOT NULL,
    url VARCHAR(255) NOT NULL,
    cleaned_ingredients VARCHAR(255) NOT NULL,
    recipe_image_url VARCHAR(255) NOT NULL,
    ingredient_count INT NOT NULL,
    PRIMARY KEY (recipe_id)
);

CREATE table bookmarks(
    rec_id int,
    user_id int,
    /* FOREIGN KEY (recipe_id) REFERENCES recipe(recipe_id), */
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);


-- alter table users, modify veg to be enum veg, nonveg or egg
ALTER TABLE users MODIFY COLUMN veg ENUM('veg', 'nonveg', 'egg');