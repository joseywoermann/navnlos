![](https://github.com/joseywoermann/navnlos/blob/master/assets/navnlos.PNG)

[Join the support-server!](https://discord.gg/52TbNHPBU9)

# A multi purpose Discord bot.

## Hosting navnløs yourself

##### Requirements

You need to...

-   have Python installed
-   install all dependencies by doing `pip install -r requirements.txt` in the bot's root directory (you may want to do this in a virtual environment)
-   create a bot on [this website](https://discord.com/developers/applications/)
-   create a file called `.env` with the following structure in the root directory:

```
DISCORD_TOKEN=
GITHUB_TOKEN=
SHORTIO_TOKEN=
SENTRY_URL=
STATCORD_TOKEN=
```

-   If you want to use the `/bugreport` feature, you will need to create a GitHub "personal access token"
-   If you want to use the `/shorturl` feature, you will need to create a [short.io](https://short.io/) API-key
-   That should be it!

##### Basic setup and start

-   open a command line tool
-   (execute `.venv\Scripts\activate.bat`)
-   execute `python main.py`
-   Now the bot should be running!
