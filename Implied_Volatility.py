from py_vollib.black_scholes import black_scholes as bs
from py_vollib.black_scholes.greeks.analytical import vega

def impliedVol (S, K, T ,r, market_p, flag='c', tolerance=0.00001):
    #calculate the implied vol of an european option
    """
    :param S:Stock price
    :param K: Strike price
    :param T: Time to maturity
    r: risk free rate
    :param market_p:
    :param flag: option type
    :param tolerance:
    """

    max_iteration    = 200
    vol_old=0.3 #initial guess

    for k in range (max_iteration):
        bs_price = bs(flag,S, K, T ,r, vol_old)
        Cprime=vega(flag,S, K, T ,r, vol_old)*100
        C = bs_price - market_p

        vol_new=vol_old - C/Cprime
        new_bs_price = bs(flag,S, K, T ,r, vol_new)
        if (abs(vol_old-vol_new)< tolerance or abs(new_bs_price-market_p)< tolerance):
            break



        vol_old=vol_new

    implied_vol=vol_new
    return implied_vol


S,K,T,r = 30 ,28 ,0.5 ,0.025
market_pr = 2.5
print(impliedVol(S,K,T,r,market_pr)*100)

#doesn't work for a market price <= 2 because it doesn't exist in the bs formula for the variables chosen here
