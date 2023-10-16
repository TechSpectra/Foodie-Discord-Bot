import discord
import os
from dotenv import load_dotenv

load_dotenv()
dtoken = os.getenv('DKEY')

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        # Check if the message is from the bot itself
        if message.author == self.user:
            return

        print(f"Message from {message.author}: {message.content}")
        channel = message.channel
        await channel.send("Hi, I am Foodie-Bot")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(dtoken)
