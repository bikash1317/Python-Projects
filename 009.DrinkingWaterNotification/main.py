import time 
from plyer import notification

if __name__ == "__main__":
    while(True):

        notification.notify(
            title = "Please Drink Water ",
            message = "Please Drink water now", 
            app_icon = "Iconsmind-Outline-Glass-Water.ico" ,
            timeout = 10 
        )
        time.sleep(60*60)