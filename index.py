import discord
import asyncio
import time
import os

total_lines = 47768
total_frames = 3412

sw_file = open("ascii_movie/spacewars.txt", "r")

def get_frame():
	frame_delay = int(sw_file.readline().replace("\n", ""))/100
	frame = "```"
	for i in range(13):
		# print(i)
		frame += sw_file.readline()

	frame += "```"

	return [frame_delay, frame]

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$starwars'):
    	embed = discord.Embed(title="Sample Embed")
    	embed.set_image(url="https://images-ext-2.discordapp.net/external/cC-YBJkH2GXnX7MHMASUM9Gle1S1im3rDJj2K54A28w/%3Fcid%3D73b8f7b19a5ccc575679c0a7fc4a673b753e4ce993f35223%26rid%3Dgiphy.mp4/https/media2.giphy.com/media/Q8bEDnj9hZd6vivXSZ/giphy.mp4")
    	
    	msg = await message.channel.send(content="Loading...")

    	for _ in range(total_frames):
    		[frame_delay, frame] = get_frame()
    		frame_size = len(frame.replace("\n",""))

    		if(frame_size > 2):
	    		await asyncio.sleep(0.5)
	    		await msg.edit(content=frame)

client.run('')
