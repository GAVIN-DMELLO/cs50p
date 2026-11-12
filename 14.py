import sys
# ip = input("number? ")

# for i in range(1,11):
#   print(f" {ip} * {i} = {int(ip)*i}")

# l = ["Harry", "Soham", "Sachin", "Rahul"]

# for i in l:
#   if i[0] == 'S':
#     print(f"Hello , {i}")


# i=0 

# ip = input("num?")

# while(i<=10):
#   print(f"{ip} * {i} = {int(ip)*i}")
#   i=i+1


# ip = input("enter your number? ")

# for i in range(2,int(ip)):
#   if int(ip)%i == 0:
#     print("Not a prime")
#     sys.exit()

# print("Prime")


# ip = input("enter the value of n ")

# n = int(ip)

# i=0
# sum=0
# while(i<=n):
#   sum += i
#   i=i+1

# print(sum)


# ip = input("number? ")

# n = int(ip)

# fact=1
# for i in range(1,n+1):
#   fact *= i

# print(fact)


# print("*")
# print("***")
# print("*****")

# # 1->1
# # 2->3
# # 3->5

# for i in range(1,4):
#   for j in range(2*i-1):
#     print(f"*" , end="")
#   print()


# *
# **
# ***

# 1->1
# 2->2
# 3->3

# for i in range(1,4):
#   for j in range(i):
#     print("*" , end="")
#   print()


# 1->3
# 2->2
# 3->3

# for i in range(1,4):
#   if i%2 != 0:
#     for j in range(3):
#       print("*",end="")
#     print()
#   else:
#     for j in range(2):
#       print("*",end="")
#     print()


ip = input("number? ")

n = int(ip)

for i in range(10 , 0 , -1):
  print(f"{n} * {i} = {n*i}")