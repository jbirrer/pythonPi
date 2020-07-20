#Pi annähern mit Hilfe von Pythagoras Yarek Huber, Joël Birrer

from random import *
x = 0
y = 0 # X und Y setzen wir 0, da wir später Werte dazuaddieren werden
t = int(input("Wie viele Punkte sollen generiert werden?"))

#Je mehr Punkte, desto genauer ist Pi und desto länger läuft das Programm.

if t < 10:
  print("Bitte eine groessere Zahl eingeben.") 
  #hier wird gesichert, dass genug punkte eingegeben werden, da es sonst eine division durch 0 ergeben würde
  exit()
print

from turtle import *
r = 300 #=radius
speed(0)

left(90) #hier wird das raster gezeichnet
forward(r)
left(90)
circle(r,90)
for i in range(4):
  left(90)
  forward(r)

for i in range(1,t):
  a=random()
  b=random()
  penup()
  aa = -(a * r) 
  bb = (b * r) 
  setpos(aa,bb)
  pendown()

  if (a**2+b**2)<=1:
    x +=1.0
    dot(0.1, "blue")
  else:
    y+=1.0
    dot(0.1, "red")
  if i % (t/10.0) == 0:
    print i, "Punkte"
    
z = x / (x+y)*4.0
print "-" * 50
print z
print "-" * 50

pi = 3.14159265359
print "Im Vergleich zu Pi:", pi
diff = pi - z
if diff < 0:
  diff =  diff * (-1)
print "Die Differenz bei", t, "Punkten ist:", diff
