
import requests,os,json
    
def send(bot_message):
       bot_token = os.environ.get("TOKEN")
       bot_chatID = os.environ.get("CHATID")
       send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&disable_web_page_preview=true&text=' + bot_message
    
       response = requests.get(send_text)
    
       return response.json()
goh = ""
for i in range(3):
    send(str(os.environ.get("LOC"+str(i+1))))
    lat = os.environ.get("LAT"+str(i+1))
    long = os.environ.get("LONG"+str(i+1))
    x = requests.get("https://foodparty.zoodfood.com/676858d198d35e7713a47e66ba0755c8/mobile-offers/"+str(lat)+"/"+str(long)+"?superType=1")
    y = json.loads(x.text)
    #print(y["data"]["products"][0]) 
    for ghaza in y["data"]["products"]:
      if ghaza["discountRatio"] >= 40:
        print(ghaza["vendorCode"])
        f = open("goh.txt", "r")
        if str(ghaza["productVariationId"]) not in str(f.read()):
          send("["+ghaza["title"]+"](https://m.snappfood.ir/selectSideDish/"+str(ghaza["productVariationId"])+") "+str(ghaza["price"]-ghaza["discount"]+ghaza["vendorContainerFee"]+int(ghaza["deliveryFee"])))
        goh += str(ghaza["productVariationId"])+","
    
f = open("goh.txt", "w")
f.write(goh)
f.close()    
    
    
    
    
 
