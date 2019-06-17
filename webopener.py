import webbrowser
import json
from urllib.request import urlopen
print("lets find an old website.")
website = input("type a url:")
era = input("type a year month and day like 20140613: ")
url = "http://archive.org/wayback/available?url=%s&timestamp=%s" % (website,era)
response = urlopen(url)
contents = response.read()
text = contents.decode("utf-8")
data = json.loads(text)
try:
    old_site = data["archived_snapshots"]["closest"]["url"]
    print("found this copy: ", old_site)
    print("It should appear in your browser now.")
    webbrowser.open(old_site)
except:
    print("Sorry, no luck finding", website)
      
