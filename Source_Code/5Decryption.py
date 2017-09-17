
#********************** DECRYPTION & VERIFYING ***************************************
from ecdsa import VerifyingKey, BadSignatureError
import pem

message_list = []
message_list1 = []
my_list3 = []
my_list4 = []
a = 'a'
e = 0
w = 0

print("\nType 1 to decrypt a String")
print("Type 2 to decrypt a Number")

k = int(input("Enter 1 or 2 : "))  

if (k==1):
    #list_c2 = input("Enter List c2 : ")    

    if (num ==3):
        d1 = int(input("Please Enter First Decryption Share : "))
        d2 = int(input("Please Enter Second Decryption Share : "))
        d3 = int(input("Please Enter Third Decryption Share : "))
    
        d = (d1 * d2 * d3) % p

    if (num ==4):
        d1 = int(input("Please Enter First Decryption Share : "))
        d2 = int(input("Please Enter Second Decryption Share : "))
        d3 = int(input("Please Enter Third Decryption Share : "))
        d4 = int(input("Please Enter Fourth Decryption Share : "))
        
        d = (d1 * d2 * d3 * d4) % p

    if (num ==5):
        d1 = int(input("Please Enter First Decryption Share : "))
        d2 = int(input("Please Enter Second Decryption Share : "))
        d3 = int(input("Please Enter Third Decryption Share : "))
        d4 = int(input("Please Enter Fourth Decryption Share : "))
        d5 = int(input("Please Enter Fifth Decryption Share : "))
        
        d = (d1 * d2 * d3 * d4 * d5) % p
    
    for i in range(0,len(list_c2)):
        message_list1.append(a)
        
    for i in range (0,len(list_c2)):
        m = ( list_c2[i] * invmodp(d,p)) % p 
        message_list.append(m-w)
        w=w+1
        
    for i in range(0,len(list_c2)):
        message_list1[i] = chr(message_list[i])
    
    r = ''.join(message_list1)
    #print("\nOriginal Message Is =", r)
    
    string = r
    
    data_integrity2 = hash(r) % ((z+1) * 2)
    print("Hash Value of Recovered Message = ",data_integrity2)
    
    for c in string:
        my_list3.append(c)
    
    for c in string:
        my_list4.append(ord(c))
     
    b_dec = [str(x) for x in my_list4]
    r_dec_int = ''.join(b)
    #r = int(r)
    
    r_dec = hash(r_dec_int) % ((z + 1) * 2)
    
    
    
    mbytes_dec = int_to_bytes(r_dec)

    if (f==1):
        try:
            vk1 = VerifyingKey.from_pem(open("public_key1.pem").read())
            assert vk1.verify(sig, mbytes_dec)
            print("\nSIGNATURE IS VALID !! \nMessage was Encrypted by User 1")
            print("\nOriginal Message Is =", r)
            e=1
        except BadSignatureError:
            print ("\nNot a Valid Signature!!")
    elif (f==2):
        try:
            vk2 = VerifyingKey.from_pem(open("public_key2.pem").read())
            assert vk2.verify(sig, mbytes_dec)
            print("\nSIGNATURE IS VALID !! \nMessage was Encrypted by User 2")
            print("\nOriginal Message Is =", r)
            e=1
        except BadSignatureError:
            print ("\nNot a Valid Signature!!")
    elif (f==3):
        try:
            vk3 = VerifyingKey.from_pem(open("public_key3.pem").read())
            assert vk3.verify(sig, mbytes_dec)
            print("\nSIGNATURE IS VALID !! \nMessage was Encrypted by User 3")
            print("\nOriginal Message Is =", r)
            e=1
        except BadSignatureError:
            print ("\nNot a Valid Signature!!")
    elif (f==4):
        try:
            vk4 = VerifyingKey.from_pem(open("public_key4.pem").read())
            assert vk4.verify(sig, mbytes_dec)
            print("\nSIGNATURE IS VALID !! \nMessage was Encrypted by User 4")
            print("\nOriginal Message Is =", r)
            e=1
        except BadSignatureError:
            print ("\nNot a Valid Signature!!")
    elif (f==5):
        try:
            vk5 = VerifyingKey.from_pem(open("public_key5.pem").read())
            assert vk5.verify(sig, mbytes_dec)
            print("\nSIGNATURE IS VALID !! \nMessage was Encrypted by User 5")
            print("\nOriginal Message Is =", r)
            e=1
        except BadSignatureError:
            print ("\nNot a Valid Signature!!")
     
    if (e==0):
         print("Message sent from unauthorised source")
         
