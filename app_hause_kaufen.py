from bs4 import BeautifulSoup
import requests
import lxml
import re
from query import insertquerykaufen
from doc_handler import Doc_handler_kaufen

print("program is running...")

#will take the first index-1 pages
index=2

result = requests.get("https://www.immonet.de/immobiliensuche/sel.do?pageoffset=1&objecttype=1&listsize=26&locationname=Hamburg&acid=&actype=&city=109447&ajaxIsRadiusActive=true&sortby=19&suchart=2&radius=0&pcatmtypes=2_1&pCatMTypeStoragefield=&parentcat=2&marketingtype=1&fromprice=&toprice=&fromarea=&toarea=&fromplotarea=&toplotarea=&fromrooms=&torooms=&objectcat=-1&wbs=-1&fromyear=&toyear=&fulltext=&absenden=Ergebnisse+anzeigen")
src=result.content
soup=BeautifulSoup(src,'lxml')

divs=soup.find_all('div')

tupla=['flex-grow-1', 'display-flex', 'flex-direction-column', 'overflow-hidden']

for div in divs:
    try:
        if div.attrs['class']==tupla:
            spans=div.find_all('span')
            for span in spans:
                if span.attrs['class'][0]=='text-100':
                    result=span.text
                    title = re.sub('\s+', '',result)
                elif span.attrs['class'][0]=='text-250':
                    price = span.text
            divs1=div.find_all('div')
            for div1 in divs1:
                try:
                    a=div1.attrs['id'][0:7]
                    if a[0:7]=='selArea':
                        ps=div1.find_all('p')
                        for p in ps:
                            try:
                                if p.attrs['class'][0]=="text-250":
                                    result=p.text
                                    area=re.sub('\s+', '',result)
                            except:
                                pass                
                except:
                    pass
                
                try:
                    a=div1.attrs['id'][0:8]
                    if a[0:8]=='plotArea':
                        ps=div1.find_all('p')
                        for p in ps:
                            try:
                                if p.attrs['class'][0]=="text-250":
                                    result=p.text
                                    totalarea=re.sub('\s+', '',result)
                            except:
                                pass                
                except:
                    pass
                try:
                    a=div1.attrs['id'][0:8]
                    if a[0:8]=='selRooms':
                        ps=div1.find_all('p')
                        code=div1.attrs['id'][9:100]
                        result2 = requests.get("https://www.immonet.de/angebot/"+str(code))
                        src2=result2.content
                        soup2=BeautifulSoup(src2,'lxml')
                        ls=soup2.find_all('p')
                        dictp=['text-100','pull-left']
                        for l in ls:
                            try:
                                if l.attrs['class']==dictp:
                                    h=l.text
                                    stringformated = re.sub('\s+', '',h)
                                    indexposition = stringformated.find('Hamburg')
                                    postcode = stringformated[indexposition-5:indexposition]
                                                                       
                            except:
                                pass
                        for p in ps:
                            try:
                                if p.attrs['class'][0]=="text-250":
                                    result=p.text
                                    rooms=re.sub('\s+', '',result)
                            except:
                                pass                
                except:
                    pass
            
            #insertquerykaufen(title,price,area,totalarea,rooms,postcode)
            json_results = {title:title,price:price,area:area,totalarea:totalarea,rooms:rooms,postcode:postcode}
            print(json_results)
            Doc_handler_kaufen(json_results)
            
    except:
        pass
