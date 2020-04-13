import json
import myParser as parser 
import time

fileName = "13.04.2020.json"
#fileName = "deneme.json"
stocks = ["HEKTS","YUNSA","EREGL","MAKTK","KRDMD","THYAO","TUPRS","PETKM","ALKIM","ISCTR","GARAN","TCELL","ASELS","ARCLK","EKGYO"]

#lastValues = [[[]]]*15
try:
    while True:
        json_read = open(fileName,"r")
        data = json.load(json_read)
        json_read.close()

        for i in range(0,len(stocks)):
            stockName = stocks[i]
            print(stockName,end=" ",)
            currentPrice, table = parser.parse(stockName)
            if currentPrice != -1: #and lastValues[i] != table:
                #print("new reading detected")
                #lastValues[i]=table
                newParse = {
                    "kademeDeğerleri":table,
                    "stockPrice":currentPrice
                }
                data.get("stocks")[i].get("parses").append(newParse)
            if currentPrice == -1:
                errNo = data["stocks"][i]["errors"]
                data["stocks"][i]["errors"] = errNo+1
        json_write = open(fileName,"w")
        json.dump(data,json_write,indent = 4)
        json_write.close()
        print("===========================================================")
        time.sleep(30)
        
except KeyboardInterrupt:
    print("User stopped the program.")
    exit()

