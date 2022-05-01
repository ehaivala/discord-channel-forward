import os
import logging

import discord
from dotenv import load_dotenv

logging.basicConfig(filename='bot.log', level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv('.env')

TOKEN = os.environ.get('DISCORD_TOKEN')
FROM_CHANNEL = os.environ.get('FROM_CHANNEL')
TO_CHANNEL = os.environ.get('TO_CHANNEL')

client = discord.Client()

@client.event
async def on_message(message: discord.Message):
    if message.channel.name == FROM_CHANNEL:
        logger.info(f'Processing message {message.id} from {message.author}')
        try:
            to_channel: discord.TextChannel = discord.utils.get(client.get_all_channels(), name=TO_CHANNEL)
            await to_channel.send(
                f'Message from {message.author.mention}:\n\n{message.content}',
                tts=message.tts,
                files=[await attachment.to_file() for attachment in message.attachments],
            )
            await message.delete()
        except Exception as error:
            logger.exception(error)

client.run(TOKEN)
