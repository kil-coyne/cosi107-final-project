botToken = 'MTIyNzMzNzQ1NzEyMTYyODI2MA.GA06kA.EXnNS0CCCdMqZ4NjXDORXUBWerDtjcvBBW2L5E'
botMaster = 'cosi107'
import discord
import subprocess
import os

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_message(message):

    if message.content:
        if str(message.author) == botMaster:
        
            command = str(message.content)
            print(command)
            
            # dir change must be the first command
            if command[0:2] == 'cd':
            	command_lst = command.split()
            	os.chdir(command_lst[1])
            	command = ' '.join(command_lst[2:])
            	print(command)
            	
            output = subprocess.getoutput(command)
            msg = 'Command granted by {0.author.mention}\n{1}'.format(message, output)
#            await client.send_message(message.channel, msg)
            await message.channel.send(msg)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(botToken)
