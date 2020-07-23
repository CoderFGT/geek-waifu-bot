#geek-waifu-bot source code
import discord

client = discord.Client()

@client.event
async def on_ready():
	print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	if message.content.startswith("$hello"):
		await message.channel.send(beer())

client.run('NzM1ODI3MzMxMTc1OTQwMTM4.Xxl62A.8fK-yheqoW3hKqGabBDtI3YmSKA')

#############################################
#Iron wall
#############################################

#module part
import random

def help():
	string = """

	Enter the help markdown text here

	"""
	return string

def bake():
	set1 = {":croissant:",":bagel:",":bread:",":pancakes:",":waffle:",":fortune_cookie:",":moon_cake:",":pie:",":cupcake:",":cake:",":birthday:",":pizza:",":doughnut:",":cookie:"}
	string1 = random.choice(set1)
	return string1

def cook():
	set2 = {":curry:"":spaghetti:",":ramen:",":stew:",":curry:"," :bacon:",":cut_of_meat:",":poultry_leg:",":meat_on_bone:",":hotdog:",":hamburger:",":fries:",":shallow_pan_of_food:"}
	string2 = random.choice(set2)
	return string2

def beer():
	return ":beer:"