elif (k==2):
    
    c2 = int(input("\nEnter C2 : "))
    if (num ==3):
        d1 = int(input("Please Enter First Decryption Share : "))
        d2 = int(input("Please Enter Second Decryption Share : "))
        d3 = int(input("Please Enter Third Decryption Share : "))
    
        d = (d1 * d2 * d3) % p

    if (num ==4):
        d1 = int(input("Please Enter First Decryption Share : "))
        d2 = int(input("Please Enter Second Decryption Share : "))
        d3 = int(input("Please Enter Third Decryption Share : "))
        d4 = int(input("Please Enter Fourth Decryption Share : "))
        
        d = (d1 * d2 * d3 * d4) % p

    if (num ==5):
        d1 = int(input("Please Enter First Decryption Share : "))
        d2 = int(input("Please Enter Second Decryption Share : "))
        d3 = int(input("Please Enter Third Decryption Share : "))
        d4 = int(input("Please Enter Fourth Decryption Share : "))
        d5 = int(input("Please Enter Fifth Decryption Share : "))
        
        d = (d1 * d2 * d3 * d4 * d5) % p

    m = ( c2 * invmodp(d,p)) % p 
    #print("\nOriginal Message Is =", m)
    
    r = str(m)
    
    r = hash(r) % ((z + 1) * 2)
    
    l=str(m)
    data_integrity2 = hash(l) % ((z+1) * 2)
    
    mbytes_dec = int_to_bytes(r)
    
    if f==1:
        try:
            vk1 = VerifyingKey.from_pem(open("public_key1.pem").read())
            assert vk1.verify(sig, mbytes_dec)
            print("\nSIGNATURE IS VALID !! \nMessage was Encrypted by User 1")
            print("\nOriginal Message Is =", m)
            if data_integrity1 == data_integrity2:
                print("Message Integrity is Not Compromised")
            else:
                print("Message Integrity is Compromised!!!")
            e=1
            print("Hash Value of Recovered Message = ",data_integrity2) 
        except BadSignatureError:
            print ("\nNot a Valid Signature!!")
    elif f==2:
        try:
            vk2 = VerifyingKey.from_pem(open("public_key2.pem").read())
            assert vk2.verify(sig, mbytes_dec)
            print("\nSIGNATURE IS VALID !! \nMessage was Encrypted by User 2")
            print("\nOriginal Message Is =", m)
            if data_integrity1 == data_integrity2:
                print("Message Integrity is Not Compromised")
            else:
                print("Message Integrity is Compromised!!!")
            e=1
            print("Hash Value of Recovered Message = ",data_integrity2)
        except BadSignatureError:
            print ("\nNot a Valid Signature!!")
    elif f==3:
        try:
            vk3 = VerifyingKey.from_pem(open("public_key3.pem").read())
            assert vk3.verify(sig, mbytes_dec)
            print("\nSIGNATURE IS VALID !! \nMessage was Encrypted by User 3")
            print("\nOriginal Message Is =", m)
            if data_integrity1 == data_integrity2:
                print("Message Integrity is Not Compromised")
            else:
                print("Message Integrity is Compromised!!!")
            e=1
            print("Hash Value of Recovered Message = ",data_integrity2)
        except BadSignatureError:
            print ("\nNot a Valid Signature!!")
    elif f==4:
        try:
            vk4 = VerifyingKey.from_pem(open("public_key4.pem").read())
            assert vk4.verify(sig, mbytes_dec)
            print("\nSIGNATURE IS VALID !! \nMessage was Encrypted by User 4")
            print("\nOriginal Message Is =", m)
            if data_integrity1 == data_integrity2:
                print("Message Integrity is Not Compromised")
            else:
                print("Message Integrity is Compromised!!!")
            e=1
            print("Hash Value of Recovered Message = ",data_integrity2)
        except BadSignatureError:
            print ("\nNot a Valid Signature!!")
    elif f==5:
        try:
            vk5 = VerifyingKey.from_pem(open("public_key5.pem").read())
            assert vk5.verify(sig, mbytes_dec)
            print("\nSIGNATURE IS VALID !! \nMessage was Encrypted by User 5")
            print("\nOriginal Message Is =", m)
            if data_integrity1 == data_integrity2:
                print("Message Integrity is Not Compromised")
            else:
                print("Message Integrity is Compromised!!!")
            e=1
            print("Hash Value of Recovered Message = ",data_integrity2)
        except BadSignatureError:
            print ("\nNot a Valid Signature!!")
     
    if (e==0):
         print("\nMessage sent from unauthorised source!!!")

         
else:
    print("Invalid Choice! Choose Again")
