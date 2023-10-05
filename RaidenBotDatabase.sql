use discordbot;

select * from users;
select * from chistesnegros;
select * from mascotasDisponibles;

create table musicpaths(
	id int not null auto_increment,
    musicpath varchar(255),
    primary key (id)
);

create table users(
	id int not null auto_increment,
    user varchar(255),
    coins int,
    mascotaEquipada varchar(255),
    primary key (id)
);

create table memepaths(
	id int not null auto_increment,
    memepath varchar(255),
    primary key (id)
);

create table curiositys(
	id int not null auto_increment,
    curiosity varchar(255),
    primary key (id)
);

create table chistesnegros(
	id int not null auto_increment,
    chiste varchar(255),
    primary key (id)
);

select user, password from usersgui where user = "Yahir" and password = "lolazo"; 
insert into usersgui (user, password) values ("Yahir", "lolazo");
select * from usersgui;
select * from curiositys;
select * from memepaths;
select * from musicpaths;
select * from mascotaEquipada;
update users set mascotaEquipada = "Tegemoto" where user = 758205403955200031;