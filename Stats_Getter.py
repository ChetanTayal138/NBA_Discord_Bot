import requests
from bs4 import BeautifulSoup
from pprint import pprint
import re 


def make_soup(url):
    #Making a soup object by creating a response object using requests.get and then getting html_content from res.text
    res = requests.get(url)
    html_content = res.text
    soup_object = BeautifulSoup(html_content , "html.parser") #Allows to parse the html_content with help of BeautifulSoup
    return soup_object
   



# def stats_converter(stat_list):
#     actual_stats = []
     
#     for i in stat_list:
#         if i.text == '':
#             break
#         else:
#             actual_stats.append(i.text)

#     return actual_stats

def url_checker(first_name , last_name):
    for i in range(1,5):
        
        if "'" in first_name:
            url = ("https://www.basketball-reference.com/players/{}/{}{}{}0{}.html").format(last_name[0].lower(), last_name[:5].lower(), first_name[0].lower() , first_name[2].lower(), i)
        
        elif "'" in last_name:
            url = ("https://www.basketball-reference.com/players/{}/{}{}{}0{}.html").format(last_name[0].lower(),last_name[0].lower(), last_name[2:6].lower(), first_name[:2].lower() , i)
        
        else:
            url = ("https://www.basketball-reference.com/players/{}/{}{}0{}.html").format(last_name[0].lower(), last_name[:5].lower(), first_name[:2].lower() , i)
        
        soup = make_soup(url) #Uses the first function to generate required URL
        name_check = soup.select('h1')[0].text.strip().lower()
        if name_check == ("{} {}".format(first_name.lower() , last_name.lower())):
            return soup
        else:
            continue
     
    return False



def picture_getter(first_name , last_name):
    for i in range(1,5):
        
        if "'" in first_name:
            url = ("https://www.basketball-reference.com/players/{}/{}{}{}0{}.html").format(last_name[0].lower(), last_name[:5].lower(), first_name[0].lower() , first_name[2].lower(), i)
        
        elif "'" in last_name:
            url = ("https://www.basketball-reference.com/players/{}/{}{}{}0{}.html").format(last_name[0].lower(),last_name[0].lower(), last_name[2:6].lower(), first_name[:2].lower() , i)
        
        else:
            url = ("https://www.basketball-reference.com/players/{}/{}{}0{}.html").format(last_name[0].lower(), last_name[:5].lower(), first_name[:2].lower() , i)
        
        soup = make_soup(url) #Uses the first function to generate required URL
        name_check = soup.select('h1')[0].text.strip().lower()
        if name_check == ("{} {}".format(first_name.lower() , last_name.lower())):
            return ("https://d2cwpp38twqe55.cloudfront.net/req/201807091/images/players/{}.jpg").format(url[47:56])



