# import textwrap
# global s

# def wrap(string, max_width):
#     s=''
#     for i in range(0,len(string),max_width):
#         s += string[i:i + max_width] + '\n'
#         s=s.rstrip()
#     return s

# if __name__ == '__main__':
#     string, max_width = input(), int(input())
#     result = wrap(string, max_width)
#     print(result)

# n,n1=7,21
# c='.'+'|'+'.'
# print(len(c))
# for i in range(n//2):
#     print((c*i).rjust((n1//2)-1,'-')+c+(c*i).ljust((n1//2)-1,'-'))
# t=n//2
# print("WELCOME".rjust(n1,'-')+'WELCOME'.ljust(n1,'-'))
# for i in range(t):
#     print((c*(t-i-1)).rjust(n1-1,'-')+c+((c*(t-i-1)).ljust(n1-1,'-')))

# n,n1=map(int,input().split())
# c='.|.'
# for i in range(n//2):
#     print((c*i).rjust((n1//2)-1,'-')+c+((c*i).ljust(((n1//2)-1),'-')))
        
# print("WELCOME".center(n1//2,'-'))    


# for i in range(n//2):
#     print((c*((n//2)-i-1)).rjust(((n1//2)+1),'-')+c+(c*((n//2)-i-1)).ljust(((n1//2)+1),'-'))
    

# def print_formatted(number):
#     # your code goes here`BD
#     for i in range(1,number+1):
#         c=' '
#         h=' '
#         j=i
#         while i!= 0:
#             c=c+str(i%8)
#             i=i//8
#         i=j
#         while i!=0:
#             if i>0 and i<=15:
#                 if i>0 and i<10:
#                     h=h+str(i)
#                     break
#                 else:
#                     if i==10:
#                         h='A'+h
#                         break
#                     elif i==11:
#                         h='B'+h
#                         break
#                     elif i==12:
#                         h='C'+h
#                         break
#                     elif i==13:
#                         h='D'+h
#                         break
#                     elif i==14:
#                         h='E'+h
#                         break
#                     elif i==15:
#                         h=='F'+h
#                         break
#             else:
#                 h=h+str(i%16)
#                 i=i//16
#         i=j
#         b=''
#         while i!=0:
#             b=str(i%2)+b
#             i=i//2
#         i=j
#         print(i,c,h,b)
                
                            

# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)

n=int(input())
import string
d=string.ascii_lowercase
l=[]

for i in range(n):
    s='-'.join(d[i:n])
    l.append((s[::-1]+s[1:]).center(4*n-3,'-'))
print('\n'.join(l[:0:-1]+l))





