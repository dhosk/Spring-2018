import json
from urllib.parse import urlencode
from urllib.request import urlretrieve
import pandas as pd
import numpy as np
import requests
from lxml import html
import subprocess as sp
import re

def get_nba_data(endpoint, params, return_url=False):
    
    """Retrieves data from http://stats.nba.com
    
    For community documentation, visit 
    https://github.com/seemethere/nba_py/wiki/stats.nba.com-Endpoint-Documentation.
    
    Args:
        endpoint: endpoint specifies data table
        params: dictionary of parameters: e.g., {'LeagueID':'00'}
        return_url: returns URL instead of downloading data then returning it
    Returns:
        out: Pandas data frame
    """
    
    from pandas import DataFrame
    from urllib.parse import urlencode
    import json
    import subprocess as sp
    
    useragent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"
    dataurl = "http://stats.nba.com/stats/" + endpoint + "?" + urlencode(params)
    
    # for debugging: just return the url
    if return_url:
        return(dataurl)
    
    wgetout = sp.Popen(['wget', '-q', '-O', '-', '--user-agent='+useragent, dataurl], stdout=sp.PIPE)
    
    jsonstr, _ = wgetout.communicate()
    data = json.loads(jsonstr)
    
    h = data['resultSets'][0]['headers']
    d = data['resultSets'][0]['rowSet']
    
    out = DataFrame(d, columns=h)
    
    return(out)
## Credit to Sang-Yun Oh,
## Function taken from PSTAT_234 example code


def get_params(url):
    endpt = url.split('stats/')[1].split('?')[0]
    params = {}
    paramstring = url.split('stats/')[1].split('?')[1]

    for substring in paramstring.split("&"):
        variable = substring.split('=')[0]
        value = substring.split('=')[1]
        params.update({variable:value})
    return([endpt,params])
user_agent = "\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9\""

headers = {'User-Agent':user_agent}

def SportsRefCBBRowMaker(player_url,table_list,player_name,correct_year,player_id="0"):
    
    page = requests.get(player_url,headers=headers)
    tree = html.fromstring(page.content)
    
    if '404' in tree.xpath('//title')[0].text:
        return('404')
    else:
        year = tree.xpath('//table/tbody/tr')[-1].items()[0][-1][-4:]
        if(year!=correct_year):
            return(year)
        
        for i,table_name in enumerate(table_list):
            path = '//div[@id="'+table_name+'"]'
		## Table Name being something like all_players_advanced, players_per_game, etc.
            try:
                treeStr = str(tree.xpath(path)[0].getchildren()[-1])[8:-4]
		## There is a formatted html string for the table witin the larger html at this point
		## Need to remove some leading and trailing characters for python to properly interpert it 
            except:
                continue
            #This is tricky and comments might be nice here. 

            tree2 = html.fromstring(treeStr)

            valuesHTML = tree2.xpath('//table/tfoot/tr')[-1].getchildren()[1:]
            ## This gives career in particular 
            conf = tree2.xpath('//table/tbody/tr/td')[1].getchildren()[0].text
            colNamesHTML = tree2.xpath('//table/thead/tr/th')
            colNames = ["PLAYER_ID","PLAYER_NAME"]+["CONF"] + [col.text for col in colNamesHTML][1:]
            values = [player_id,player_name] + [conf] + [val.text for val in valuesHTML]
            if(i==0):
                row = pd.DataFrame(pd.Series(values,index=colNames)\
                    .dropna()).transpose()
            else:
                row = pd.merge(row,pd.DataFrame(pd.Series(values,index=colNames)\
                    .dropna()).transpose())
        return(row)
    
def sportsRefCBBTableMaker(player_df, table_list):
    base_url = 'https://www.sports-reference.com/cbb/players/'
    columns_df_url = "https://www.sports-reference.com/cbb/players/malcolm-brogdon-1.html"
    columns_df = SportsRefCBBRowMaker(columns_df_url,table_list
                                      ,"Malcolm Brogdon(2016)",'2016')
    CBB_df = pd.DataFrame(columns=columns_df.columns)
    for index,row in player_df.iterrows():
        player_name = row['PLAYER_NAME']
        first = re.sub('[^a-zA-Z]+', '',player_name.split()[0].lower())
        last = "".join(player_name.split()[1:])[0:-6].lower().strip(".")
        year = player_name.split()[1][-5:-1]
        name_url = base_url + first + "-" + last + "-"

        i = 1
        stopping_condition=False
        while(stopping_condition==False):
            data_url = name_url + str(i) + ".html"
#            print(data_url)
            row = SportsRefCBBRowMaker(data_url,table_list,player_name,year,player_id=index)
            if isinstance(row, pd.DataFrame):
                stopping_condition=True
                continue
            if(row=='404'):
                stopping_condition=True
                row = None
                if(last[-2:]=="jr"):
                    last = last[:-2]
                    name_url = base_url + first + "-" + last + "-"
                    i=1
                    stopping_condition = False 
            i+=1
        CBB_df = pd.concat([CBB_df,row])
    return(CBB_df)
