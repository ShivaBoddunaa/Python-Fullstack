temp=float(input("enter the temperature"))
type=input("enter celsius or fahrenheit? (C/F):")
if type == "C":
    fahrenhiet=(temp*9/5)+32
    print("temperature in fahrenheit:",fahrenhiet)
if type=="F":
    Celsius=(temp-32)*5/9
    print("temp in celsius:",Celsius)
elif type !="C" and type !="F":
    print("invalid input please give C or F in type")
    


    