with open('CurrencyData.txt') as f:
    lines = f.readlines()


choice = int(input(
    'To convert indian currency to any other press 1 else press anything : '))
if(choice == 1):
    dictionary = {}
    for line in lines:
        currency = line.split("\t")
        # This has the values of 1 IndianRupee = ? other currency
        dictionary[currency[0]] = currency[1]

    amount = float(input("Enter the amount : "))
    print(''' Enter the name of the currency you want to convert into Available Options \n  ''')
    # print(dictionary.keys())  ==--  It is not the best way to print the files
    # this is called dictionary comprehension
    [print(line) for line in dictionary.keys()]

    currency = input("Please Enter one of these values : \n1 ")
    print(
        f'{amount} in INR is = {amount * float(dictionary[currency])} in currency {currency}')

else:
    dictionary = {}
    for line in lines:
        currency = line.split("\t")
        # This has the values of 1 IndianRupee = ? other currency
        dictionary[currency[0]] = currency[2]
    amount = float(input("Enter the amount : "))
    print(''' Enter the name of the currency you want to convert into Available Options \n  ''')
    # print(dictionary.keys())  ==--  It is not the best way to print the files
    # this is called dictionary comprehension
    [print(line) for line in dictionary.keys()]

    currency = input("Please Enter one of these values : \n1 ")
    print(
        f'{amount}  in {currency} is = {amount * float(dictionary[currency])} in INR ')
