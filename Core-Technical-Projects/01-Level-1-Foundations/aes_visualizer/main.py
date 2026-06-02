#encrypt
word = "SECRET"
import random
xor = random.randint(0,100)
#print(xor)
a = []
for i in word:
  a.append(str(ord(i) ^ xor).zfill(3))
encrypt = "".join(str(i) for i in a)+str(bin(xor)[2:].zfill(10))
print(f"The encrypted message is: {encrypt}")

#decrypt
rox = int(encrypt[-10:],2)
#print(rox)
l=[]
for x in range(0,len(encrypt)-10,3):
  var = int(encrypt[x:x+3])^rox
  l.append(chr(var))
  var = "".join(str(x) for x in l)
print(f"{encrypt} is decoded as {var}")





