# l=[]

# def string_s(string,sub_string):
#     count=0
#     for i in range(len(string)):
#         if string[i:i+len(sub_string)]==sub_string:
#             count += 1
#     return count
# a="ABCDCDC"
# b="CDC"
# r=string_s(a,b)
# print(r)
# s = input()
# print(any(char.isalnum() for char in s))
# print(any(char.isalpha() for char in s))
# print(any(char.isdigit() for char in s))
# print(any(char.islower() for char in s))
# print(any(char.isupper() for char in s))
thickness = int(input()) #This must be an odd number
c = 'H'
#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))
i=thickness
for i in range(thickness):
    print((((c*(thickness-i-1)).rjust(thickness))+c+((c*(thickness-i-1)).ljust(thickness))).rjust(thickness*6))
  
    #print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))
    