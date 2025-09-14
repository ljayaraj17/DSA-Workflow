# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


num = int(input("enter a number"))
n=num
c=0
while (n>0):
    dig = n%10
    c=c+1
    n=n//10
print("Count : ",c)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
