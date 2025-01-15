def how_big(x):
    if x > 10:
         print('huge')
    elif x > 5:
         return 'big'
    if x > 0:
         print('positive')
    else:
       print(0)


n = 3
while n >= 0:  # If this loops forever, just type Infinite Loop
     n -= 1
     print(n)

negative = -12
while negative: # If this loops forever, just type Infinite Loop
    if negative + 6:
       print(negative)
    negative += 3