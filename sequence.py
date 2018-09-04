#1 búa til breytur fyrir rununa
#2 Gera for lykkju sem keyrir og plúsar saman
#3 prentar út fjölda tala sem inputið er.

n = int(input("Enter the length of the sequence: ")) # Do not change this line

a1 = 1
a2 = 2
a3 = 3
sum_int = 0

print (a1)
print (a2)
print (a3)

for i in range (n-3):
  sum_int = a1 + a2 + a3
  print (sum_int)
  a1 = a2
  a2 = a3
  a3 = sum_int

