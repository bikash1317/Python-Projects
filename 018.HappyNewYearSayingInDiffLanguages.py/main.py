from win32com.client import Dispatch

def speak(str):
    speak=Dispatch(("SAPI.SPVoice"))
    speak.Speak(str)

if __name__ == "__main__":
    with open("happyNewYear.txt") as f:
        for item in f.readlines():
            speak(item)
