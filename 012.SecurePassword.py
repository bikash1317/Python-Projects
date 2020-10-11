
SECURE = (('s','$') , ('and','&') , ('a','@') , ('o' , '0'),('i','1') , ('0','*') ,('I','|'))

def securePassword(password):
    for a,b in SECURE : 
        password = password.replace(a,b)
    return password
        

userPassword = input("Enter your password : ")
password = (securePassword(userPassword))
print(f'Your sercure password is {password}')