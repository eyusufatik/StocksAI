import requests
from bs4 import BeautifulSoup

errorCounter = 0

def parse(stockName):
    global errorCounter
    page = requests.get("http://graph.foreks.com/grafik/webfx/line3djson.jsp?hisse="+stockName)
    print(page.status_code)

    if page.status_code == 200:
        currentVal=-1
        table = []
        try:
            soup = BeautifulSoup(page.content, 'html.parser')
            currentVal = float(soup.findAll("td", {"style" : "color:#ff0000"})[0].get_text().replace(",","."))
            data = soup.find_all("tr")
            data = data[1:len(data)]
            table = []
            for item in data:
                values = item.get_text().split('\n')
                values = [values[1],values[3]]
                values = [i.replace(",",".") for i in values]
                values = [i.replace("%","") for i in values]
                values = [float(i) for i in values[0:2]]
                table.append(values)
        except Exception as e:
            print("something happened returning empty data for this parsing: "+ str(e))
        return currentVal,table
        
    else:
        errorCounter+=1
        print(errorCounter)
        if errorCounter == 2:
            errorCounter = 0
            return -1,-1
        else:
            return parse(stockName)
