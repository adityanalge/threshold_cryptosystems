
#*************************** CREATING DECRYPTION SHARES ***************************************

def invmodp(a, b):

    for d in range(1, b):
        r = (d * a) % b
        if r == 1:
            break
    else:
        raise ValueError('%d has no inverse mod %d' % (a, b))
    return d

if (num ==3):
    
    u = int(input("\nEnter your user number : "))
    
    if (u == 1):
        if(u == u1):
            t = int(input("Enter your share :"))
            s = (t * ((u2*u3) * invmodp(((u2-u1)*(u3-u1)),q)))
            print("Your Decryption Share Is =",(pow(c1,s,p)))
        
        elif(u == u2):
            t = int(input("Enter your share :"))
            s = (t * ((u1*u3) * invmodp(((u1-u2)*(u3-u2)),q)))
            print("Your Decryption Share Is =",(pow(c1,s,p)))
        
        elif(u == u3):
            t = int(input("Enter your share :"))
            s = (t * ((u1*u2) * invmodp(((u2-u3)*(u1-u3)),q)))
            print("Your Decryption Share Is =",(pow(c1,s,p)))
        else:
            print("User Not Present")
    
    elif (u == 2):
        if(u == u1):
            t = int(input("Enter your share :"))
            s = (t * ((u2*u3) * invmodp(((u2-u1)*(u3-u1)),q)))
            print("Your Decryption Share Is =",(pow(c1,s,p)))
        
        elif(u == u2):
            t = int(input("Enter your share :"))
            s = (t * ((u1*u3) * invmodp(((u1-u2)*(u3-u2)),q)))
            print("Your Decryption Share Is =",(pow(c1,s,p)))
        
        elif(u == u3):
            t = int(input("Enter your share :"))
            s = (t * ((u1*u2) * invmodp(((u2-u3)*(u1-u3)),q)))
            print("Your Decryption Share Is =",(pow(c1,s,p)))
        else:
            print("User Not Present")        
   
    elif (u == 3):
        if(u == u1):
            t = int(input("Enter your share :"))
            s = (t * ((u2*u3) * invmodp(((u2-u1)*(u3-u1)),q)))
            print("Your Decryption Share Is =",(pow(c1,s,p)))
        
        elif(u == u2):
            t = int(input("Enter your share :"))
            s = (t * ((u1*u3) * invmodp(((u1-u2)*(u3-u2)),q)))
            print("Your Decryption Share Is =",(pow(c1,s,p)))
        
        elif(u == u3):
            t = int(input("Enter your share :"))
            s = (t * ((u1*u2) * invmodp(((u2-u3)*(u1-u3)),q)))
            print("Your Decryption Share Is =",(pow(c1,s,p)))
        else:
            print("User Not Present")
    
    elif (u == 4) :   
        if(u == u1):
            t = int(input("Enter your share :"))
            s = (t * ((u2*u3) * invmodp(((u2-u1)*(u3-u1)),q)))
            print("Your Decryption Share Is =",(pow(c1,s,p)))
        
        elif(u == u2):
            t = int(input("Enter your share :"))
            s = (t * ((u1*u3) * invmodp(((u1-u2)*(u3-u2)),q)))
            print("Your Decryption Share Is =",(pow(c1,s,p)))
        
        elif(u == u3):
            t = int(input("Enter your share :"))
            s = (t * ((u1*u2) * invmodp(((u2-u3)*(u1-u3)),q)))
            print("Your Decryption Share Is =",(pow(c1,s,p)))
        else:
            print("User Not Present")
    
    elif (u == 5) :   
        if(u == u1):
            t = int(input("Enter your share :"))
            s = (t * ((u2*u3) * invmodp(((u2-u1)*(u3-u1)),q)))
            print("Your Decryption Share Is =",(pow(c1,s,p)))
        
        elif(u == u2):
            t = int(input("Enter your share :"))
            s = (t * ((u1*u3) * invmodp(((u1-u2)*(u3-u2)),q)))
            print("Your Decryption Share Is =",(pow(c1,s,p)))
        
        elif(u == u3):
            t = int(input("Enter your share :"))
            s = (t * ((u1*u2) * invmodp(((u2-u3)*(u1-u3)),q)))
            print("Your Decryption Share Is =",(pow(c1,s,p)))
        
        else:
            print("User Not Present")
            

