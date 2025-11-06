import random
print("Welcome to Password Generator!")
lowercase_letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z'
]
uppercase_letters = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = [
    '!','@','#','$','%','^','&','*','(',')','_','+','-'
    ,'|',';',':','/'
]
print(random.choice(symbols))
length=int(input("Enter password length: "))
uppercase=input("Include uppercase letters? 'yes'/'no' ").lower()
lowercase=input("Include lowercase letters? 'yes'/'no' ").lower()
num=input("Include numbers? 'yes'/'no' ").lower()
symbol=input("Include symbols? 'yes'/'no' ").lower()
password=[ ]


while len(password)<length:
    if uppercase=="yes":
        upper_pass=random.choice(uppercase_letters)
        password.append(upper_pass)
    elif uppercase=="no":
        pass
    else:
        print("Error: You must select at least one character type.")
    if lowercase=="yes":
        lower_pass=random.choice(lowercase_letters)
        password.append(lower_pass)
    elif lowercase == "no":
        pass
    else:
        print("Error: You must select at least one character type.")
    if num=="yes":
        num_pass=random.choice(numbers)
        password.append(num_pass)
    elif num == "no":
        pass
    else:
        print("Error: You must select at least one character type.")
    if symbol=="yes":
        sym_pass=random.choice(symbols)
        password.append(sym_pass)
    elif symbol == "no":
        pass
    else:
        print("Error: You must select at least one character type.")
random.shuffle(password)
str_pass=""
str_pass=str_pass.join(password)
print(str_pass)

