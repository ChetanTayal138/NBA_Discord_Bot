from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import requests

def make_soup(url):
    #Making a soup object by creating a response object using requests.get and then getting html_content from res.text
    res = requests.get(url)
    html_content = res.text
    soup_object = BeautifulSoup(html_content , "html.parser") #Allows to parse the html_content with help of BeautifulSoup
    return soup_object

def other_soup_maker(url):
    options = Options()
    options.add_argument('--headless')
    browser = webdriver.Chrome(options = options)
    url = browser.get(url)
    innerHTML = browser.execute_script("return document.body.innerHTML")
    soup = BeautifulSoup(innerHTML , 'html.parser')
    return soup

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


def playoffs_advanced_getter(first_name , last_name):
    player_url = url_needer(first_name , last_name)
    soup_object = other_soup_maker(player_url)
    ppg_pf_adv = []
    apg_pf_adv = []
    rpg_pf_adv = []
    spg_pf_adv = []
    bpg_pf_adv = []
    fg_pf_adv  = []

    playoffs = soup_object.find("div" , {"id":"div_playoffs_advanced"})
    playoff_years  = playoffs.findAll('tr')

    try:
        for year in playoff_years[1:]:
            ppg = year.find('td' , {'data-stat':'per'})
            apg = year.find('td' , {'data-stat':'ts_pct'})
            rpg = year.find('td' , {'data-stat':'ws'})
            spg = year.find('td' , {'data-stat':'ws_per_48'})
            bpg = year.find('td' , {'data-stat':'bpm'})
            fg  = year.find('td' , {'data-stat':'vorp'})

            ppg_pf_adv.append(ppg.text)
            apg_pf_adv.append(apg.text)
            rpg_pf_adv.append(rpg.text)
            spg_pf_adv.append(spg.text)
            bpg_pf_adv.append(bpg.text)
            fg_pf_adv.append(fg.text)
    
    except AttributeError:
            return False

    
    things =  [ppg_pf_adv , apg_pf_adv , rpg_pf_adv , spg_pf_adv , bpg_pf_adv , fg_pf_adv]
    return things



def advanced_getter(first_name , last_name):
    player_url = url_needer(first_name , last_name)
    soup_object = other_soup_maker(player_url)
    ppg_adv = []
    apg_adv = []
    rpg_adv = []
    spg_adv = []
    bpg_adv = []
    fg_adv  = []

    playoffs = soup_object.find("div" , {"id":"div_advanced"})
    playoff_years  = playoffs.findAll('tr')

    
    try:
        for year in playoff_years[1:]:
            ppg = year.find('td' , {'data-stat':'per'})
            apg = year.find('td' , {'data-stat':'ts_pct'})
            rpg = year.find('td' , {'data-stat':'ws'})
            spg = year.find('td' , {'data-stat':'ws_per_48'})
            bpg = year.find('td' , {'data-stat':'bpm'})
            fg  = year.find('td' , {'data-stat':'vorp'})

            ppg_adv.append(ppg.text)
            apg_adv.append(apg.text)
            rpg_adv.append(rpg.text)
            spg_adv.append(spg.text)
            bpg_adv.append(bpg.text)
            fg_adv.append(fg.text)

    except AttributeError:
        return False


    things = [ppg_adv ,apg_adv,rpg_adv,spg_adv,bpg_adv,fg_adv]
    return things




def playoffs_stat_getter(first_name , last_name):
    player_url = url_needer(first_name , last_name)
    soup_object = other_soup_maker(player_url)
    ppg_pf = []
    apg_pf = []
    rpg_pf = []
    spg_pf = []
    bpg_pf = []
    fg_pf  = []

    playoffs = soup_object.find("div" , {"id":"div_playoffs_per_game"})
    playoff_years  = playoffs.findAll('tr')

    try:
        for year in playoff_years[1:]:
            ppg = year.find('td' , {'data-stat':'pts_per_g'})
            apg = year.find('td' , {'data-stat':'ast_per_g'})
            rpg = year.find('td' , {'data-stat':'trb_per_g'})
            spg = year.find('td' , {'data-stat':'stl_per_g'})
            bpg = year.find('td' , {'data-stat':'blk_per_g'})
            fg  = year.find('td' , {'data-stat':'fg_pct'})

            ppg_pf.append(ppg.text)
            apg_pf.append(apg.text)
            rpg_pf.append(rpg.text)
            spg_pf.append(spg.text)
            bpg_pf.append(bpg.text)
            fg_pf.append(fg.text)

    except AttributeError:
        return False


    things =  [ppg_pf , apg_pf , rpg_pf , spg_pf , bpg_pf, fg_pf]
    return things



#print('\n'.join(playoffs_stat_getter('kevin' , 'durant')))
#print('\n'.join(playoffs_advanced_getter('kevin' , 'durant')))
#print('\n'.join(advanced_getter('kevin' , 'durant')))