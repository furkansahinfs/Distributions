import numpy as np
import random
import seaborn as sns
from scipy.stats import norm
import matplotlib.pyplot as plt
from scipy.stats import semicircular  


# experiment function for Experiment 1,2,3,4,5,6,7

def experiment(experiment_name,number_of_values,given_random_values):
    values =  given_random_values  #list of random values according to given parameter 

    selected_values_list = [] #holds selected values
    samples = [] #holds every single sample


    if(experiment_name != 4):

        for sample in range(0, 100000): 
            selected_values = random.choices(values, k=number_of_values) # select random values according to given number of values
            samples.append(sum(selected_values)) # sample = the sum of selected random values, append the sample to samples list
            selected_values_list.extend(selected_values)  # append the selected values to selected values list
    

    else:

        for sample in range(0, 10000):

            count = 0  # count for k=100 number of values
            current_total=0

            while count<100:
                random_number = sum(random.choices(values,k=1)) # take a random value

                #According to situation use the random value or pass for the next random value

                if(current_total < 40 and 0.5 < random_number < 1.5 ):
                    current_total += random_number
                    count +=1
                    selected_values_list.append(random_number) # append the selected value to selected values list
                    
                elif(current_total > 40 and -0.5 < random_number < 0.5):
                    current_total += random_number
                    count +=1
                    selected_values_list.append(random_number)  # append the selected value to selected values list
                else:
                    continue #pass for the next random value

            samples.append(current_total) # sample = the sum of selected random values = cırrent total, append the sample to samples list


   

    mean_value = np.mean(samples)
    std_value = np.std(samples)
    print( "Experiment : ",experiment_name)
    print("!! When you close the graphs of experiment ",experiment_name, " code runs the next experiment.")

    print("For # of value ",number_of_values ," mean : " ,mean_value)
    print("For # of value ",number_of_values ," std : " ,std_value)

    plt.figure()
    plt.title("Histogram for generated random values", fontsize=10)
    plt.hist(selected_values_list,100,density=True)

    plt.figure()

    title = ("Experiment : " ,experiment_name,": Histogram for sums of generated random values for # values :" , number_of_values) 
    plt.title(title, fontsize=8)

    plt.hist(samples,100,density=True)

    curve = np.linspace(mean_value-5*std_value, mean_value + 5*std_value,100000)

    plt.plot(curve,norm.pdf(curve,mean_value,std_value))
    plt.show()

    print("\n")


# for standart uniform distribution : np.random.uniform(0,1, size=100000)
# for semicircle distributionsemicircular.rvs(a,b,size = 100000)
# for experiment 4 np.concatenate([np.random.uniform(0.5, 1.5, 10000),np.random.uniform(-0.5, 0.5, 10000)])

experiment(1,2,np.random.uniform(0,1, size=100000))
experiment(2,10,np.random.uniform(0,1, size=100000))
experiment(3,50,np.random.uniform(0,1, size=100000))
experiment(4,100,np.concatenate([np.random.uniform(0.5, 1.5, 10000),np.random.uniform(-0.5, 0.5, 10000)]))
experiment(5,2,semicircular.rvs(2,1,size = 100000))
experiment(6,10,semicircular.rvs(2,1,size = 100000))
experiment(7,50,semicircular.rvs(2,1,size = 100000))













