import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def parse_inputs(data_file):
    df = pd.read_csv(data_file, names=['cost','weight'])
    


    #df['cost'] = df['cost'].apply(pd.to_numeric,downcast='float',errors=True)
    #df['weight'] = df['weight'].apply(pd.to_numeric,downcast='float',errors=True)


    capacity = int(0.10 * sum(df['weight']))
    #print("\nSetting weight capacity to 80% of total: {}".format(str(capacity)))


    #regresar la capacity, la lista con los pesos, lista con los costos y el len de las lista
    return capacity, df['weight'].to_list(), df['cost'].to_list(), len( df['cost'])


def create_graph(size_list,time_list,name):
    fig = plt.figure()
    plt.plot(time_list)
    plt.xticks(range(len(size_list)), size_list)
    fig.suptitle(name, fontsize=20)
    plt.xlabel('Size of test', fontsize=18)
    plt.ylabel('Time (s)', fontsize=16)

    #plt.xlim(0, size_list[-1])
    #plt.ylim(0)

    plt.show()