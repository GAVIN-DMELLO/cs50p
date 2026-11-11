num = []

for i in range(4):
  ip = input(f"enter the number {i} ")
  num.append(int(ip))

max = num[0]
for i in range(len(num)):
  if(num[i]>max):
    max = num[i]


print(max)