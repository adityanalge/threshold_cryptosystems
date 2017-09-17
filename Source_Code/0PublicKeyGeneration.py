
#***************************************KEY GENERATION***************************************
#max = 9223372036854775807
#p = 6744073709551523
#q = 3372036854775761
#p = 209459
#q = 104729

p = 179
q = 89
g = 49

while True:
    x1 = int(input("User 1 - choose a random number between 0 and " + str(q) + " : "))
    if (0 < x1 < q):
        break;
    else:
        print ("Error! Choose Again")
h1 = pow(g,x1,p)
#h1 = (g**x1) % p


while True:
    x2 = int(input("User 2 - choose a random number between 0 and " + str(q) + " : "))
    if (0 < x2 < q):
        break;
    else:
        print ("Error! Choose Again")  
h2 = pow(g,x2,p)
#h2 = (g**x2) % p


while True:
    x3 = int(input("User 3 - choose a random number between 0 and " + str(q) + " : "))
    if (0 < x3 < q):
        break;
    else:
        print ("Error! Choose Again")
h3 = pow(g,x3,p)
#h3 = (g**x3) % p
     

while True:
    x4 = int(input("User 4 - choose a random number between 0 and " + str(q) + " : "))
    if (0 < x4 < q):
        break;
    else:
        print ("Error! Choose Again")
h4 = pow(g,x4,p)
#h4 = (g**x4) % p
     

while True:
    x5 = int(input("User 5 - choose a random number between 0 and " + str(q) + " : "))
    if (0 < x5 < q):
        break;
    else:
        print ("Error! Choose Again")
h5 = pow(g,x5,p)
#h5 = (g**x5) % p

h = (h1 * h2 * h3 * h4 * h5) % p

f = open('PublicKey.txt','w')
f.write("Public Key is -\n")
f.write("p =")
f.write(str(p))
f.write("\tq =")
f.write(str(q))
f.write("\tg =")
f.write(str(g))
f.write("\th =")
f.write(str(h))
f.write(' ')
f.close()

print ("\n\npublic key - p =",p, " q =",q," g =",g," h =",h)