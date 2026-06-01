chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#number = int(input("Enter a number: "))
#base = int(input("Enter a base: "))
def dec_custom(number=0, base=0):
   rem = []
   while number > 0:
     rem.append(chars[int(number % base)])
     number = number // base
   rem.reverse()
   return ("".join(rem))

def custom_dec(custom="00", current_base=0):
  val = 0
  power = len(custom)
  for i in custom:
    if i.isalpha():
      i = i.upper()
    val += chars.index(i)*current_base**(power-1)
    power -= 1
  return val

