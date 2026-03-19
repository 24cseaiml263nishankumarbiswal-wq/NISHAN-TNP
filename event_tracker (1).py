entered_std=set()
rejected_std=set()
 
n=int(input("enter attempts:"))

for i in range(n):
    name=input("enter student name:")
    if name in entered_std:
      print(name,"Entery Rejected.Already Entered")
      rejected_std.add(name)
    else:
      print(name,"ENTRY ALLOWED.Welcome")
      entered_std.add(name)
for name in entered_std:
    print(name)
 