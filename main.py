import string

import numpy as np
from scipy.stats import norm

# Define variables

r = float(input("entrer taux fixe > "))
s = float(input("entrer prix de l'option > "))
K = float(input("entrer prix d'exercise > "))
T = float(input("entrer durer en jours >"))/365
sigma = float(input('Volatilité >'))
type = input("Entrer 'C' pour un call option ou 'P' pour un put >\n").upper()


def BlackScholes(r, s, K, T, sigma, type):
    # Calculate BS option price for a call/put
    d1 = (np.log(s / K) + (r + sigma ** 2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    try:
        if type == "C":
            price = s * norm.cdf(d1, 0, 1) - K * np.exp(-r * T) * norm.cdf(d2, 0, 1)
        elif type == "P":
            price = K * np.exp(-r * T) * norm.cdf(-d2, 0, 1) - s * norm.cdf(-d1, 0, 1)
        return price
    except:
        print("Confirm the option parameters")


print("Prix de l'option :", round(BlackScholes(r,s,K,T,sigma,type),3))
