import random
import time

print("Welcome to Blackjack Game!")
time.sleep(1)

card_types = ['Spades','Hearts','Clubs','Diamonds']
special_cards = ['King' ,'Queen' ,'Jack']

a = random.randint(1,14) 
if a > 10:
    a = random.choice(special_cards) 
  
b = random.randint(1,14) 
if b > 10:
    b = random.choice(special_cards) 

c = random.randint(1,14)
if c > 10:
    c = random.choice(special_cards)

d = random.randint(1,14)
if d > 10:
    d = random.choice(special_cards)


m = random.randint(1,14) 
if m > 10:
    m = random.choice(special_cards)

n = random.randint(1,14) 
if n > 10:
    n = random.choice(special_cards)

s = random.randint(1,14) 
if s > 10:
    s = random.choice(special_cards)

q = random.randint(1,14) 
if q > 10:
    q = random.choice(special_cards)


   
x = random.choice(card_types)
y = random.choice(card_types)
z = random.choice(card_types)
t = random.choice(card_types)
r = random.choice(card_types)
u = random.choice(card_types)
d = random.choice(card_types)
ü = random.choice(card_types)


print("Your first card is :" , a , "of" , x)
time.sleep(1)
print("Your second card is :" , b , "of" , y)
time.sleep(1)

if type(a) == str:
    a = int(10)
if type(b) == str:
    b = int(10)
if type(c) == str:
    c = int(10)
if type(d) == str:
    d = int(10)

if type(m) == str:
    m = int(10)
if type(n) == str:
    n = int(10)
if type(s) == str:
    s = int(10)
if type(q) == str:
    q = int(10)
    
print("Your total is:" , a + b)
time.sleep(1)

print("Now opposite side is drawing their cards.")
time.sleep(1)
print("Two cards have been drawed. One of them is :" , m , "of" , z)

k = input("Do you want to draw a card? yes/no :")

if k == 'yes' :
    time.sleep(1)
    print("The card you drew is :" , c ,"of" , t)
    time.sleep(1)
    print("Your new total is:" , a + b + c)
    hand = a+b+c
    if a+b+c > 21 :
        print("Your hand is greater than 21. You have lost the game!")
        time.sleep(1)
        print("Thanks for playing! See you next round.")
    elif a+b+c < 21 :
        one_more = input("Do you want one more? yes/no :")
        if one_more == 'yes' :
            time.sleep(1)
            print("That was your last right to draw a card.")
            time.sleep(1)
            print("The card you drew is :" , c ,"of" , r)
            time.sleep(1)
            print("Your new total is:"  , a+b+c+d)
            hand = a+b+c+d
            if (a+b+c+d > 21):
                print("Your hand is greater than 21.")
        elif one_more == 'no' :
            time.sleep(1)
            print("Your hand is the same.")
        else :
            print("Please enter only 'yes' or 'no'.Game is now shutting down. Please restart the game! ")
elif k == 'no' :
    time.sleep(1)
    print("Your hand is still the same")
    hand = a + b
else :
    time.sleep(1)
    print("Please enter only 'yes' or 'no' .Game is now shutting down. Please restart the game!")

print("Opposite side's second card is :" , n , "of" , u)

if (m+n) < 21 :
    time.sleep(1)
    print("Opposite side is drawing..")
    time.sleep(1)
    print("They drawed:" , s , "of" , ü)
    time.sleep(1)
    print("Their new total is:" , m+n+s)
    if (m+n+s) < 21 :
        time.sleep(1)
        print("Opposite side continues.")
        time.sleep(1)
        print("They drawed:" , q , "of" , ü)
        time.sleep(1)
        print("Their new total is:" , m+n+s+q)
        if (m+n+s+q > 21):
            time.sleep(1)
            print("Their hand is greater than 21.")
            if hand > 21 :
                time.sleep(1)
                print("It's a tie!")
        elif (m+n+s+q < 21):
            time.sleep(1)
            print("That was their last right to draw a card")
            time.sleep(1)
            print("Their final hand is : " , m+s+n+q)
            if m+s+n+q > hand :
                time.sleep(1)
                print("You have lost the game. Try again!")
            elif m+n+s+q == hand :
                time.sleep(1)
                print("It's a tie!")
            else :
                time.sleep(1)
                print("Congratulations! You have won the game.")
    elif (m+n+s) > 21 :
        time.sleep(1)
        print("The opposite side's hand is greater than 21.")
        if hand > 21 :
            time.sleep(1)
            print("It's a tie!")
        elif hand <= 21 :
            time.sleep(1)
            print("Congratulations! You have won the game.")
    else :
        time.sleep(1)
        print("The opposite side's hand is 21.")
        if hand == m+n+s :
            time.sleep(1)
            print("It's a tie!")
        else :
            time.sleep(1)
            print("You have lost the game. Try again!")
elif (m + n == 21):
    time.sleep(1)
    print("Their hand is 21.")
    if hand == m + n :
        time.sleep(1)
        print("It's a tie game!")
    else :
        time.sleep(1)
        print("You have lost the game. Try again!")



        









   



