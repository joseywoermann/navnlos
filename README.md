# ![]

![](https://github.com/joseywoermann/navnlos/blob/master/assets/navnlos.PNG)

![](https://badgen.net/github/release/joseywoermann/navnlos/stable?color=black) ![](https://badgen.net/github/last-commit/joseywoermann/navnlos?color=black) [![CodeFactor](https://www.codefactor.io/repository/github/joseywoermann/navnlos/badge)](https://www.codefactor.io/repository/github/joseywoermann/navnlos)

[Join the support-server!](https://discord.gg/52TbNHPBU9)

## A multi purpose Discord bot.

navnløs is a Discord bot designed to be modular and feature rich.

# Features

#### Moderation

* User-management
* Role-management
* server management



#### Automatic actions

* member counter (requires a channel named `Members:` which the bot can modify)
* automatically publish messages in announcement-channels (currently in development)


# Hosting navnløs yourself

##### Requirements

You need to...
* have Python 3.5.3 or newer installed
* install all dependencies by doing `pip install -r requirements.txt` in the bot's root directory (you may want to do this in a virtual environment)
* create a bot on [this website](https://discord.com/developers/applications/)
* create a file called `bot.TOKEN` in the root directory of the bot and paste your token into it
* If you want to use the `$bugreport` feature, you will need to create a GitHub "personal access token" and paste it into `github.TOKEN`
* If you want to use the `$shorturl` feature, you will need to create a [short.io](https://short.io/) API-key and paste it into `shortio.TOKEN`
* That should be it!

##### Basic setup and start

* open a command line tool
* execute the command `.venv\Scripts\activate.bat`
* execute the command `python main.py`
* Now the bot should be running!
