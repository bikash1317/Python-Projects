print(''' ********** Welcome To The Store ********** 
'q' --          To Quit The store
Any number --   To Add that number and print the receipt ''')

TotalAmount = 0.0
amount = 0
while(True):
    amount = (input("Enter the number to be inputed or press 'q' to Quit "))
    if(amount=='q'):
        print("Thanks For using our calculator")
        print(f'Your Amount to be Paid is {TotalAmount}')
        exit()
    else:
        try:
            TotalAmount = TotalAmount+float(amount)
            print(f"Order Total So Far = {TotalAmount}")
        except Exception as e :
            print ("Try again Invalid Input")

    
    
    