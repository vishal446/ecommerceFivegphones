def kangaroo(x1, v1, x2, v2):
    # Write your code here
    t1=x1
    t2=x2
    while x1!=x2<=1000:
        x1+=v1
        x2+=v2
        t=False
        if x1==x2:
            t=True
    if t==True and x1%t1==x2%t2:
        print("YES")
    else:
        print("NO")
if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)