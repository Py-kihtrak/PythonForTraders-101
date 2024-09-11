
api_key = 'YOUR_API_KEY'
clientId = 'ANGEL_CLIENT_ID'
pwd = 'ANGEL_LOGIN_PASSWORD'
token = 'API_TOKEN'

## ANGLE ONE LOGIN  & ACCOUNT SETUP
from SmartApi import SmartConnect
import pyotp
totp = pyotp.TOTP(token).now()
smartApi = SmartConnect(api_key,disable_ssl=True)
data = smartApi.generateSession(clientId, pwd, totp)
if data['status'] == False:
    logger.error(data)
else:
    authToken = data['data']['jwtToken']
    refreshToken = data['data']['refreshToken']

## GET LIST OF ALL TRADABLE INSTRUMENTS. TOKEN IS REQUIRED TO PLACE ORDER.
url = "https://margincalculator.angelbroking.com/OpenAPI_File/files/OpenAPIScripMaster.json"
import pandas as pd
dump = pd.read_json(url)
dump.to_excel("Tradable_Instruments.xlsx") ## SAVE TO EXCEL FOR FUTURE REFERENCES


## PLACING ORDER USING ANGLE ONE API
orderparams = {
    "variety": "NORMAL",
    "tradingsymbol": 'SYMBOL FROM ABOVE DUMP'],
    "symboltoken": 'TOKEN FROM ABOVE DUMP',
    "transactiontype": "BUY",
    "exchange": "NSE",
    "ordertype": "LIMIT",
    "producttype": "INTRADAY",
    "duration": "DAY",
    "price": "195",
    "quantity": "10"
    }
orderid = smartApi.placeOrder(orderparams)


## ANGLE ONE LOG OUT OR TERMINATE SESSION
try:
    logout=smartApi.terminateSession('ClientID')
    print("Logout Successfull")
except Exception as e:
    print("Logout failed: {}".format(e.message))
