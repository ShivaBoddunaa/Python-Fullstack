user=input("enter the input")
# user="shivaaa"
vowels=user.count("a")
vowels1=user.count("e")
vowels2=user.count("i")
vowels3=user.count("o")
vowels4=user.count("u")
total_vowels=vowels+vowels1+vowels2+vowels3+vowels4
total_letters=len(user)
total_consonents=total_letters-total_vowels
print(f"vowels present: {total_vowels}")
print(f"consonents present: {total_consonents}")