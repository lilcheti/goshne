
import requests,os,json,sys
    
def send(bot_message):
       bot_token = os.environ.get("TOKEN")
       bot_chatID = os.environ.get("CHATID")
       send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&disable_web_page_preview=true&text=' + bot_message
    
       response = requests.get(send_text)
    
       return response.json()
goh = ""
d = open(str(os.environ.get("CHATID"))+".txt", "r")
ff = str(d.read())
print(ff)
for i in range(int(sys.argv[1])):
    lat = os.environ.get("LAT"+str(i+1))
    long = os.environ.get("LONG"+str(i+1))
    x = requests.get("https://foodparty.zoodfood.com/676858d198d35e7713a47e66ba0755c8/mobile-offers/"+str(lat)+"/"+str(long))
    print(x.text)
    y = json.loads(x.text)
    #print(y["data"]["products"][0]) 
    for ghaza in y["data"]["products"]:
      if ghaza["discountRatio"] > 10:
        print(ghaza["vendorCode"])
        if str(ghaza["productVariationId"]) not in ff:
          send("["+ghaza["title"]+"](https://m.snappfood.ir/selectSideDish/"+str(ghaza["code"])+") %0A"+str(ghaza["price"]-ghaza["discount"]+ghaza["vendorContainerFee"]+int(ghaza["deliveryFee"]))+"%0A"+str(os.environ.get("LOC"+str(i+1)))+"%0A"+"["+ghaza["vendorTitle"]+"](https://m.snappfood.ir/restaurant/"+ghaza["vendorCode"]+")")
        goh += str(ghaza["productVariationId"])+","
g = open(str(os.environ.get("CHATID"))+".txt", "w")
print(goh)
g.write(goh)
g.close()    
    
    
    
    
 
