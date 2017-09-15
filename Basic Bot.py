# These are the dependecies. The bot depends on these to function, hence the name. Please do not change these unless your adding to them.
import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands

# Here you can modify the bot's prefix and description and wether it sends help in direct messages or not.
client = Bot(description="Basic Bot by Habchy#1665", command_prefix="PUT YOUR PREFIX HERE", pm_help = True)

# This is what happens everytime the bot launches. In this case, it prints information like server count, user count the bot is connected to, and the bot id in the console.
@client.event
async def on_ready():
	print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
	print('--------')
	print('Support Discord Server: https://discord.gg/FNNNgqb')
	print('--------')
	print('Created by Habchy#1665')

# This is a basic example of a call and response command. You tell it do "this" and it does it.
@client.command()
async def ping(*args):

	await client.say(":ping_pong: Pong!")
	await asyncio.sleep(3)
	await client.say(":warning: This bot was created by **Habchy#1665**, it seems that you have not modified it yet. Go edit the file and try it out!")
# After you have modified the code, feel free to delete the line above (line 25) so it does not keep popping up everytime you initiate the ping commmand.
	
client.run('PUT YOUR BOT TOKEN HERE')

# Basic Bot was created by Habchy#1665
# Please join this Discord server if you need help: https://discord.gg/FNNNgqb
# Please modify the parts of the code where it asks you to. Example: The Prefix or The Bot Token
# This is by no means a full bot, it's more of a starter to show you what the python language can do in Discord.
# Thank you for using this and don't forget to star my repo on GitHub!

# The help command is currently set to be Direct Messaged.
# If you would like to change that, change "pm_help = True" to "pm_help = False" on line 14.
