password=input("enter your passord : ")
length=len(password)>=8
upper_case=password !=password.upper()
lower_case=password !=password.lower()
digit=any(char.isdigit() for char in password)

print(f"your password has 8 charcters: {length}\n your password contains uppercase: {upper_case} \n your password contains digit: {digit}")
