import numpy as np
from matplotlib import pyplot as plt


numSamples = 100000
numBins = 100

# For the random variable Y, cdf of Fy(y) = y**2. pdf of Fy(y) is the derivative of cdf of fy
def Fy(y):
    if y < 0:
        return 0
    elif y <= 1:
        return 2*y
    else:
        return 0

Fy_array = []
ind = []
for i in range(-100,200):
    Fy_array.append(Fy(i/100))
    ind.append(i/100)
plt.figure()
plt.title('Pdf of Y')
plt.plot(ind,Fy_array)

################################################################################################

# For the random variable X, Pdf of fx(x) = 1.08 / (3*x+2), Cdf of fx is the integration of pdf of fx

"""
fx= 0 when x<0
    1.08 / (3x+2) when 0<= x <= 10
    0 when x > 10
    According to pdf to cdf solutions : 
    0 to x ∫ 1.08 / 3x+2 dx = from 0 to x 1.08/3 * ln(3x+2)	= 0.36 ln(3x+2) - 0.36 ln2 = 0.36 ln((3x+2)/2)
"""
def fx(x):
    if x < 0:
        fx = 0
    elif x <= 10:
        fx = 0.36 * np.log(abs((3*x+2) / 2))
    else:
        fx = 1
    return fx

fx_array = []
ind = []
for i in range(-200,1200):
    fx_array.append(fx(i/100))
    ind.append(i/100)
plt.figure()
plt.title('Cdf of X')
plt.plot(ind,fx_array)



#inverse transformation method
print('-------------------------- Inverse transformation method --------------------------')
def Fx_inverse(u):
    return (  (2* ( np.exp(1)**(2.77777 * u))) -2) /3 # inverse of  0.36 * np.log(abs((3*x+2) / 2))
U = []
X = []
for i in range(numSamples):
    U.append(np.random.rand())
    X.append(Fx_inverse(U[i]))
plt.figure()
plt.title('Histograms of the generated U and X samples (pdf)')
hU = plt.hist(U,numBins,alpha=0.5, density=True)
hX = plt.hist(X,numBins,alpha=0.5, density=True)
plt.figure()
plt.title('Normalized cumulative sum of histogram values for the generated U and X samples (cdf)')
plt.plot(np.cumsum(hU[0])/hU[0].sum())
plt.plot(np.cumsum(hX[0])/hX[0].sum())




#rejection method
print('----------------------------- Sample rejection method -----------------------------')
c = 0.6
a = -2
b = 12
Y = []
i = 0
while i < numSamples:
    u = np.random.rand()
    v = np.random.rand()
    y = (b-a)*u+a
    x = c*v
    if x <= Fy(y):
        Y.append(y)
        i = i + 1
        
plt.figure()
plt.title('Histogram of the generated Y samples (pdf)')
hY = plt.hist(Y, numBins, density=True)
plt.figure()
plt.title('Normalized cumulative sum of histogram values for the generated Y samples (cdf)')
plt.plot(hY[1][0:numBins], np.cumsum(hY[0])/hY[0].sum())
plt.show()