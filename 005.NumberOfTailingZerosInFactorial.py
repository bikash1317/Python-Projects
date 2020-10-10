

while(True):
    print("Enter the Number And see the Tailing Zeros in it or 'q' to qiut : ")
    choice = (input(''))
    if(choice != 'q'):
        try:
            i = 5
            countZeros = 0
            while(int(choice) >= i):
                countZeros = countZeros + int((int(choice)/i))
                i = i * 5
            print(f'The Number of tailing Zeros are = {countZeros}')
        except Exception as e:
            print("Wrong Input Try again")

    else:
        print("Thanks for coming see you soon")
        exit()
