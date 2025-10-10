amount=int(input("enter the tota amount : "))
if amount==1000:
    print(f"you have unlock 10% discount")
    print(f"your final bill is {(amount-amount*10/100)}")
elif amount>=500:
    print(f"you have unlock 5% discount")
    print(f"your final bill is {(amount-amount*5/100)}")
elif amount<=499:
    print(f"Sorry we dont have any Discounts On this Price")
    print(f"your final bill is {amount}")