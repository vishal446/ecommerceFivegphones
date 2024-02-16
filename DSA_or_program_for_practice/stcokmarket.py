import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    l=0
    t=0
    p=0
    s=list(set(ar))
    print(s)
    for i in range(len(s)):
        l=ar.count(s[i])
        if l>1:
            p=l//2

            t+=p
            
    return t
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = 9
    ar=[10, 20, 10, 20, 10, 30, 50, 10, 20]

    #ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
