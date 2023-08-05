import os
import time
import ccxt
import platform
import yfinance as yf
import tushare as ts
import pandas as pd
from datetime import date,datetime, timedelta
#from market import signals as tawSignal
from alpaca.data.historical import CryptoHistoricalDataClient,StockHistoricalDataClient
from alpaca.data.requests import CryptoBarsRequest,StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass
from alpaca.trading.requests import GetOrdersRequest
from alpaca.trading.enums import OrderSide, QueryOrderStatus
from alpaca.trading.requests import MarketOrderRequest,LimitOrderRequest,StopOrderRequest,StopLimitOrderRequest,TrailingStopOrderRequest
from alpaca.data.requests import CryptoLatestQuoteRequest

from alpaca.broker.models import Contact,Identity,Disclosures,Agreement
from alpaca.broker.requests import CreateAccountRequest
from alpaca.broker.enums import TaxIdType, FundingSource, AgreementType
from alpaca.broker.requests import CreateJournalRequest
from alpaca.broker.enums import JournalEntryType
from alpaca.broker.client import BrokerClient
from alpaca.broker.requests import CreateACHTransferRequest
from alpaca.broker.enums import TransferDirection, TransferTiming
from alpaca.trading.enums import OrderSide, TimeInForce

from alpaca.broker.requests import CreateACHRelationshipRequest
from alpaca.broker.enums import BankAccountType
import byquant
#from market import models as marketModels

