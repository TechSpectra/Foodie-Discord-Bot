import re
import sys
sys.dont_write_bytecode = True

import nextcord
from nextcord import Interaction
from nextcord.ext import commands
import os
from dotenv import load_dotenv
from prompter import suggest_foods


load_dotenv()
dtoken = os.getenv("DKEY")


intents = nextcord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print(f"Logged on as {client.user}!")

res=""

testserverId = 1106837576964390994

@client.slash_command(name="test" , description="gives you food according to ingredients")
async def test(interaction: Interaction, question: str):
    print(question)
    cleanedmsg = re.sub(r'<.*?>', '', question)
    user_ingredients = [ingredient.strip() for ingredient in cleanedmsg.split(',')]
    suggested_foods = suggest_foods(user_ingredients)
    res = "" 
    for food in suggested_foods:
        res += "- " + food + "\n"
    await interaction.response.send_message("Here are some foods you can make with those ingredients:\n" + res)


client.run(dtoken)