from win32com.client import Dispatch 
speak = Dispatch("Sapi.SpVoice")
speak.Speak("Bikash Is a good boy .")