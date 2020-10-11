import pandas as pd
import datetime


def sendEmail():
    pass




if __name__ == "__main__":
    df = pd.read_excel("Data.ods")
    # print(df)
    # completeToday= datetime.datetime.now()  # To show the complete date
    # print("The Complete Format of the date is = ",completeToday)
    today= datetime.datetime.now().strftime("%d-%m")  # To show only day and month 
    # print ("Showing only date and month = ",today)

    for index , item in df.iterrows():
        # print(index , item["Birthday"])
        bday = item["Birthday"].strftime("%d-%m")
        print(bday)