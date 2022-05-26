'''
Codigo obtenido de: https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
'''


# A Dynamic Programming based Python
# Program for 0-1 Knapsack problem
# Returns the maximum value that can
# be put in a knapsack of capacity capacity

def knapSack_DP(capacity, weight_list, cost_list, n):
    K = [[0 for x in range(capacity + 1)] for x in range(n + 1)]
    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for capacity in range(capacity + 1):
            if i == 0 or capacity == 0:
                K[i][capacity] = 0
            elif weight_list[i-1] <= capacity:
                K[i][capacity] = max(cost_list[i-1] + K[i-1][capacity-weight_list[i-1]], K[i-1][capacity])
            else:
                K[i][capacity] = K[i-1][capacity]

    return K[n][capacity]

#print("the maximum value that can be put knapsack of capacity %s is: %s" %(capacity,  knapSack_max_val))
