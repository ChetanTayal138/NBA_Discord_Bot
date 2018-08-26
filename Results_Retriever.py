from bs4 import BeautifulSoup
import requests

import datetime

results = []



def make_soup(month , date , year):
    url = f"https://www.basketball-reference.com/boxscores/?month={month}&day={date}&year={year}"
    res = requests.get(url)
    html_content = res.text
    soup_object = BeautifulSoup(html_content , "html.parser")
    return soup_object








def game_results(month , date , year):
    results.clear()

    soup = make_soup(month , date , year)
    all_games = soup.find("div" , {"class":"game_summaries"})
    try:
        games_row = all_games.findAll("div" , {"class":"game_summary expanded nohover"})
    except AttributeError:
        return "No Matches On This Day"

    for game in games_row:
        game_result = game.find("tbody")

        winner = game_result.find("tr",{"class":"winner"})
        winner_name  = winner.find("td")
        winner_score = winner.find("td",{"class":"right"})
        winner_score = winner_score.text

        loser  = game_result.find("tr",{"class":"loser"})
        loser_name  = loser.find("td")
        loser_score = loser.find("td", {"class":"right"})
        loser_score = loser_score.text
        
    
        results.append(f"{winner_name.text.upper()} {winner_score}   -   {loser_name.text.upper()} {loser_score}")
        
    return '\n\n'.join(results)


#print(game_results(year , month , date))
