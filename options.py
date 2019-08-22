import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('seaborn-darkgrid')

def call_payoff(sT, strike_price, premium):
    return np.where(sT > strike_price, sT - strike_price, 0) - premium

def put_payoff(sT, strike_price, premium):
    return np.where(sT < strike_price, strike_price - sT, 0) - premium 

def log_returns_plot_volatility(data, days):
    label = days + 'day Historical Volatility'
    data['Log Returns'] = np.log(data['Adj Close']/data['Adj Close'].shift(1))
    data[label] = 100*data['Log Returns'].rolling(window=int(days)).std()
    plt.plot(data[label], color = 'b', label =label)
    plt.legend(loc='best')
    plt.show()

def plot_chart(payoff, stockname, strategy_type, option_type, strike_price):
    # Plot
    fig, ax = plt.subplots(figsize=(8,5))
    ax.spines['bottom'].set_position('zero')
    ax.plot(sT,payoff,label=strategy_type + ' ' + str(strike_price) + ' Strike ' + option_type,color='g')
    plt.xlabel(stockname + 'Stock Price')
    plt.ylabel('Profit and loss')
    plt.legend()
    plt.show()

def import_data():
    data = pd.read_csv('apple_stock_data.csv')
    data.head()
    return data
    
if __name__ == "__main__":
    
    data = import_data()
    stockname = 'Infosys'
    # Infosys stock price 
    spot_price = 900 

    # Long call
    strike_price_long_call = 920 
    premium_long_call = 15

    # Short call
    strike_price_short_call = 940 
    premium_short_call = 10

    # Long put
    strike_price_long_put = 880 
    premium_long_put = 15

    # Short put
    strike_price_short_put = 860 
    premium_short_put = 10

    # Stock price range at expiration of the call
    sT = np.arange(0.95*spot_price,1.1*spot_price,1) 
    
    log_returns_plot_volatility(data, '20') ## 20 days of volatility window

    payoff_long_put = put_payoff(sT, strike_price_long_put, premium_long_put)
    payoff_long_call = call_payoff(sT, strike_price_long_call, premium_long_call)
    
    plot_chart(payoff_long_call, stockname, 'Long', 'Call', strike_price_long_call)
    plot_chart(payoff_long_put, stockname, 'Long', 'Put', strike_price_long_put)


