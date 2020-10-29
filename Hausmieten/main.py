
from bs4 import BeautifulSoup
import requests
import lxml
import doc_handler
import re

print("program is running...")

#will take the first index-1 pages
index=2

result = requests.get("https://www.immonet.de/immobiliensuche/sel.do?suchart=2&torooms=8.0&city=109447&marketingtype=2&pageoffset=27&radius=0&parentcat=2&listsize=27&sortby=0&objecttype=1&page=3")
src=result.content
soup = BeautifulSoup(src,'lxml')

divs = soup.find_all('div')
for div in divs:
    try:
        if div.attrs['class'] == ['flex-grow-1','display-flex','flex-direction-column','box-25','overflow-hidden','cursor-hand']:
            title = 'not found'
            price = 'not found'
            area = 'not found'
            totalarea = 'not found'
            rooms = 'not found'
            location = 'not found'
            
            tagas = div.find_all('a')
            for taga in tagas:
                value = taga.attrs['id'][13:100]
               
                if taga.attrs['id'] == 'lnkToDetails_'+value:
                    title = re.sub('\s+','',taga.text)
       
            
            divs2 = div.find_all('div')
            for div2 in divs2:
                try:                      
                    if div2.attrs['id'] == 'selPrice_'+value:                 
                        price = re.sub('\s+','',div2.text)[12:17]
                        # print(price)
                    elif div2.attrs['id'] == 'selArea_'+value:
                        area = re.sub('\s+','',div2.text)[13:18]
                        # print(area)
                    elif div2.attrs['id'] == 'plotArea_'+value:
                        totalarea = re.sub('\s+','',div2.text)[13:18]
                    elif div2.attrs['id'] == 'selRooms_'+value:
                        rooms = re.sub('\s+','',div2.text)[3:100]
                except:
                    pass
        
            result2 = requests.get('https://www.immonet.de/angebot/'+value+'?drop=sel&related=false&product=standard')
            src2=result2.content
            soup2 = BeautifulSoup(src2,'lxml')
            ps = soup2.find_all('p')
                               
            for p in ps:
                
                try:
                    if p.attrs['class'] == ['text-100', 'pull-left']:
                        location = re.sub('\s+','',p.text)
                except:
                    pass

            
 

            dictmieten = {'title':title,'price':price,'area':area,'totalarea':totalarea,'rooms':rooms, 'location':location}
            print(dictmieten)
                
    except:
        pass


    
  
                

