list = []
n = int(input("enter number of accountId:"))
for i in range (0,n):
    ele = int(input("enter accountID"))
    list.append(ele)
print(list)
print("choose search")
print("linear")
print("binary")
print("exit")

choice=int(input("enter the choice 1 or 2"))

match choice :
    case 1:
        Ac_ID=int(input("enter the element of search"))
        for i in range (0,n):
          if list[i]==Ac_ID:
             print(Ac_ID,"os found at index",i)
          else:
             print("Ac_ID not found")
    case 2:
     
     list.sort()
print(list)
Ac_ID=int(input("enter the element of search"))
left=0
right=len(list)-1   
flag=False 
while left<=right:
    mid=(left+right)//2
    if(list[mid]==Ac_ID):
        print(Ac_ID,"is found at",mid)
        flag=True
        break
    elif(list[mid]>Ac_ID):
        right=mid-1
    elif(list[mid]<Ac_ID):
        left=mid+1
if flag==False:
  print(Ac_ID,"not found")
    