class Bar():
    def __init__(self, symbol,ktype = 'quote',freq = '1d',tawtime = 86400,renew = '0',cache = False):
        self.symbol = symbol
        self.market = self.getSymbolInfo()['market']
        self.limit = 1000
        self.offset = 0
        self.ktype = ktype
        self.freq = freq
        self.tawtime = tawtime
        self.renew = renew
        self.cache = cache
        self.haskey = 'no'
        self.exchange = self.symbol.split('.')[-1]
        self.underlying = self.symbol.replace('~', '/').replace('$', ':').replace('.' + self.exchange, '')
        self.MARKET_DATA_PATH = '~/temp/%s/' % (self.ktype)
        if not os.path.isdir('~/temp/'):
            os.makedirs('~/temp/')
            if not os.path.isdir(self.MARKET_DATA_PATH):
                os.makedirs(self.MARKET_DATA_PATH)
        self.tushareKey = 'Your  API  Token'
        self.filepath = self.MARKET_DATA_PATH + '%s/%s/%s.csv' % (self.exchange, self.freq, self.symbol.replace('.' + self.exchange, ''))

        self.underlying_ex = self.underlying
        if self.exchange == 'SSE':
            self.underlying_ex = self.underlying_ex.replace('SH', '') + '.SH'
        elif self.exchange == 'SZSE':
            self.underlying_ex = self.underlying_ex.replace('SZ', '') + '.SZ'
        elif self.exchange == 'BSE':
            self.underlying_ex = self.underlying_ex.replace('BJ', '') + '.BJ'
        elif self.exchange == 'HKEX':
            self.underlying_ex = self.underlying_ex.replace('HK', '') + '.HK'

        #print(self.tushareKey)
        #print(self.market)



    def quote(self):

        #print(self.haskey)
        self.haskey = self.checkKey()
        #print(self.filepath)
        #print(self.symbol)
        #print(self.haskey)
        #print(self.haskey)
        if not os.path.exists(self.filepath):
            result = self.createQuote()
        elif self.haskey == 'no':
            result = self.createQuote()
        elif self.renew == '0':
            result = self.readCSV()
        else:
            fileTime = int(os.path.getmtime(self.filepath))
            nowTime = time.time()
            expireTime = fileTime + self.tawtime
            if nowTime > expireTime:
                result = self.updateQuote()
            else:
                result = self.readCSV()

        return result

    def quoteTimeSort(self):

        result = self.quote()
        result.rename(columns={"quote_time": "datetime"}, inplace=True)
        result['datetime'] = pd.to_datetime(result['datetime'])
        # print(df)
        result = result.sort_values('datetime')  # 数据顺序排列
        # print(df)

        return result

    def signal(self):
        self.haskey = self.checkKey()
        if not os.path.exists(self.filepath):
            result = self.createSignal()
        elif self.haskey == 'no' :
            result = self.createSignal()
        else:
            result = self.readCSV()
        return result

    def createQuote(self):
        df = {}
        try:

            if self.exchange in ['SSE','SZSE','BSE','AMEX','ARCA','BATS','HKEX','NASDAQ','NYSE','OTC', 'NYSEARCA', 'FTXU', 'CBSE', 'GNSS', 'ERSX']:
                #print('yahoo_0')
                df = self.yahooApi()

                if len(df) < 10:
                    if self.exchange in ['SSE','SZSE','BSE']:
                        #print('tushare_cn')
                        if self.market == 'FUND':
                            df = self.tushareFundApi()
                        elif self.market == 'STOCK':
                            df = self.tushareStockApi()
                        else:
                            pass


                    elif self.exchange in ['AMEX', 'ARCA', 'BATS','NASDAQ', 'NYSE', 'OTC', 'NYSEARCA', 'FTXU','CBSE', 'GNSS', 'ERSX']:

                        #print('alpaca_1')

                        df = self.tushareCNStockApi()
                    elif self.exchange in ['HKEX']:
                        #print('tushare_hk')
                        df = self.tushareHKStockApi()  #没有权限


            elif self.exchange == 'ALPACA':
                df = self.alpacaCryptoApi()

            else:
                df = self.ccxtApi()

            if len(df) > 0 and self.cache:
                self.saveCSV(df)



        except Exception as e:
            print(e.args)
            pass

        ###########

        return df

    def yahooApi(self):
        df = {}
        try:
            if self.freq == 'D' or self.freq == '1d':
                periodlUS = '10y'
                intervalUS = '1d'
            elif self.freq == '1min' or self.freq == '1m':
                periodlUS = '7d'
                intervalUS = '1m'
            elif self.freq == '5min':
                periodlUS = '60d'
                intervalUS = '5m'
            elif self.freq == '15min':
                periodlUS = '60d'
                intervalUS = '15m'
            elif self.freq == '30min':
                periodlUS = '60d'
                intervalUS = '30m'
            elif self.freq == '60min' or self.freq == '1h':
                periodlUS = '1y'
                intervalUS = '1h'
            elif self.freq == 'W':
                periodlUS = '1y'
                intervalUS = '1wk'
            elif self.freq == 'M':
                periodlUS = '1y'
                intervalUS = '1mo'


            self.underlying_ex = self.underlying_ex.replace('.SH', '.SS')

            # print('===================')
            # print(self.exchange)
            # print(periodlUS)
            # print(intervalUS)

            # dfTemp = pdr.get_data_yahoo(
            dfTemp = yf.download(  # or pdr.get_data_yahoo(...
                tickers=self.underlying_ex,  # tickers list or string as well
                period=periodlUS,
                # use "period" instead of start/end # valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max# (optional, default is '1mo')
                interval=intervalUS,
                # valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo  # fetch data by interval (including intraday if period < 60 days) # (optional, default is '1d')
                ignore_tz=False,
                # Whether to ignore timezone when aligning ticker data from # different timezones. Default is False.
                group_by='ticker',  # group by ticker (to access via data['SPY']) # (optional, default is 'column')
                auto_adjust=True,  # adjust all OHLC automatically # (optional, default is False)
                repair=False,  # attempt repair of missing data or currency mixups e.g. $/cents
                prepost=True,  # download pre/post regular market hours data # (optional, default is False)
                threads=True,
                # use threads for mass downloading? (True/False/Integer) # (optional, default is True)
                proxy=None  # proxy URL scheme use use when downloading?# (optional, default is None)
            )

            dfTemp.reset_index(drop=False, inplace=True)
            if self.freq == 'D' or self.freq == '1d' or self.freq == 'W' or self.freq == 'M':
                dfTemp['Datetime'] = dfTemp['Date']
                dfTemp['Datetime'] = dfTemp['Datetime'].dt.tz_convert('UTC')
                dfTemp['Datetime'] = dfTemp['Datetime'].dt.tz_localize(None)
            # dfTemp['symbol'] = self.symbol

            df = pd.DataFrame()
            df['quote_time'] = dfTemp['Datetime']
            df['open'] = dfTemp['Open']
            df['high'] = dfTemp['High']
            df['low'] = dfTemp['Low']
            df['close'] = dfTemp['Close']
            df['volume'] = dfTemp['Volume']




        except Exception as e:
            print(e.args)
            pass

        ###########

        return df

    def tushareCNStockApi(self):
        df = {}
        try:
            pro = ts.pro_api(self.tushareKey)
            # underlying = self.symbol.replace('~', '/').replace('$', ':').replace('.' + self.exchange, '')
            if self.exchange == 'SSE':
                self.underlying_ex = self.underlying_ex.replace('.SS', '.SH')
            # 拉取数据

            startDay = date.today() + timedelta(days=-1000)
            if self.freq == '1m':
                startDay = date.today() + timedelta(days=-15)
            startDay = format(startDay.strftime('%Y%m%d'))
            # print(LastWeek)
            toDay = date.today()
            toDay = format(toDay.strftime('%Y%m%d'))
            # print(startDay)
            # print(toDay)
            # print(self.underlying)
            dfTemp = pro.daily(**{
                "ts_code": self.underlying_ex, "trade_date": "", "start_date": startDay, "end_date": toDay, "offset": "",
                "limit": ""
            }, fields=[
                "ts_code", "trade_date", "open", "high", "low", "close", "pre_close", "change", "pct_chg", "vol",
                "amount"
            ])
            # print(dfTemp)

            df = pd.DataFrame()
            df['quote_time'] = dfTemp['trade_date']
            df['open'] = dfTemp['open']
            df['high'] = dfTemp['high']
            df['low'] = dfTemp['low']
            df['close'] = dfTemp['close']
            df['volume'] = dfTemp['vol']




        except Exception as e:
            print(e.args)
            pass

        ###########

        return df

    def tushareHKStockApi(self):
        df = {}
        try:
            pro = ts.pro_api(self.tushareKey)
            startDay = date.today() + timedelta(days=-1000)
            if self.freq == '1m':
                startDay = date.today() + timedelta(days=-15)
            startDay = format(startDay.strftime('%Y%m%d'))
            # print(LastWeek)
            toDay = date.today()
            toDay = format(toDay.strftime('%Y%m%d'))
            #print(startDay)
            #print(toDay)
            #print(self.underlying)
            dfTemp = pro.hk_daily(**{
                "ts_code": self.underlying, "trade_date": "", "start_date": startDay, "end_date": toDay, "offset": "",
                "limit": ""
            }, fields=[
                "ts_code", "trade_date", "open", "high", "low", "close", "pre_close", "change", "pct_chg", "vol",
                "amount"
            ])
            #print(dfTemp)

            df = pd.DataFrame()
            df['quote_time'] = dfTemp['trade_date']
            df['open'] = dfTemp['open']
            df['high'] = dfTemp['high']
            df['low'] = dfTemp['low']
            df['close'] = dfTemp['close']
            df['volume'] = dfTemp['vol']




        except Exception as e:
            print(e.args)
            pass

        ###########

        return df

    def tushareFundApi(self):
        df = {}
        try:
            pro = ts.pro_api(self.tushareKey)
            # underlying = self.symbol.replace('~', '/').replace('$', ':').replace('.' + self.exchange, '')
            if self.exchange == 'SSE':
                self.underlying = self.underlying.replace('.SS', '.SH')
            # 拉取数据

            startDay = date.today() + timedelta(days=-1000)
            if self.freq == '1m':
                startDay = date.today() + timedelta(days=-15)
            startDay = format(startDay.strftime('%Y%m%d'))
            # print(LastWeek)
            toDay = date.today()
            toDay = format(toDay.strftime('%Y%m%d'))
            #print(startDay)
            #print(toDay)
            #print(self.underlying)
            dfTemp = pro.fund_daily(**{
                "ts_code": self.underlying, "trade_date": "", "start_date": startDay, "end_date": toDay, "offset": "",
                "limit": ""
            }, fields=[
                "ts_code", "trade_date", "open", "high", "low", "close", "pre_close", "change", "pct_chg", "vol",
                "amount"
            ])
            #print(dfTemp)

            df = pd.DataFrame()
            df['quote_time'] = dfTemp['trade_date']
            df['open'] = dfTemp['open']
            df['high'] = dfTemp['high']
            df['low'] = dfTemp['low']
            df['close'] = dfTemp['close']
            df['volume'] = dfTemp['vol']




        except Exception as e:
            print(e.args)
            pass

        ###########

        return df

    def ccxtApi(self):
        df = {}
        try:
            # getExchange = tawCCXT(self.exchange)
            getExchange = byquant.getExchange(self.exchange)
            getExchange.load_markets()

            strFreq = self.freq
            if strFreq == '1min':
                strFreq = '1m'
            elif strFreq == 'H':
                strFreq = '1h'
            elif strFreq == 'D':
                strFreq = '1d'
            elif strFreq == 'M':
                strFreq = '1M'
            elif strFreq == 'Y':
                strFreq = '1y'
            limit = 1000

            if getExchange.has['fetchOHLCV']:
                # time.sleep(getExchange.rateLimit / 1000)  # time.sleep wants seconds
                quotes = []
                df = {}
                # underlying = self.symbol.replace('~', '/').replace('$', ':').replace('.' + self.exchange, '')
                ohlcvData = getExchange.fetchOHLCV(self.underlying, timeframe=strFreq, limit=limit, params={})

                for ohlcv in ohlcvData:
                    quote = {}
                    quoteTime = time.localtime(ohlcv[0] / 1000)
                    quote_time = time.strftime("%Y-%m-%d %H:%M:%S", quoteTime)
                    quote['quote_time'] = quote_time
                    quote['open'] = ohlcv[1]
                    quote['high'] = ohlcv[2]
                    quote['low'] = ohlcv[3]
                    quote['close'] = ohlcv[4]
                    quote['volume'] = ohlcv[5]
                    quotes.append(quote)

                # df['open'] = df['ohlcv'][0]
                df = pd.DataFrame(quotes)





        except Exception as e:
            print(e.args)
            pass

        ###########

        return df

    def alpacaCryptoApi(self):
        df = {}
        try:
            # underlying = self.symbol.replace('~', '/').replace('$', ':').replace('.' + self.exchange.upper(), '')
            # print([freq])
            # toDay = date.today()
            # toDay = format(toDay.strftime('%Y-%m-%d'))
            client = CryptoHistoricalDataClient("Key", "KeyI")
            # strFreq = freq
            if self.freq == '1m':
                # strFreq = '1m'
                startTime = (date.today() + timedelta(days=-7)).strftime("%Y-%m-%d %H:%M:%S")
                request_params = CryptoBarsRequest(
                    symbol_or_symbols=[self.underlying],
                    timeframe=TimeFrame.Minute,
                    start=datetime.strptime(startTime, '%Y-%m-%d %H:%M:%S')
                )
            elif self.freq == '1h':
                startTime = (date.today() + timedelta(days=-90)).strftime("%Y-%m-%d %H:%M:%S")
                request_params = CryptoBarsRequest(
                    symbol_or_symbols=[self.underlying],
                    timeframe=TimeFrame.Hour,
                    start=datetime.strptime(startTime, '%Y-%m-%d %H:%M:%S')
                )
            elif self.freq == '1d':
                # strFreq = '1d'
                startTime = (date.today() + timedelta(days=-1000)).strftime("%Y-%m-%d")
                request_params = CryptoBarsRequest(
                    symbol_or_symbols=[self.underlying],
                    timeframe=TimeFrame.Day,
                    start=datetime.strptime(startTime, '%Y-%m-%d')
                )
            else:
                startTime = (date.today() + timedelta(days=-1000)).strftime("%Y-%m-%d")
                request_params = CryptoBarsRequest(
                    symbol_or_symbols=[self.underlying],
                    timeframe=TimeFrame.Day,
                    start=datetime.strptime(startTime, '%Y-%m-%d')
                )

            barsInfo = client.get_crypto_bars(request_params)
            barsData = barsInfo.data
            # print(type(barData))
            barsList = barsData[self.underlying]

            # print(barsList)
            barList = []
            for bars in barsList:
                barDict = dict(bars)
                barTemp = {}
                barTemp['quote_time'] = str(barDict['timestamp'])
                barTemp['open'] = float(barDict['open'])
                barTemp['high'] = str(barDict['high'])
                barTemp['low'] = float(barDict['low'])
                barTemp['close'] = float(barDict['close'])
                barTemp['volume'] = float(barDict['volume'])
                # barTemp['trade_count'] = float(barDict['trade_count'])
                barTemp['vwap'] = str(barDict['vwap'])


                # print(tickTemp)
                barList.append(barTemp)

            dfTemp = pd.DataFrame(barList)
            # dfTemp['symbol'] = symbol
            df = dfTemp.tail(1000)
            # print(df)





        except Exception as e:
            print(e.args)
            pass

        ###########

        return df

    def alpacaStockApi(self):
        df = {}
        try:
            # underlying = self.symbol.replace('~', '/').replace('$', ':').replace('.' + self.exchange.upper(), '')
            # print([freq])
            # toDay = date.today()
            # toDay = format(toDay.strftime('%Y-%m-%d'))
            client = StockHistoricalDataClient("KEY", "KEYI")
            # strFreq = freq
            if self.freq == '1m':
                # strFreq = '1m'
                startTime = (date.today() + timedelta(days=-7)).strftime("%Y-%m-%d %H:%M:%S")
                request_params = StockBarsRequest(
                    symbol_or_symbols=[self.underlying],
                    timeframe=TimeFrame.Minute,
                    start=datetime.strptime(startTime, '%Y-%m-%d %H:%M:%S')
                )
            elif self.freq == '1h':
                startTime = (date.today() + timedelta(days=-90)).strftime("%Y-%m-%d %H:%M:%S")
                request_params = StockBarsRequest(
                    symbol_or_symbols=[self.underlying],
                    timeframe=TimeFrame.Hour,
                    start=datetime.strptime(startTime, '%Y-%m-%d %H:%M:%S')
                )
            elif self.freq == '1d':
                # strFreq = '1d'
                startTime = (date.today() + timedelta(days=-1000)).strftime("%Y-%m-%d")
                request_params = StockBarsRequest(
                    symbol_or_symbols=[self.underlying],
                    timeframe=TimeFrame.Day,
                    start=datetime.strptime(startTime, '%Y-%m-%d')
                )
            else:
                startTime = (date.today() + timedelta(days=-1000)).strftime("%Y-%m-%d")
                request_params = StockBarsRequest(
                    symbol_or_symbols=[self.underlying],
                    timeframe=TimeFrame.Day,
                    start=datetime.strptime(startTime, '%Y-%m-%d')
                )

            barsInfo = client.get_stock_bars(request_params)
            barsData = barsInfo.data
            # print(type(barData))
            barsList = barsData[self.underlying]

            # print(barsList)
            barList = []
            for bars in barsList:
                barDict = dict(bars)
                barTemp = {}
                barTemp['quote_time'] = str(barDict['timestamp'])
                barTemp['open'] = float(barDict['open'])
                barTemp['high'] = str(barDict['high'])
                barTemp['low'] = float(barDict['low'])
                barTemp['close'] = float(barDict['close'])
                barTemp['volume'] = float(barDict['volume'])
                # barTemp['trade_count'] = float(barDict['trade_count'])
                barTemp['vwap'] = str(barDict['vwap'])


                # print(tickTemp)
                barList.append(barTemp)

            dfTemp = pd.DataFrame(barList)
            # dfTemp['symbol'] = symbol
            df = dfTemp.tail(1000)
            # print(df)





        except Exception as e:
            print(e.args)
            pass

        ###########

        return df

    def saveHDF(self, data): #将放弃
        result = False
        df = data
        try:

            if len(df) > 0:
                result = df
                df.fillna("0", inplace=True)
                df.sort_values(by="quote_time", ascending=False, inplace=True)

                filedir = self.MARKET_DATA_PATH + '%s' % (self.exchange)
                if not os.path.isdir(filedir):
                    os.makedirs(filedir)
                filepath = self.MARKET_DATA_PATH + '%s/%s.hdf' % (self.exchange, self.symbol)
                df.to_hdf(filepath, mode='a', key='quote_%s' % (self.freq), complevel=9, complib='blosc',
                          format='table')
                result = True



        except Exception as e:
            print(e.args)
            pass

        ###########

        return result

    def saveCSV(self,data):
        result = False
        df = data
        try:


            if len(df) > 0:
                result = df
                df.fillna("0", inplace=True)
                df.sort_values(by="quote_time", ascending=True, inplace=True)

                filedir = self.MARKET_DATA_PATH + '%s' % (self.exchange)
                if not os.path.isdir(filedir):
                    os.makedirs(filedir)

                mfiledir = self.MARKET_DATA_PATH + '%s/%s' % (self.exchange, self.freq)
                if not os.path.isdir(mfiledir):
                    os.makedirs(mfiledir)

                df.to_csv(self.filepath, index=False)
                """filepath = self.MARKET_DATA_PATH + '%s/%s.hdf' % (self.exchange, self.symbol)
                df.to_hdf(filepath, mode='a', key='quote_%s' % (self.freq), complevel=9, complib='blosc',
                          format='table')"""
                result = True



        except Exception as e:
            print(e.args)
            pass

        ###########

        return result

    def createSignal(self):
        result = tawSignal.autoStrategy(self.symbol, self.market, self.freq, self.limit, self.offset, self.tawtime)
        return result

    def updateQuote(self):
        result = self.createQuote() ##暂定
        return result

    """def read(self):
        readHdf = pd.read_hdf(self.filepath, key='%s_%s' % (self.ktype, self.freq),mode='a')
        result = pd.DataFrame(readHdf)
        return result"""

    def readHDF(self): #将放弃
        readResult = pd.read_hdf(self.filepath, key='%s_%s' % (self.ktype, self.freq))
        self.result = pd.DataFrame(readResult)
        return self.result

    def readCSV(self):
        readResult = pd.read_csv(self.filepath)
        self.result = pd.DataFrame(readResult)
        return self.result

    def checkKey(self):
        result = 'no'
        if os.path.exists(self.filepath):
            keyName = '%s_%s' % (self.ktype, self.freq)
            getStore = pd.HDFStore(self.filepath, 'a')
            keyArr = getStore.keys()
            getStore.close()
            if keyName in keyArr:
                result = 'yes'
        return result

    def getSymbolInfo(self):
        result = {}
        result['market']='CRYPTO'
        #try:
        #    result = marketModels.Underlying.objects.filter(symbol = self.symbol).values('market')
        #except Exception as e:
        #    print(e.args)
        #    pass
        return result




