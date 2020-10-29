
from bs4 import BeautifulSoup
import requests
import lxml
import doc_handler
import re

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
                                    postcode=re.sub('\s+', '',h)[0:5]
                                    print(postcode)                                    
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



            dic_results={'title':title,'price':price,'area':area,'totalarea':totalarea,'rooms':rooms,'postcode':postcode}
            print(dic_results)
    except:
        pass

 
                     
            
















    #         divs_1=div.find_all(div)
    #         for div_1 in divs_1:
    #             try:
    #                 if div_1.attrs['class'][0]=="box-25":
    #                     print(1)
    #             except:
    #                 pass
    # except:
    #     pass
# spans=soup.find_all('span')
# ps=soup.find_all('p')

# for span in spans:
#     try:
#         if span.attrs['class'][0]=="text-100":
#             title=span.text
#         if 





    #         divs_1=soup.find_all('span')
    #         for div_1 in divs_1:
    #             if div_1.attrs['class'][0]=='box-25':
    #                 # print(span)
    #                 try:
    #                     title=(div_1.text)
    #                     print(title)
    #                 except:
    #                     pass
    # except: pass




#         pass
#  tags_a=li.find_all('a')
#                 tags_h3=li.find_all('h3')
#                 tags_spans=li.find_all('span')
#                 for a in tags_a:
#                     try:
#                         if a.attrs['class'][0]=='s-item__link':
#                             link=a.attrs['href']
#                     except:
#                         link='NOTFOUND'
#                         pass
#                 for h3 in tags_h3:
#                     try:
#                         if h3.attrs['class'][0]=='s-item__title':
#                             title=h3.text.replace(",","")
#                     except:
#                         title='NOTFOUND'
#                         pass
#                 for span in tags_spans:
#                     try:
#                         if span.attrs['class'][0]=='s-item__price':
#                             price=span.text
#                     except:
#                         price='NOTFOUND'
#                         pass
#                 for span in tags_spans:
#                     try:
#                         if span.attrs['class'][0]=='s-item__location':
#                             location=span.text
#                     except:
#                         location='NOTFOUND'
#                         pass
#                 for span in tags_spans:
#                     try:
#                         if span.attrs['class'][0]=='s-item__hotness':
#                             sales=span.text
#                     except:
#                         sales='NOTFOUND'
#                         pass
#                 for span in tags_spans:
#                     try:
#                         if span.attrs['class'][0]=='s-item__shipping':
#                             delivery=span.text
#                     except:
#                         delivery='NOTFOUND'
#                         pass
#                 try:
#                     dict_item={
#                         'page':x+1,
#                         'record':record,
#                         'li':li.attrs['data-view'],
#                         'title':title,'price':price,
#                         'location':location,
#                         'sales':sales,
#                         'delivery':delivery,
#                         'link':link
#                         }
#                     doc_handler.Doc_handler(dict_item)
#                     record=record+1        
#                 except:
#                     pass
#         except:
#             pass

# print('program have ended')

