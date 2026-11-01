import random

def choices():
    num = [1,2,3,4,5,6]
    y = gamble(num)
    return y
    
def gamble(a):
    x = random.choice(a)
    return x

name = str(input("Enter your name :\t"))
money = float(input("Enter your money order\n(minimum order size 100) :\t"))
              
def m():
    global money
    
    start = choices()
    if start == 6:
        print("\nWOW! JACKPOT YOU GOT +1 point :-)\n\n\t\t%d"%(start))
        money = money*2
    else:
        print(f"\nYOU GOT NUMBER {start}, BETTER LUCK NEXT TIME :-(")
        money = money - 10
        
    restart = int(input("\nEnter 1 to restart / 0 to stop :\t"))
    if restart == 1 and money>0:
        m()
    else:
        print(f"\nThank you for playing {name} !")
        print("YOURS TOTAL EARNING IS %0.2f !"%money)
m()       