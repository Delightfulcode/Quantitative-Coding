import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
from pandas_datareader import data as pdr

# importing data
def grabData(stocks, start, end):

        stocksdata = pdr.get_data_yahoo(stocks, start, end)
        stocksdata = stocksdata['Close']
        returns = stocksdata.pct_change()
        returns_mean = returns.mean()
        covMatrix = returns.cov()

        return returns_mean, covMatrix

stocklist = ['CBA', 'BHP', 'STO', 'NAB']
stocks = [stock + '.AX' for stock in stocklist]
enddate= dt.datetime.now()  #specific orthographe
startdate = enddate - dt.timedelta(days=300)

returns_mean, covMatrix = grabData(stocks,startdate,enddate)

print(returns_mean)
weights= np.random.random(len(returns_mean))
weights /= np.sum(weights)
#print("\n",covMatrix)

#Monte carlo sim

mc_sims=100
T = 100 #time in days

MeanMatrix = np.full(shape=(T, len(weights)),fill_value=returns_mean)
MeanMatrix = MeanMatrix.T

portfolio_sims = np.full(shape=(T,mc_sims), fill_value=0.0)
initial_portfo = 10000

for m in range (0, mc_sims):
        #MC loops
        Ze = np.random.normal(size=(T, len(weights)))
        Le = np.linalg.cholesky(covMatrix)
        daily_returns = MeanMatrix +np.inner(Le, Ze)
        portfolio_sims[:,m] = np.cumprod(np.inner(weights, daily_returns.T)+1)*initial_portfo


### HERE IS THE VALUE AT RISK AND CONDITIONAL VALUE AT RISK

def mcVar(returns, alpha=5):
        "pandas series of return to output a percentileon return distribution to a given level alpha "

        if isinstance(returns,pd.Series):
                return np.percentile(returns,alpha)
        else:
                raise TypeError

def mcCvar (returns, alpha=5):
        if isinstance(returns,pd.Series):
                belowVar = returns <= mcVar(returns,alpha=alpha)
                return returns[belowVar].mean()
        else:
                raise TypeError

portfolio_results = pd.Series(portfolio_sims [-1,:])

Var = initial_portfo - mcVar(portfolio_results)
Cvar = initial_portfo - mcCvar(portfolio_results)

print('var =',round(Var,2))
print('CVar= ',round(Cvar,2))


plt.plot(portfolio_sims)
plt.xlabel("Days")
plt.ylabel("Portfolio Values $")
plt.title("Monte Carlo Sim of Portfolio")
plt.show()

