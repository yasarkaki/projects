print("Welcome To Holiday Calculator")

print("Sunday : 0")
print("Monday : 1")
print("Tuesday: 2")
print("Wednesday: 3")
print("Thursday : 4")
print("Friday : 5")
print("Saturday : 6")

entree = int(input("Please enter first day of your holiday : "))


if not 0 <= entree <= 6 :
     print("Wrong value!")
     print("Restart the calculator!")
  

howmanydays = int(input("Please enter the number of days that you will stay :"))

k = (entree + howmanydays) % 7

if k == 0 :
    print("Last day is Sunday")
elif k == 1 :
     print("Last day is Monday")
elif k == 2 :
     print("Last day is Tuesday")
elif k == 3 :
     print("Last day is Wednesday")
elif k == 4 :
     print("Last day is Thursday")
elif k == 5 :
     print("Last day is Friday")
elif k == 6 :
     print("Last day is Saturday")
else :
     print("Wrong value")

a = (entree + howmanydays)
b = int(input("How many people are you?"))

print("Your total is : " , a*b*500 , "USD")



