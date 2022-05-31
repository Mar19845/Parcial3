'''
Codigo obtenido de: https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
'''

# A naive recursive implementation
# of 0-1 Knapsack Problem
 
# Returns the maximum value that
# can be put in a knapsack of
# capacity capacity
import sys
sys.setrecursionlimit(200)

def knapSack_DAC(capacity, weight_list, cost_list, n):
    # Base Case
    if n == 0 or capacity == 0:
        return 0
    # If weight of the nth item is
    # more than Knapsack of capacity capacity,
    # then this item cannot be included
    # in the optimal solution
    if (weight_list[n-1] > capacity):
        return knapSack_DAC(capacity, weight_list, cost_list, n-1)
    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(cost_list[n-1] + knapSack_DAC(capacity-weight_list[n-1], weight_list, cost_list, n-1),knapSack_DAC(capacity, weight_list, cost_list, n-1))
# end of function knapSack
#print("the maximum value that can be put knapsack of capacity %s is: %s" %(capacity,  knapSack_max_val))
