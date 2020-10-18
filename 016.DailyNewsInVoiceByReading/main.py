from win32com.client import Dispatch 
from newsapi import NewsApiClient
import requests

result = requests.get("http://newsapi.org/v2/top-headlines?country=in&apiKey=31428bd4396942399ba89d032d24a5ed")
result.status_code
# print (result.json())
articles = result.json()
data = articles["articles"]   # collecting only the articles part 

title = [] 
string = ""                    # will 

for ti in data:
    title.append(ti["author"])
    title.append(ti["title"])

for i in title:
    string = string + " from the author "+str(i) +" the news is  "

speak = Dispatch("Sapi.SpVoice")
speak.Speak(string)

