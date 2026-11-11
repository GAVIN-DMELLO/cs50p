import sys

marks = []

for i in range(3):
  ip = input(f"marks{i+1} ")
  marks.append(int(ip))

sum=0
for i in range(3):
  if(marks[i]<33):
    print("Failed ")
    sys.exit()
  sum += marks[i]

total_percent = (sum/300)*100

# print(total_percent)

if(total_percent>=40):
  print("Pass")
elif(total_percent<=40):
  print("Failed")




