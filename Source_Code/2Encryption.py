
#***************************************ENCRYPTION & SIGNING ***************************************
from ecdsa import SigningKey
from Crypto import Random
from Crypto.Util import number
import pem

def int_to_bytes(x):
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

def int_from_bytes(xbytes):
    return int.from_bytes(xbytes, 'big')

my_list1 = []
my_list2 = []
list_c2 = []
z = 9223372036854775807
w = 0

y = number.getRandomRange(1, (q-1), Random.new().read)
#y = 10
print ("Y chosen at random between 1 and ",q-1,"=",y)

#h = int(input("Enter Value of h : ")) 
print('')
print("\nType 1 to encrypt a String")
print("Type 2 to ecnrypt a Number")
k = int(input("Enter 1 or 2 : "))
f = int(input("Enter your user number : "))

if (k==1):
    
    string = input("Enter a String to be Encrypted : ")
    print('')

    for c in string:
        my_list1.append(c)
    
    for c in string:
        my_list2.append(ord(c)+w)
        w=w+1
        
        
    b = [str(x) for x in my_list2]
    r_int = ''.join(b)
    #r = int(r)
    
    r_enc = hash(r_int) % ((z + 1) * 2)
    
    data_integrity1 = hash(string) % ((z+1) * 2)
    print("Hash Value of Entered Message = ",data_integrity1)
    
    mbytes_enc = int_to_bytes(r_enc)
     
    
    if (f==1):
        sk1 = SigningKey.generate()
        vk1 = sk1.get_verifying_key()        
        open("private_key1.pem","wb").write(sk1.to_pem())
        open("public_key1.pem","wb").write(vk1.to_pem()) 
        sk1 = SigningKey.from_pem(open("private_key1.pem").read())
        sig = sk1.sign(mbytes_enc)

   
    elif (f==2):
        sk2 = SigningKey.generate()
        vk2 = sk2.get_verifying_key()
        open("private_key2.pem","wb").write(sk2.to_pem())
        open("public_key2.pem","wb").write(vk2.to_pem()) 
        sk2 = SigningKey.from_pem(open("private_key2.pem").read())
        sig = sk2.sign(mbytes_enc)

    
    elif (f==3):
        sk3 = SigningKey.generate()
        vk3 = sk3.get_verifying_key()
        open("private_key3.pem","wb").write(sk3.to_pem())
        open("public_key3.pem","wb").write(vk3.to_pem()) 
        sk3 = SigningKey.from_pem(open("private_key3.pem").read())
        sig = sk3.sign(mbytes_enc)

    
    elif (f==4):
        sk4 = SigningKey.generate()
        vk4 = sk4.get_verifying_key()
        open("private_key4.pem","wb").write(sk4.to_pem())
        open("public_key4.pem","wb").write(vk4.to_pem()) 
        sk4 = SigningKey.from_pem(open("private_key4.pem").read())
        sig = sk4.sign(mbytes_enc)

    
    elif (f==5):
        sk5 = SigningKey.generate()
        vk5 = sk5.get_verifying_key()
        open("private_key5.pem","wb").write(sk5.to_pem())
        open("public_key5.pem","wb").write(vk5.to_pem())     
        sk5 = SigningKey.from_pem(open("private_key5.pem").read())
        sig = sk5.sign(mbytes_enc)

    
    for i in range (0,(len(string))):
        c1 = pow(g,y,p)
        #c1 = (g**y) % p
        c2 = (((h)**y) * my_list2[i]) % p
        list_c2.append(c2)
        
        
        print("Cipher Text for",my_list1[i]) 
        print ("C1 =",c1)
        print ("C2 =",c2)
    
    print("List containing C2 of all characters part of input string : ")
    print(list_c2)    

elif (k==2):
    print('')
    m = int(input("Enter a Number to be Encrypted : "))
    print('')
    
    r = str(m)
    
    data_integrity1 = hash(r) % ((z+1) * 2)
    print("Hash Value of Entered Message = ",data_integrity1)
    
    r = hash(r) % ((z + 1) * 2)
    
    
    mbytes_enc = int_to_bytes(r)
    
    if (f==1):
        sk1 = SigningKey.generate()
        vk1 = sk1.get_verifying_key()        
        open("private_key1.pem","wb").write(sk1.to_pem())
        open("public_key1.pem","wb").write(vk1.to_pem()) 
        sk1 = SigningKey.from_pem(open("private_key1.pem").read())
        sig = sk1.sign(mbytes_enc)
        
   
    elif (f==2):
        sk2 = SigningKey.generate()
        vk2 = sk2.get_verifying_key()
        open("private_key2.pem","wb").write(sk2.to_pem())
        open("public_key2.pem","wb").write(vk2.to_pem()) 
        sk2 = SigningKey.from_pem(open("private_key2.pem").read())
        sig = sk2.sign(mbytes_enc)
        
    
    elif (f==3):
        sk3 = SigningKey.generate()
        vk3 = sk3.get_verifying_key()
        open("private_key3.pem","wb").write(sk3.to_pem())
        open("public_key3.pem","wb").write(vk3.to_pem()) 
        sk3 = SigningKey.from_pem(open("private_key3.pem").read())
        sig = sk3.sign(mbytes_enc)
        
    
    elif (f==4):
        sk4 = SigningKey.generate()
        vk4 = sk4.get_verifying_key()
        open("private_key4.pem","wb").write(sk4.to_pem())
        open("public_key4.pem","wb").write(vk4.to_pem()) 
        sk4 = SigningKey.from_pem(open("private_key4.pem").read())
        sig = sk4.sign(mbytes_enc)
        
    
    elif (f==5):
        sk5 = SigningKey.generate()
        vk5 = sk5.get_verifying_key()
        open("private_key5.pem","wb").write(sk5.to_pem())
        open("public_key5.pem","wb").write(vk5.to_pem())     
        sk5 = SigningKey.from_pem(open("private_key5.pem").read())
        sig = sk5.sign(mbytes_enc)
        
        
    #hm = hash(m)
    #print ("Hash value of your message : ",hm)

    c1 = pow(g,y,p) 
    #c1 = (g**y) % p
    c2 = (((h)**y) * m) % p

    print("Cipher Text =") 
    print ("C1 =",c1)
    print ("C2 =",c2)

else: 
    print("Invalid Choice")