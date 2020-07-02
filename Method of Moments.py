import numpy as numpyp
from matplotlib import pyplot as plt


def binom_and_calc(N):
    #Binomial calculation
    Y = [] #holds the number of success from n trial for N sample
    p=0.3

    for i in range(N):
        X = []
        for i in range(40):
            u = numpyp.random.rand()
            x = u<p
            X.append(x)
        y=sum(X)
        Y.append(y)

    np = sum(Y)/N #Sample mean : (1/N) * ∑xi : x̄
    npq = (1/N) * (sum((i - np) ** 2 for i in Y)) #Sample variance (1/N) * ∑(xi - x̄)**2 : Sx
    q = npq/np # q = 1-p : Sx/x̄
    ps = 1-q # 1- (Sx/x̄) = 1-q : Ṕ # şapkalı p
    ns = np/ps # x̄/ps : ñ # şapkalı n
    return ps,ns


def samples(N):
    list_of_p= []
    list_of_n = []
    for i in range(1000):
        ps,ns = binom_and_calc(N)
        list_of_p.append(ps)
        list_of_n.append(ns)
    

    print(N," sample : mean for estimated p:",numpyp.mean(list_of_p))
    print(N," sample : std for estimated p:",numpyp.std(list_of_p))
    print(N," sample : mean for estimated n:",numpyp.mean(list_of_n))
    print(N," sample : std for estimated n:",numpyp.std(list_of_n))
    print("\n")

    return list_of_p,list_of_n



def main_func():
    list_of_p200,list_of_n200 = samples(200)
    list_of_p800,list_of_n800 = samples(800)
    list_of_p3200,list_of_n3200 = samples(3200)

    

    plt.figure()
    plt.title("Histogram for estimated p")
    
    kwargs = dict(histtype='stepfilled', alpha=0.3,density=True, bins=100)
    plt.hist((list_of_p200,list_of_p800,list_of_p3200),**kwargs,color=['blue','orange','green'],label=["200","800","3200"])
    plt.legend()
        

    plt.figure()
    plt.title("Histogram for estimated n")
    plt.hist((list_of_n200,list_of_n800,list_of_n3200),**kwargs,color=['blue','orange','green'],label=["200","800","3200"])
    plt.legend()

    plt.show()


main_func()



