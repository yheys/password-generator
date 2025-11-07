import random
print("Welcome to Password Generator!")
lowercase_letters = [
    'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
]
uppercase_letters = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]
numbers = ['0','1','2','3','4','5','6','7','8','9']

symbols = ['!','@','#','$','%','^','&','*','(',')','_','+','-' ,'|',';',':','/']

print("Your password must have alist one from 'Uppercase letters', 'lowercase letters', 'numbers' , 'symbols'!")
try:
    uppercase=int(input("how many Uppercase latters do you want? '1-26': "))
    lowercase=int(input("how many Lowercase latters do you want? '1-26': "))
    number=int(input("how many numbers  do you want? '1-10': "))
    symbol=int(input("how many symbols  do you want? '1-17':  "))
except ValueError:
    print("invalid error")
    exit()
if uppercase==0 or lowercase==0 or number==0 or symbol==0:
    print("Your password must have alist one from 'Uppercase letters', 'lowercase letters', 'numbers' , 'symbols'!")
    exit()
elif uppercase < 0 or lowercase<0 or number<0 or symbol<0:
    print("Donot enter the negative number!")
elif uppercase > 26 or lowercase> 26 or number> 10 or symbol>17:
    print("This is out of the box!")
    exit()
else:
    if uppercase != 0:
        from_upper=random.choices(uppercase_letters, k=uppercase)

    if lowercase != 0:
        from_lower=random.choices(lowercase_letters, k=lowercase)

    if number != 0:
        from_number=random.choices(numbers, k=number)

    if symbol != 0:
        from_symbol = random.choices(symbols, k=symbol)

    password_list=from_lower + from_upper + from_symbol + from_number
    random.shuffle(password_list)
    password=''.join(password_list)
    print(password)






