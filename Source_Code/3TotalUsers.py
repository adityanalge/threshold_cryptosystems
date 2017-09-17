#***************************************USERS PRESENT***************************************

v=0

while v==0:
    num = int(input("Enter number of users present "))
    
    if (num <= 0 or num >5):
        print("Invalid Choice! Choose Again")
        
    if (0< num < 3):
        print("Not Enough Users ! Choose Again")   

    elif num==3:
        v=1  
        
        while True:
            u1 = int(input("Enter the user number of the first user : "))
            u2 = int(input("Enter the user number of the second user : "))
            u3 = int(input("Enter the user number of the third user : "))
            if((u1 <= 0) or (u1>5) or (u2<=0) or (u2>5) or (u3 <= 0) or (u3 > 5)):
                print("\nInvalid User Number! Re Enter")
            else:
                break;
                
    elif num==4:       
        v=1  
        
        while True:
            u1 = int(input("Enter the user number of the first user : "))
            u2 = int(input("Enter the user number of the second user : "))
            u3 = int(input("Enter the user number of the third user : "))
            u4 = int(input("Enter the user number of the fourth user : "))
            
            if((u1 <= 0) or (u1>5) or (u2<=0) or (u2>5) or (u3 <= 0) or (u3 > 5) or (u4 <= 0) or (u4 > 5)):                
                print("\nInvalid User Number! Re Enter")
            else:
                break;
                
    elif num==5:
        v=1   
        
        while True:
            u1 = int(input("Enter the user number of the first user : "))
            u2 = int(input("Enter the user number of the second user : "))
            u3 = int(input("Enter the user number of the third user : "))
            u4 = int(input("Enter the user number of the fourth user : "))
            u5 = int(input("Enter the user number of the fifth user : "))
        
            if((u1 <= 0) or (u1>5) or (u2<=0) or (u2>5) or (u3 <= 0) or (u3 > 5) or (u4 <= 0) or (u4 > 5) or (u4 <= 0) or (u5 > 5) ):
                print("\nInvalid User Number! Re Enter")
            else:
                break;
