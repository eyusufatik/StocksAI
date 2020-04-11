import json
import myParser as parser 
import time

fileName = "deneme.json"

stocks = ["YUNSA","EREGL","MAKTK","KRDMD","THYAO","TUPRS","PETKM","ALKIM","ISCTR","GARAN","TCELL","ARCLK","EKGYO","ASELS","HEKTS"]

try:
    while True:
        json_read = open(fileName,"r")
        data = json.load(json_read)
        json_read.close()

        for i in range(0,len(stocks)-2):
            stockName = stocks[i]
            print(stockName)
            currentPrice, table = parser.parse(stockName)
            if currentPrice != -1:
                newParse = {
                    "kademeDeğerleri":table,
                    "stockPrice":currentPrice
                }
                data.get("stocks")[i].get("parses").append(newParse)
        
        json_write = open(fileName,"w")
        json.dump(data,json_write,indent = 4)
        json_write.close()
        time.sleep(900)
        
except KeyboardInterrupt:
    print("User stopped the program.")
    exit()

