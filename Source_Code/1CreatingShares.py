
#***************************************CALCULATING SHARES***************************************

from Crypto.Util import number
from Crypto import Random

n = 5
t = 3


my_list = []

s = int(input("\nEnter Your Secret : "))
my_list.append(s)


for i in range(1,t):
    CryptoRandomNumber = number.getRandomRange(1, 88, Random.new().read)
    my_list.append(CryptoRandomNumber)

#my_list[2] = 15
#my_list[1] = 14

print("")       
print("Creating Shares of Your Secret")       
print("")

for i in range(1,n+1):
    share = ((my_list[2]*(i**2))+(my_list[1]*i)+(my_list[0]))%q
    print("Share of your Secret for user number",i,"=",share)

