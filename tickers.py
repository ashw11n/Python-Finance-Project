# getting a python list of all the tickers of the SNP500
import bs4 as bs
import datetime as dt
import os
import pandas as pd
import pandas_datareader.data as web
import pickle
import requests
import fix_yahoo_finance as yf


def save_sp500_tickers():
    # basic webscraping at this point?
    resp = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    soup = bs.BeautifulSoup(resp.text, "lxml")
    # table data
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        ticker = row.findAll('td')[0].text
        tickers.append(ticker)

    with open("sp500tickers.pickle", "wb") as f:
        pickle.dump(tickers, f)

    # take this print out tho
    print(tickers)

    return tickers


save_sp500_tickers()

# getting data from yahoo
# pulling stock pricing data on all of the SNP500 part 6
def get_data_from_yahoo(reload_sp500=False):

    if reload_sp500:

        tickers = save_sp500_tickers()
    else:
        with open("sp500tickers.pickle", "rb") as f:

            tickers = pickle.load(f)
    if not os.path.exists('stock_dfs'):

        # if that directory doesnt exist, then make it
        os.makedirs('stock_dfs')

    start = dt.datetime(2000,1,1)
    end = dt.datetime(2016, 12, 31)

    for ticker in tickers[:10]:
        # just to know if working
        print(ticker)

        if not os.path.exists('stock_dfs/{}.csv'.format(ticker)):

            df = web.DataReader(ticker, 'yahoo', start, end)
            df.to_csv('stock_dfs/{}.csv'.format(ticker)) # path to csv

        else:
            print('Aready have {}'.format(ticker))



get_data_from_yahoo()

fix_yahoo_finance