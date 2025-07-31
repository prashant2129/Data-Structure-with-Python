list = []
n = int(input("enter number of accountId:"))
for i in range (0,n):
    ele = int(input("enter accountID"))
    list.append(ele)
print(list)

Ac_id=int(input("Enter Ac_id to searched"))
flag=False
for i in range (0,n):
    if(list[i]==Ac_id):
        print(Ac_id,"found at index",i)
        flag = True
        break
if flag==False:
        print(Ac_id,"not Found")
