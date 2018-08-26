from Stats_Getter import picture_getter
from Stats_Getter import url_needer

import discord
from discord.ext import commands

def embeder(type_stats , attributes , first_name , last_name):
    normal_stats   = {1:'PPG' , 2:'APG' , 3:'RPG' , 4:'SPG' , 5:'BPG' , 6:'FG%'}
    advanced_stats = {1:'PER' , 2:'TS%' , 3:'WS' , 4:'WS/48' ,5:'BPM' , 6:'VORP'}
    
    
    
    nba_embed = discord.Embed(
    title = 'STATS',
    description = '',
    colour = discord.Colour.red()
    )
     
    title = 'STATS',
    description = f'{first_name.upper()} {last_name.upper()}',
    colour = discord.Colour.blue()
    


    if type_stats == 'rs' or type_stats == 'ps':
        for i in range(1,7):
            nba_embed.add_field(name = normal_stats[i] , value = attributes[i]   , inline = False)


    elif type_stats == 'ra' or type_stats == 'pa':
        for i in range(1,7):
            nba_embed.add_field(name = advanced_stats[i] , value = attributes[i] , inline = False)

 
       


    nba_embed.set_footer(text = url_needer(first_name,last_name))
    #embed.set_image(url = 'https://d2p3bygnnzw9w3.cloudfront.net/req/201807242/logos/bbr-logo.svg')
    nba_embed.set_thumbnail(url =  picture_getter(first_name , last_name))
    nba_embed.set_author(name = "NBA")

    
    


    return nba_embed