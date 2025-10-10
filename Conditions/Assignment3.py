# secret_num=6
# guess_name=int(input("enter the number : "))
# if guess_name>secret_num:
#     print(" number is too high")
# elif guess_name<secret_num:
#     print("number is too less")
    
# else:
#     print("you won")
    
    
    
    
secret_num=6
guess_name=int(input("enter the number : "))
if guess_name==7:
    print(" number is near to num")
elif guess_name==5:
    print("your near to num")
elif guess_name<secret_num:
    print("number is too less")
elif guess_name>secret_num:
    print("your is to high")
    
else:
    print("you won")
    