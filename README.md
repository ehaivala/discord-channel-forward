# Discord channel forward

Forward Discord messages from one channel to another and deletes the original
message.

## Setup

- Create virtualenv `python3 -m venv venv`
- Activate venv `. venv/bin/activate`
- Install dependencies `pip install -r requirements.txt`

## Config

Create `.env` file with following content for your specific use-case
```
DISCORD_TOKEN=<token>
FROM_CHANNEL=messages-in
TO_CHANNEL=messages-out
```

The bot user must have permissions configured for the channels on Discords GUI.

With these settings the bot will read messages from #messages-in channel,
post it to #messages-out channel and finally delete the original message
from #messages-in channel.
