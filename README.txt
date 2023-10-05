This is for create your own discord bot, so you just need to change a few things.
The discord bot uses a MySQL database, Open AI api and cogs from discord to do the next things:
 
1. Play, pause, resume and change music staying in the voice channel
2. Register users to a little economy with only coins
3. Talk with the bot
4. Show memes, curiositys, and black humor jokes

It also have a GUI for add more music, jokes and memes. In the case of music and memes, it has to be the path (just something like meme.jpg, music.mp3).
The GUI has 4 widgets, write what you want to add in the entry and click the button.
To use the bot write the commands in a text channel in a server with the prefix (below you will see how to change it) something like: !meme.

In this link you can see how to get your bot token: https://www.youtube.com/watch?v=aI4OmIbkJH8
In this other link you can see how to get your Open AI api key: https://www.youtube.com/watch?v=nafDyRsVnXU

For the 1st thing the bot can do, you need to create the database table with the next code:
create table musicpaths(
    id int not null auto_increment,
    musicpath varchar(255),
    primary key (id)
);

For the 2nd thing the bot can do, you need to create the database table with the next code:
create table users(
    id int not null auto_increment,
    user varchar(255),
    coins int,
    mascotaEquipada varchar(255),
    primary key (id)
);

For the 4th thing the bot can do, you need to create the database tables with the next code:

Memes:
create table memepaths(
    id int not null auto_increment,
    memepath varchar(255),
    primary key (id)
);

Curiositys:
create table curiositys(
    id int not null auto_increment,
    curiosity varchar(255),
    primary key (id)
);

Black humor jokes:
create table chistesnegros(
    id int not null auto_increment,
    chiste varchar(255),
    primary key (id)
);

Things you can change:
- Bot token: this obviusly can be changed, otherwise the bot won't run, go to main.py in "client.run()".
- Open AI api key: for change this, go to RaidenTalk class in support_classes.py and place your key in "self.api_key" atribute.
- Config file path: go to "self.path_file" atribute in curiositys, pelea_mascotas, Memes_working and music_working, DB_pymysql classes.
- Prefix: go to "command_prefix" parameter on the super().__init() of client class in main.py
- Cogs to load: if you create more cogs, add it to "self.coglist" atribute in Client class in main.py
- Config values: open the config.json file with notepad and change the values, but don't change the "values_choose" dictionary.
- The RockPaperScissors minigame answers: go to the RPS class on curiositys.py
- Name of functions in curiositys, pelea_mascotas, Memes_working and music_workinG and RPS classes: just someting like "async def pausar" to "async def pause".
- Multimedia paths: in config file, the "paths_music" and "paths_memes" can be change it, i recommend a simple path like "C:\\Songs".


