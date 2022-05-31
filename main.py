from utils import parse_inputs,create_graph
from KnapsackDAC import knapSack_DAC
from KnapsackDP import knapSack_DP
import time
from os import walk


files_paths = []
path = './data/'
filenames = next(walk(path), (None, None, []))[2]

for file in filenames:
    files_paths.append(path+file)

    
#list for time of test
DAC_time = []
DP_time = []

#list for size of test
DAC_size = []
DP_size = []


# for dac algorithm
for index,file in enumerate(files_paths):
    #load weights and cost 
    #capacity, la lista con los pesos, lista con los costos y el len de las lista
    capacity, weight_list, cost_list , n = parse_inputs(file)
    #create start time
    start_time = time.time()
    #get max value
    knapSack_max_val = knapSack_DAC(capacity, weight_list, cost_list, n)
    #calcular end time
    end_time = (time.time() - start_time)
    #print(index,capacity)
    #append to list
    DAC_time.append(end_time)
    DAC_size.append(n)

# for DP algorithm
for file in files_paths:
    #load weights and cost 
    #capacity, la lista con los pesos, lista con los costos y el len de las lista
    capacity, weight_list, cost_list , n = parse_inputs(file)
    #create start time
    start_time = time.time()
    #get max value
    knapSack_max_val = knapSack_DP(capacity, weight_list, cost_list, n)
    #calcular end time
    end_time = (time.time() - start_time)


    #append to list
    DP_time.append(end_time)
    DP_size.append(n)

#dac graph
create_graph(DAC_size,DAC_time,'knapSack DAC')
#dp graph
create_graph(DP_size,DP_time,'knapSack DP')