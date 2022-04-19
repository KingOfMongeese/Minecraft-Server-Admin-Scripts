# Minecraft-Server-Admin-Scripts

Useful bash scripts to be used with a minecraft server running inside a screen socket.

These run best when used with cron. Each script has different configuration requirements.


# Screen Setup

```sudo apt update && sudo apt install screen```

```screen -S screen_name```
You can name the screen what ever you want. The defualt for the scripts is "mainworld" if you change this be sure to configure the scripts accordingly

You can exit the screen and return to the parent terminal any time by:
```ctrl + a + d```

To resume the screen use:
```screen -r screen_name```

For more help run:
```man screen```

Or see the docs: [Screen Docs](https://www.gnu.org/software/screen/manual/screen.html)

