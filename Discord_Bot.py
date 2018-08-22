import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

from Stats_Getter import *
from Standings_Retriever import *
from Results_Retriever import game_results

import datetime
    
#<Issue for player played with multiple teams> - FIXED ALMOST
#<Issue with iphone users '> 
#<Issue with Luc Mbah A Moute> 


#Games which are on for tonight
#League leaders
#Assign roles as team names 



TOKEN = 'NDc0NjYyNzUwMTk1Mjg2MDE2.DkT2nA.IJgCY6pm917ZHJcNd01dM_Ublsk'

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
        await client.send_message(channel , '<< !stats firstname lastname >> - Regular Season Stats Of Player\n'
                                            '<< !twit firstname lastname >>   - Twitter Account Of Player\n'
                                            '<< !open firstname lastname >> - Open Stats Page Of Player\n'
                                            '<< !standings conference >> - Display Current Standings of Conference\n'
                                            '<< !results date month year >> - Display Game Day Results of entered date'
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

        
        if msg[1].lower()   == "east":
            await client.send_message(channel , standings("east"))
        
        elif msg[1].lower() == "west":
            await client.send_message(channel , standings("west"))


    elif message.content.startswith('!results'):
        msg = message.content.split(' ')
        date  = msg[1] 
        month = msg[2]
        year  = msg[3] 

        await client.send_message(channel , game_results(month , date , year))

    elif message.content == ('!yesterday'):
        yest_date = str(datetime.date.today()-datetime.timedelta(1))

        yest_year , yest_month , yest_date = yest_date.split('-')
        print(f"Finding results for matches played on {yest_date}/{yest_month}/{yest_year}")

        try:
            await client.send_message(channel , game_results(yest_month , yest_date , yest_year))
        except AttributeError:
            await client.send_message(channel , "No Matches Were Played Yesterday")

    #Allow user to see a player's stats in discord channel

    elif message.content.startswith('!stats'):

        msg = message.content.split(' ')
        first_name,last_name  =  msg[1] , msg[2]
        

        embed = discord.Embed(
        title = 'STATS',
        description = f'{first_name.upper()} {last_name.upper()}',
        colour = discord.Colour.blue()
        )



        embed.set_footer(text = url_needer(first_name,last_name))
        #embed.set_image(url = 'http://news.sportslogos.net/2017/07/07/nba-makes-change-to-league-logo/new-nba-logo-2/')
        #embed.set_thumbnail(url = 'data:image/png;base64,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')
        #embed.set_author(name = "Retarded Rhino" , icon_url = 'data:image/png;base64,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')
        things = stat_getter(first_name , last_name)
        if things == False:
            await client.send_message(channel , "Player Not Found")
            return

        ppg = ' '.join(things[0])#[float(i) for i in things[0]]
        apg = ' '.join(things[1])#[float(i) for i in things[1]]
        rpg = ' '.join(things[2])#[float(i) for i in things[2]]
        if things[3] != []:
            spg = ' '.join(things[3])#[float(i) for i in things[3]]
        else:
            spg = [0]
        if things[4] != []:
            bpg = ' '.join(things[4])#[float(i) for i in things[4]]
        else:
            bpg = [0]

        fg =  ' '.join(things[5])#[float(i) for i in things[5]]

        embed.add_field(name = 'PPG' , value = ppg , inline = False)
        embed.add_field(name = 'APG' , value = apg , inline = False)
        embed.add_field(name = 'RPG' , value = rpg , inline = False)
        embed.add_field(name = 'SPG' , value = spg , inline = False)
        embed.add_field(name = 'BPG' , value = bpg , inline = False)
        embed.add_field(name = 'FG'  , value = fg  , inline = False)
        #await self.bot.say(embed = embed)
        await client.send_message(channel , embed = embed)

    elif message.content.startswith('!twit'):
        msg = message.content.split(' ')
        first_name , last_name = msg[1] , msg[2]
        await client.send_message(channel , tweet_getter(first_name , last_name))


    
    elif message.content.startswith('!team'):
        msg = message.content.split(' ')
        team_name = msg[1]
        existing_role = discord.utils.get(author.server.roles , name = team_name)
        new_role = discord.utils.get(author.server.roles, name = team_name)
        await client.add_roles(author , new_role)


                                      

@client.event
async def on_message_delete(message):

    author = message.author
    content = message.content
    channel = message.channel
    print("The following message was deleted by {} - {}".format(author , content))
    # await client.send_message(channel , "Message was deleted")


        
client.run(TOKEN)
