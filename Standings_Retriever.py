from bs4 import BeautifulSoup
import requests
from pprint import pprint

east_team_names = []
west_team_names = []

east_team_record = []
west_team_record = []

def standings_getter():
    east_team_names.clear()
    west_team_names.clear()
    east_team_record.clear()
    west_team_record.clear()
        
    url = "https://www.basketball-reference.com"
    res = requests.get(url)
    html_content = res.text
    soup = BeautifulSoup(html_content , "html.parser")

    east_table = soup.find('div' , {"id":"all_confs_standings_E"})
    west_table = soup.find('div' , {"id":"all_confs_standings_W"})

    west_rows = west_table.findAll('tr' , {"class" : "full_table"})
    east_rows = east_table.findAll('tr' , {"class" : "full_table"})




    for row in west_rows:
        names = row.find('th' , {"data-stat" : "team_name"})
        wins = row.find('td' , {"data-stat":"wins"})
        losses = row.find('td' , {"data-stat":"losses"})
        west_team_record.append([wins.text , losses.text])
        west_team_names.append(names.text[:3])

    for row in east_rows:
        names = row.find('th' , {"data-stat" : "team_name"})
        wins = row.find('td' , {"data-stat":"wins"})
        losses = row.find('td' , {"data-stat":"losses"})
        east_team_record.append([wins.text , losses.text])
        east_team_names.append(names.text[:3])


# # for row in west_rows:
# #     some1 = row.find('td' , {"data-stat":"wins"})
# #     some2 = row.find('td' , {"data-stat":"losses"})
# #     west_team_record.append([some1.text , some2.text])


# for row in east_rows:
#     some1 = row.find('td' , {"data-stat":"wins"})
#     some2 = row.find('td' , {"data-stat":"losses"})
#     east_team_record.append([some1.text , some2.text])


def standings(conference):
    content = []
    if conference == "east":
        for i in range(15):
            content.append("{} {}-{}".format(east_team_names[i] , east_team_record[i][0] , east_team_record[i][1]))
        

        return '\n'.join(content)
        

    elif conference == "west":
        for i in range(15):
            content.append("{} {}-{}".format(west_team_names[i] , west_team_record[i][0] , west_team_record[i][1]))
        
        return '\n'.join(content)
        