def stat_getter(first_name , last_name):
    
    print("Finding Stats For {} {}".format(first_name , last_name))
    points_per_game  = []
    assists_per_game = []
    rebounds_per_game = []
    steals_per_game = []
    blocks_per_game = []
    percent_per_game = []

    soup = url_checker(first_name , last_name)
    try:
        '''points_per_game   = soup.findAll('td' , {"data-stat" : "pts_per_g"})
        assists_per_game  = soup.findAll('td' , {"data-stat" : "ast_per_g"})
        rebounds_per_game = soup.findAll('td' , {"data-stat" : "trb_per_g"})
        steals_per_game   = soup.findAll('td' , {"data-stat" : "stl_per_g"})
        blocks_per_game   = soup.findAll('td' , {"data-stat" : "blk_per_g"})
        percent_per_game  = soup.findAll('td' , {"data-stat" : "fg_pct"})'''
        
        stats_table = soup.find('div' , {'id' : 'div_per_game'})
        stats_row = stats_table.findAll('tr')
        #return stats_row[1:]

        for row in stats_row[1:]:
            if row.text == '':
                break
            #ppg = row.find('td' , {"data-stat" : "pts_per_g"})
            #print(ppg.text)
            #apg = stats_row.find('td' , {"data-stat" : "pts_per_g"})
            #rpg = stats_row.find('td' , {"data-stat" : "pts_per_g"})

            points_per_game.append(row.find('td' , {"data-stat" : "pts_per_g"}))
            assists_per_game.append(row.find('td' , {"data-stat" : "ast_per_g"}))
            rebounds_per_game.append(row.find('td' , {"data-stat" : "trb_per_g"}))
            steals_per_game.append(row.find('td' , {"data-stat" : "stl_per_g"}))
            blocks_per_game.append(row.find('td' , {"data-stat" : "blk_per_g"}))
            percent_per_game.append(row.find('td' , {"data-stat" : "fg_pct"}))


           



        
    except AttributeError:
        return False
   
    if points_per_game == []:
        return False
    
    #if steals_per_game or blocks_per_game == []:
        #things = [[(i.text) for i in points_per_game] , [(i.text) for i in assists_per_game] , [(i.text) for i in rebounds_per_game] , [] ,[] , [(i.text) for i in percent_per_game]]
    #else:
    #things = [ [(i.text) for i in points_per_game] , [(i.text) for i in assists_per_game] , [(i.text) for i in rebounds_per_game] , [(i.text) for i in steals_per_game if i != []] ,[(i.text) for i in blocks_per_game if i != []] , [(i.text) for i in percent_per_game]]
    somethings  = []

    somethings.append([(i.text) for i in points_per_game])
    somethings.append([(i.text) for i in assists_per_game])
    somethings.append([(i.text) for i in rebounds_per_game])
    try:
        somethings.append([(i.text) for i in steals_per_game])
        somethings.append([(i.text) for i in blocks_per_game])
        

    except AttributeError:
        somethings.append([])
        somethings.append([])

    somethings.append([(i.text) for i in percent_per_game])

    return somethings

    # PPG = stats_converter(points_per_game[:-1])   
    # APG = stats_converter(assists_per_game[:-1])   
    # RPG = stats_converter(rebounds_per_game[:-1])  
    # SPG = stats_converter(steals_per_game[:-1])    
    # BPG = stats_converter(blocks_per_game[:-1])    
    # FG  = stats_converter(percent_per_game[:-1])
             
    # #return (f"PPG - {[float(i) for i in PPG]}\nAPG - {[float(i) for i in APG]}\nRPG - {[float(i) for i in RPG]}\nSPG - {[float(i) for i in SPG]}\nBPG - {[float(i) for i in BPG]}\nFG% - {[float(i) for i in FG]}")
    # things =  [PPG,APG,RPG,SPG,BPG,FG]
    # return things

def tweet_getter(first_name , last_name):

    print("Finding twitter account for {} {}".format(first_name , last_name))
     
    soup = url_checker(first_name , last_name)
    try:
        links = soup.findAll('a' , attrs = {'href' : re.compile('^https://')})
    except AttributeError:
        return "Player Not Found"

    all_links = []
    for link in links:
        all_links.append(link.get('href'))
    if "twitter.com" not in all_links[12]:
        return "Player does not have a twitter account"
    return all_links[12]
   
def url_needer(first_name , last_name):
    for i in range(1,6):
        
        if "'" in first_name:
            url = ("https://www.basketball-reference.com/players/{}/{}{}{}0{}.html").format(last_name[0].lower(), last_name[:5].lower(), first_name[0].lower() , first_name[2].lower(), i)
        
        elif "'" in last_name:
            url = ("https://www.basketball-reference.com/players/{}/{}{}{}0{}.html").format(last_name[0].lower(),last_name[0].lower(), last_name[2:6].lower(), first_name[:2].lower() , i)

        else:
            url = ("https://www.basketball-reference.com/players/{}/{}{}0{}.html").format(last_name[0].lower(), last_name[:5].lower(), first_name[:2].lower() , i)
    

        soup = make_soup(url) #Uses the first function to generate required URL
        name_check = soup.select('h1')[0].text.strip().lower()
        #print(name_check)
        if name_check == ("{} {}".format(first_name.lower() , last_name.lower())):
            break
        else:
            continue

    #webbrowser.open(url)
    return url

def stats_page_opener(first_name , last_name):
    
    print("Finding Page for {} {}".format(first_name , last_name))
    return url_needer(first_name , last_name)
    
#print(url_checker("kobe"  , "bryant"))
#print(stat_getter("Kevin" , "Durant"))
#print(stat_getter("Wilt" , "Chamberlain"))


#stats_page_opener("kobe" , "bryant")


#print(picture_getter('rudy','gay'))