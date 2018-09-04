#1 búa til breytur fyrir rununa
#2 Gera for lykkju sem keyrir og plúsar saman
#3 prentar út fjölda tala sem inputið er.

n = int(input("Enter the length of the sequence: ")) # Do not change this line

n1 = 1
n2 = 2
n3 = 3
sum_int = 0

print (n1)
print (n2)
print (n3)

for i in range (n-3):
  sum_int = n1 + n2 + n3
n1 = n2
n2 = n3
n3 = sum_int

print (sum_int)