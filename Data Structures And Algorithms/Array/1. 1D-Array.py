print("Enter the number of elements in the array")
num=input()
arr=[]
print("\nEnter",num,"Element:",end="")
num=int(num)

for i in range(num):
    element=input()
    arr.append(element)

print("\nThe Elements in the array are: ")
for i in range(num):
    print(arr[i]," ",end="")