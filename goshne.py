
import requests,os,json

lat = os.environ.get("LAT")
long = os.environ.get("LONG")
    
def send(bot_message):
       bot_token = os.environ.get("TOKEN")
       bot_chatID = os.environ.get("CHATID")
       send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    
       response = requests.get(send_text)
    
       return response.json()
    
x = requests.get("https://foodparty.zoodfood.com/676858d198d35e7713a47e66ba0755c8/mobile-offers/"+str(lat)+"/"+str(long)+"?superType=1")
y = json.loads(x.text)
#print(y["data"]["products"][0]) 
goh = ""
for ghaza in y["data"]["products"]:
  if ghaza["discountRatio"] >= 10:
    print(ghaza["vendorCode"])
    f = open("goh.txt", "r")
    if str(ghaza["productVariationId"]) not in str(f.read()):
      send("["+ghaza["title"]+"](https://snappfood.ir/restaurant/menu/"+ghaza["vendorCode"]+") "+str(ghaza["price"]-ghaza["discount"]))
    goh += str(ghaza["productVariationId"])+","
    
f = open("goh.txt", "w")
f.write(goh)
f.close()    
    
    
    
    
 
