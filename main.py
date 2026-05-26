p = input("Enter a number(Decimal):")
try:
  x = int(p)
except ValueError:
  x = float(p)
l = []
def dec_bin(x):
  if type(x) == int:
    if x == 0 or x ==1:
      l.append(x) 
      return "".join(map(str,l[::-1]))
    else:
      l.append(x%2)
      x = x//2
      dec_bin(x)
  if type(x) == float:
    z = int(x)
    i = dec_bin(z)
    if x-z !=0 or x-z!=1:
      l.append(int((x-z)*2))
      f= dec_bin(((x-z)*2-int((x-z)*2)))
    else:
      l.append(x-z)
    
      
  dec_bin(x)

