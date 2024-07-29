import random
ran=random.randint(1,10)
print(ran)
chances=3
while chances>=1:
    guess=int(input("enter the number:"))
    if guess==ran:
        print('congrats')
        break
    else:
        chances-=1
        continue
if chances<1:
    print('failed try next time')    
