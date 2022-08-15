
import requests,os,json
#session = os.environ.get("TOKEN")
lat = os.environ.get("LAT")
long = os.environ.get("LONG")

x = requests.get("https://foodparty.zoodfood.com/676858d198d35e7713a47e66ba0755c8/mobile-offers/"+str(lat)+"/"+str(long)+"?superType=1")
y = json.loads(x.text)
print(y["data"]["products"][0]) 
