import re
import sys
sys.dont_write_bytecode = True

import discord
import os
from dotenv import load_dotenv
from keep_alive import keep_alive
from prompter import suggest_foods


load_dotenv()
dtoken = os.getenv("DKEY")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

    async def on_message(self, message):
        # Check if the message is from the bot itself
        if message.author == self.user:
            return


        print(f"Message from {message.author}: {message.content}")
        channel = message.channel
        if self.user.mentioned_in(message):
            cleanedmsg = re.sub(r'<.*?>', '', message.content)
            user_ingredients = [ingredient.strip() for ingredient in cleanedmsg.split(',')]
            suggested_foods = suggest_foods(user_ingredients)
            await channel.send("Here are some foods you can make with those ingredients:")
            for food in suggested_foods:
                #print("- " + food)
                await channel.send("- " + food)


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
keep_alive()
client.run(dtoken)
