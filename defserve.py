import random 
while True:
        lower = "abcdefghijklmnopqrstuvwxyz" #alphabet 
        upper = lower.upper()
        number = "0123456789"
        symbol = "()[]{}.,:;-_'"

        total = lower + upper + number + symbol 

        password_length = 9 #Word length

        password = "".join(random.sample(total, password_length))
        print(f"The generated password is: {password}") 