elif(num ==4):
    
    u = int(input("\nEnter your user number :"))
    
    if (u == 1):
        if(u == u1):
            t = int(input("Enter your share :"))
            s = (t * ((u2*u3*u4) * invmodp(((u2-u1)*(u3-u1)*(u4-u1)),q)))
            print("Your Decryption Share Is =",(pow(c1,s,p)))
        
        elif(u == u2):
            t = int(input("Enter your share :"))
            s = (t * ((u1*u3*u4) * invmodp(((u1-u2)*(u3-u2)*(u4-u2)),q)))
            print("Your Decryption Share Is =",(pow(c1,s,p)))
        
        elif(u == u3):
            t = int(input("Enter your share :"))
            s = (t * ((u1*u2*u4) * invmodp(((u1-u3)*(u2-u3)*(u4-u3)),q)))
            print("Your Decryption Share Is =",(pow(c1,s,p)))
            
        elif(u == u4):
            t = int(input("Enter your share :"))
            s = (t * ((u1*u2*u3) * invmodp(((u1-u4)*(u2-u4)*(u3-u4)),q)))
            print("Your Decryption Share Is =",(pow(c1,s,p)))
            
        else:
            print("User Not Present")
    
    if (u == 2):
        if(u == u1):
            t = int(input("Enter your share :"))
            s = (t * ((u2*u3*u4) * invmodp(((u2-u1)*(u3-u1)*(u4-u1)),q)))
            print("Your Decryption Share Is =",(pow(c1,s,p)))
        
        elif(u == u2):
            t = int(input("Enter your share :"))
            s = (t * ((u1*u3*u4) * invmodp(((u1-u2)*(u3-u2)*(u4-u2)),q)))
            print("Your Decryption Share Is =",(pow(c1,s,p)))
        
        elif(u == u3):
            t = int(input("Enter your share :"))
            s = (t * ((u1*u2*u4) * invmodp(((u1-u3)*(u2-u3)*(u4-u3)),q)))
            print("Your Decryption Share Is =",(pow(c1,s,p)))
            
        elif(u == u4):
            t = int(input("Enter your share :"))
            s = (t * ((u1*u2*u3) * invmodp(((u1-u4)*(u2-u4)*(u3-u4)),q)))
            print("Your Decryption Share Is =",(pow(c1,s,p)))
            
        else:
            print("User Not Present")
            
    if (u == 3):
        if(u == u1):
            t = int(input("Enter your share :"))
            s = (t * ((u2*u3*u4) * invmodp(((u2-u1)*(u3-u1)*(u4-u1)),q)))
            print("Your Decryption Share Is =",(pow(c1,s,p)))
        
        elif(u == u2):
            t = int(input("Enter your share :"))
            s = (t * ((u1*u3*u4) * invmodp(((u1-u2)*(u3-u2)*(u4-u2)),q)))
            print("Your Decryption Share Is =",(pow(c1,s,p)))
        
        elif(u == u3):
            t = int(input("Enter your share :"))
            s = (t * ((u1*u2*u4) * invmodp(((u1-u3)*(u2-u3)*(u4-u3)),q)))
            print("Your Decryption Share Is =",(pow(c1,s,p)))
            
        elif(u == u4):
            t = int(input("Enter your share :"))
            s = (t * ((u1*u2*u3) * invmodp(((u1-u4)*(u2-u4)*(u3-u4)),q)))
            print("Your Decryption Share Is =",(pow(c1,s,p)))
            
        else:
            print("User Not Present")
            
    if (u == 4):
        if(u == u1):
            t = int(input("Enter your share :"))
            s = (t * ((u2*u3*u4) * invmodp(((u2-u1)*(u3-u1)*(u4-u1)),q)))
            print("Your Decryption Share Is =",(pow(c1,s,p)))
        
        elif(u == u2):
            t = int(input("Enter your share :"))
            s = (t * ((u1*u3*u4) * invmodp(((u1-u2)*(u3-u2)*(u4-u2)),q)))
            print("Your Decryption Share Is =",(pow(c1,s,p)))
        
        elif(u == u3):
            t = int(input("Enter your share :"))
            s = (t * ((u1*u2*u4) * invmodp(((u1-u3)*(u2-u3)*(u4-u3)),q)))
            print("Your Decryption Share Is =",(pow(c1,s,p)))
            
        elif(u == u4):
            t = int(input("Enter your share :"))
            s = (t * ((u1*u2*u3) * invmodp(((u1-u4)*(u2-u4)*(u3-u4)),q)))
            print("Your Decryption Share Is =",(pow(c1,s,p)))
            
        else:
            print("User Not Present")
            
elif(num ==5):
    u = int(input("\nEnter your user number :"))
    
    if (u == 1):
        t = int(input("Enter your share :"))
        s = (t * ((u2*u3*u4*u5) * invmodp(((u2-u1)*(u3-u1))*(u4-u1)*(u5-u1),q)))
        print("Your Decryption Share Is =",(pow(c1,s,p)))
        
    elif (u == 2):
        t = int(input("Enter your share :"))
        s = (t * ((u1*u3*u4*u5) * invmodp(((u1-u2)*(u3-u2))*(u4-u2)*(u5-u2),q)))
        print("Your Decryption Share Is =",(pow(c1,s,p)))
    
    elif (u == 3):
        t = int(input("Enter your share :"))
        s = (t * ((u1*u2*u4*u5) * invmodp(((u1-u3)*(u2-u3))*(u4-u3)*(u5-u3),q)))
        print("Your Decryption Share Is =",(pow(c1,s,p)))
        
    elif (u == 4):
        t = int(input("Enter your share :"))
        s = (t * ((u1*u2*u3*u5) * invmodp(((u1-u4)*(u2-u4))*(u3-u4)*(u5-u4),q)))
        print("Your Decryption Share Is =",(pow(c1,s,p)))
    
    elif (u == 5):
        t = int(input("Enter your share :"))
        s = (t * ((u1*u2*u3*u4) * invmodp(((u1-u5)*(u2-u5))*(u3-u5)*(u4-u5),q)))
        print("Your Decryption Share Is =",(pow(c1,s,p)))
        
    else:
            print("User Not Present")