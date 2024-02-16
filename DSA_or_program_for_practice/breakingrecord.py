import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    minimum_score=[]
    maximum_score=[]
    for i in range(len(scores)):
        if i==0:
            maximum_score.append(scores[i])
            minimum_score.append(scores[i])
        else:
            if scores[i]>=maximum_score[-1] and scores[i]>minimum_score[-1]:
                    maximum_score.append(scores[i])
                    minimum_score.append(minimum_score[-1])
                
            elif scores[i]<maximum_score[-1] and scores[i]<=minimum_score[-1]:
                maximum_score.append(maximum_score[-1])
                minimum_score.append(scores[i])
            else:
                maximum_score.append(maximum_score[-1])
                minimum_score.append(minimum_score[-1])
           

    b=0
    w=[]
    t=[]
    for i,j,k in zip(scores,maximum_score,minimum_score):
        print(i,'\t',j,'\t',k)
        if j==j==k:
            pass
        elif i==j:
            t.append(j)
        elif i==k:
            w.append(i)
    # print(t)
    # print(w)
    # b=list(set(t))
    # # w1=list(set(w))
    # print(b)
    # print(w1)
    return  len(list(set(t))),len(list(set(w)))


            
            
        

if __name__ == '__main__':

    n = 2

    scores = [23,90]

    result = breakingRecords(scores)
    print(result)

