user_num = int(input("how many number would you want to enter;"))
listnum = []

for i in range(user_num):
    numbers = int(input("Enter a number: "))
    listnum.append(numbers)

print(listnum)
 
for data in listnum:
    if data > 0:
      print(data, "this number is positive")
    elif data < 0:
      print(data, "this number is negative")
