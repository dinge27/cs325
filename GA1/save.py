import numpy as np

def partition(days, clubs, m):
    n = len(clubs)

    if days == 1:
        
        sum = np.sum(clubs)       
        return max(m, sum)

    actual_min = m
    for i in range(n - days + 1): 
        sum = np.sum(clubs[0:i+1])
        p = partition(days-1, clubs[i:], max(m, sum))
        
        actual_min = min(p, actual_min)
    
    return actual_min

def min_num_attendees(days, clubs):
    n = len(clubs)
    array = []
    if (days >= n):
        return max(clubs)
    
    return partition(days, clubs, np.sum(clubs))

print(min_num_attendees(3, [30, 20, 10, 5, 5, 5]))
