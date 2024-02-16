# n=int(input())
# p=map(int,input().split())
# t=tuple(p)
# t1=(float (x) for x in t)
# print(n,type(t1),hash(t1))ṇ
e='vx857 276@g mail.com'
user,web=e.split('@')
website,extn=web.split('.')
print(user)
print(website)
print(extn)
u=user.replace(' ','_')
print(u)
if u.isalnum:
    print(True)
if website.isalpha:
    print(True)
if len(extn)>3:
    print(True)
