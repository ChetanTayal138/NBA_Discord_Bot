import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

from Stats_Getter import *
from Standings_Retriever import *
from Results_Retriever import game_results
from Playoffs import *
from Embeder import embeder

import datetime
    
#<Issue for player played with multiple teams> - FIXED ALMOST
#<Issue with iphone users '> 
#<Issue with Luc Mbah A Moute> 
#<Issue with Photos in thumbnails due to different name lengths

###Games which are on for tonight
###League leaders




TOKEN = 'XXX'

client = commands.Bot(command_prefix = '!')


@client.event 
async def on_ready():
    print("Bot is ready")

@client.event 
async def on_member_join(member):
    await client.send_message(client.get_channel('474671567801155586') , f"Welcome {member.mention}. Type !commands to see all currently available commands that can be used for the bot. Send a message to RetardedRhino to report any bugs. Thanks")


@client.event
async def on_message(message):

    author  = message.author
    channel = message.channel
    content = message.content
    print("{} : {}".format(author , content))
     

    if message.content.startswith('!commands'):
        await client.send_message(channel , '<< !stats firstname lastname rs/ra/ps/pa>> - Stats Of Player\n'
                                            '<< !twit firstname lastname >>   - Twitter Account Of Player\n'
                                            '<< !open firstname lastname >> - Open Stats Page Of Player\n'
                                            '<< !standings conference >> - Display Current Standings of Conference\n'
                                            '<< !results date month year >> - Display Game Day Results of entered date\n'
                                            '<< !team teamname >> - Assigns You Your Team as Role '
                                            )

    

    elif message.content.startswith('!open'):
        msg = message.content.split(' ')
        first_name = msg[1]
        last_name  = msg[2]
        await client.send_message(channel , stats_page_opener(first_name , last_name))

    elif message.content.startswith('!SLAM'):
        await client.send_message(channel , 'DUNK!')

    elif message.content.startswith('!standings'):
        msg = message.content.split(' ')
        
        east_team_names = []
        west_team_names = []

        east_team_record = []
        west_team_record = []  

        standings_getter()

        embed = discord.Embed(
        title = 'STANDINGS',
        description = '',
        colour = discord.Colour.green()
        )


        if msg[1].lower() == "east":
            embed.add_field(name = 'EAST' , value = standings('east'))
            await client.send_message(channel , embed = embed)
        
        elif msg[1].lower() == "west":
            embed.add_field(name = 'WEST' , value = standings('west'))
            await client.send_message(channel , embed = embed)


    elif message.content.startswith('!results'):
        msg = message.content.split(' ')
        date  = msg[1] 
        month = msg[2]
        year  = msg[3] 

        embed = discord.Embed(
        title = 'RESULTS',
        description = '',
        colour = discord.Colour.red()
        )
         
        embed.add_field(name = f'{date}/{month}/{year}' , value = game_results(month , date , year))
        await client.send_message(channel , embed = embed)#game_results(month , date , year))

    elif message.content == ('!yesterday'):
        yest_date = str(datetime.date.today()-datetime.timedelta(1))

        yest_year , yest_month , yest_date = yest_date.split('-')
        print(f"Finding results for matches played on {yest_date}/{yest_month}/{yest_year}")

        try:
            await client.send_message(channel , game_results(yest_month , yest_date , yest_year))
        except AttributeError:
            await client.send_message(channel , "No Matches Were Played Yesterday")

    

            



    elif message.content.startswith('!twit'):
        msg = message.content.split(' ')
        first_name , last_name = msg[1] , msg[2]
        await client.send_message(channel , tweet_getter(first_name , last_name))


    
    elif message.content.startswith('!team'):
        msg = message.content.split(' ')
        team_name = msg[1]
        new_role = discord.utils.get(author.server.roles, name = team_name)
        await client.replace_roles(author , new_role)





    #Allow user to see a player's stats in discord channel

    elif message.content.startswith('!stats'):

        msg = message.content.split(' ')
        first_name,last_name  =  msg[1] , msg[2]
        type_of_stats = msg[3]
    
        if type_of_stats == 'rs':
            things = stat_getter(first_name , last_name)

        elif type_of_stats == 'ra':
            things = advanced_getter(first_name , last_name)

        elif type_of_stats == 'ps':
            things = playoffs_stat_getter(first_name , last_name)

        elif type_of_stats == 'pa':
            things = playoffs_advanced_getter(first_name , last_name)

        

        if things == False:
            await client.send_message(channel , "Player Not Found")
            return

        first = ' '.join(things[0])#[float(i) for i in things[0]]
        second = ' '.join(things[1])#[float(i) for i in things[1]]
        third = ' '.join(things[2])#[float(i) for i in things[2]]
        if things[3] != []:
            fourth = ' '.join(things[3])#[float(i) for i in things[3]]
        else:
            fourth = ['Stats Not Available For This Category']
        if things[4] != []:
            fifth = ' '.join(things[4])#[float(i) for i in things[4]]
        else:
            fifth =  ['Stats Not Available For This Category']

        sixth =  ' '.join(things[5])#[float(i) for i in things[5]]

        attributes = {1:first , 2:second , 3:third , 4:fourth , 5:fifth , 6:sixth}
        stats_embed = embeder(type_of_stats , attributes , first_name , last_name)
        await client.send_message(channel , embed = stats_embed)



                                      

@client.event
async def on_message_delete(message):

    author = message.author
    content = message.content
    channel = message.channel
    print("The following message was deleted by {} - {}".format(author , content))
    # await client.send_message(channel , "Message was deleted")

@client.event
async def on_reaction_add(reaction , user):

    channel = reaction.message.channel
    await client.send_message(channel , f'{user.name} has added {reaction.emoji} to the message: {reaction.message.content}')

@client.event
async def on_reaction_remove(reaction , user):
    channel = reaction.message.channel
    await client.send_message(channel , f'{user.name} has removed {reaction.emoji} from the message: {reaction.message.content}')

    
    
client.run(TOKEN)
