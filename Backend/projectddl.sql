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

CREATE table bookmarks(
    rec_id int,
    user_id int,
    /* FOREIGN KEY (recipe_id) REFERENCES recipe(recipe_id), */
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);


-- alter table users, modify veg to be enum veg, nonveg or egg
ALTER TABLE users MODIFY COLUMN veg ENUM('veg', 'nonveg', 'egg');
