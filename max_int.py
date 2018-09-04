#1 Byrja á því að gera while lykkju til að skoða hvort inputið sé tala
#2 Kerfið hætti að keyra þegar neikvæð tala er slegin inn
#3 Þegar kerfið hættir að keyra að það prenti út 

num_int = int(input("Input a number: "))
max_int = 0
while num_int >= 0:
  num_int = int(input("Input a number: "))
  if num_int > max_int :
     max_int = num_int

print("The maximum is", max_int)
