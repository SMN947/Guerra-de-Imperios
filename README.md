# Discord-Template-Bot

## About

This is a simple template for a Discord bot.

## Install

Using *pip* install the ***discord*** module: 
```bash
python3 -m pip install -U discord.py
```

**HTTPS:**
```bash
git clone https://github.com/SMN947/Discord-Template-Bot.git
```

**SSH:**
```bash
git clone git@github.com:SMN947/Discord-Template-Bot.git
```

Rename the file ***config.template.json*** to ***config.json*** and update its content with your own data.

```json
{
  "bot_prefix": "*",
  "token": "45gsdfgtwMzksdfsdcsdfFNjY2.EfvsfrR.5SDFvsdrVereRre5HDeg_cOsU"
}
```

## Run

```bash
python bot.py
```

## List of commands

- Info
  - Shows the current status of the server memory, cpu and latency
  - Alias:
    - info
    - botinfo
    - bi
    - status

- Help
  - Shows the main list of commands
  - Alias:
    - ayuda
    - help
    - a
    - h
