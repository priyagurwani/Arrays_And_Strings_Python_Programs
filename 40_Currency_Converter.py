amount=int(input("Enter the Indian rupees: "))
while True:
    print("-----------------Currency Converter--------------------")
    print("1.US Dollar"+"\n"+"2.Thai Bhatt"+"\n"+"3.New Zealand Dollar"+"\n"+"4.Canadian Dollar"+"\n"+"5.Swedish Krona"+"\n"+"6.Exit")
    n=int(input("Enter choice: "))
    if n==1:
        print("US dollar: " , (amount*76.46))
    elif n==2:
        print("Thai Bhatt: ",(amount*2.26))
    elif n==3:
        print("New Zealand Dollar: ",(amount*51.56))
    elif n==4:
        print("Canadian Dollar: ",(amount*60.60))
    elif n==5:
        print("Swedish Krona: ",(amount*8.01))
    elif n==6:
        break
    else:
        print("Invalid Output")
