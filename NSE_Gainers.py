# Developed by Karthikeyan G
# version 1.0
# fetch the gainers data from NSE website and triggers message onto telegram group with the top gainers data

import requests
import json
import pandas as pd
import requests
from tabulate import tabulate
import time

# getting the data from NSE website
headers = {'User-Agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
nse_url_gainers = 'https://www.nseindia.com/api/live-analysis-variations?index=gainers'
nse_url_losers = 'https://www.nseindia.com/api/live-analysis-variations?index=losers'
time.sleep(4)
gainers = requests.get(nse_url_gainers,headers=headers,verify=False)
time.sleep(4)
print(gainers.status_code)
if(gainers.status_code == 200):
    gainers_text = gainers.text;
    json_object = json.loads(gainers_text);
    
    #constructing the NIFTY top 5 gainers
    nifty50_gain = pd.DataFrame.from_dict((json_object['NIFTY'])['data']);
    nifty50_gain = nifty50_gain.sort_values(['perChange'],ascending=False);
    nifty50_gain_top5 = nifty50_gain.loc[0:4,["symbol","perChange"]];

    #constructing top 10 gainers in all securities
    all_secu_gain = pd.DataFrame.from_dict(json_object['allSec']['data'])
    all_secu_gain = all_secu_gain.sort_values(['perChange'],ascending=False)
    all_secu_gain_top10 = all_secu_gain.loc[0:9,["symbol","perChange"]]

    json_object['FOSec']['data']
    #constructing top 10 gainers in FnO securities
    fno_secu_gain = pd.DataFrame.from_dict(json_object['FOSec']['data'])
    fno_secu_gain = fno_secu_gain.sort_values(['perChange'],ascending=False)
    fno_secu_gain_top10 = fno_secu_gain.loc[0:9,["symbol","perChange"]]

    # Constructing the message and sending onto telegram group with chatid and token id
    payload = {
        'chat_id': '*************',
        'text': f"""``` Top 5 Gainers in NIFTY50\n{tabulate(nifty50_gain_top5, headers = 'keys', tablefmt = 'pretty')}\n\n\nTop 10 Gainers in FnO Category\n{tabulate(fno_secu_gain_top10, headers = 'keys', tablefmt = 'pretty')}\n\n\nTop 10 Gainers in all securities\n{tabulate(all_secu_gain_top10, headers = 'keys', tablefmt = 'pretty')}```""",
        'parse_mode': 'MarkdownV2'}
    tokenid = '*****************'
    url = f'https://api.telegram.org/bot{tokenid}/sendmessage'
    requests.post(url,data=payload,verify=False)
else:
    print("Could not fetch the data")

