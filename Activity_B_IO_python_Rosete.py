
mycontacts={}
emptylist=[]

while True:
    print("[1]-add name or numb","[2]-search name or numb")
    menu = input("Enter choice: ")

    if menu == "1":
        u_int = input("Enter name: ")
        cnumber = input("Enter Number: ")
        mycontacts[u_int] = [cnumber]
        print(mycontacts)
        continue

    elif menu == "2":
        print(mycontacts)
        search_nam = input("Enter name: ")
        if search_nam in mycontacts:
            print(mycontacts[search_nam])
        else:
            print("User not found")

    elif menu == "3":
        f = open("mycontacts.txt","w")
        for x in emptylist:
            print(f.write(str(x)))
            f.close

    else:
        print("invalid choice")
