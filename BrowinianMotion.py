import numpy as np
import matplotlib.pyplot as mp

# Variable
#Geometric BR_MO = St = S*exp((mu-sigma**2/2)*t + sigma * Wt)

n= 20
T = 1
sigma = 0.30
S = 40
nub_of_sims = 100
mu =0.1 # drift coefficient

#simulation the geometric brownian motion
# dt = t in the formula

dt = T/n

St = np.exp((mu - sigma ** 2 /2 ) *
            dt + sigma * np.random.normal(0, np.sqrt(dt), size= (nub_of_sims,n))).T

St = np.vstack([np.ones(nub_of_sims),St])

St=S*St.cumprod(axis=0)

time = np.linspace(0,T,n+1)

t1 = np.full(shape=(nub_of_sims,n+1), fill_value=time).T
#t1 doesn't work if we don't multiply by T, try to understand why ?

mp.plot(t1, St)
mp.xlabel("Years St ")
mp.ylabel("Stock price in $")
mp.suptitle("Brownian Motion")
mp.title('ds= mu St dt + sigma St dW''\nS0 ='+str(S))

mp.show()

