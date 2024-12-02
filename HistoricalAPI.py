import datetime
import pandas as pd
df = pd.DataFrame(columns = ['timestamp','Open','High','Low','Close','Volume'])
historicParam={
        "exchange": "NSE",
        "symboltoken": "99926000",
        "interval": "ONE_DAY",
        "fromdate": "2014-01-01 09:00", 
        "todate":  "2017-12-31 18:00"
        }
data_historical = smartApi.getCandleData(historicParam)
res_json = data_historical
df_new = pd.DataFrame(res_json['data'],columns=['timestamp','Open','High','Low','Close','Volume'])
df_new['timestamp'] = pd.to_datetime(df_new['timestamp'],format = '%Y-%m-%dT%H:%M:%S'+'+05:30')

## To Calculate Daily Returns ##
# 6th Column is added to return daily returns
for i in range(1,df.index.stop,df.index.step):
    df.iloc[i,6] = round(((df.iloc[i,4] - df.iloc[i-1,4])/df.iloc[i-1,4])*100,2)
print(df)
