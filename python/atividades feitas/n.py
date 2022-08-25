s1=[]
s2=[]
s3=[]
s4=[]
s5=[]

import random
import string, random

pc = random.randint(1,9)
pc6=("@")
pc5=random.choice(string.ascii_letters)
pc2 = random.randint(1,5)
pc3 = random.randint(15,99) 
pc4=random.choice(string.ascii_letters)



r2=int(input('escola um numero de 1 á 5 !digite 0 para parar! : '))

while r2 != 0 :
   r2=int(input('escola um numero de 1 á 5 !digite 0 para parar! : '))
   if r2 == 1:
         s1=(pc2,pc6,pc3,pc,pc4,pc5)
         print(s1)

   if r2 == 2:
         s2=(pc,pc5,pc2,pc3,pc6,pc4)
         print(s2)
   if r2 == 3:
         s3=(pc,pc5,pc6,pc,pc2,pc3)
         print(s3)      
   if r2 == 4:
         s4=(pc2,pc6,pc3,pc,pc4,pc5)
         print(s4)      
   if r2 == 5:
         s5=(pc5,pc2,pc4,pc3,pc6,pc)
         print(s5)
      

   