import requests
import lxml.html as lh
import pandas as pd

url = 'http://www.formula1-dictionary.net/drivers_all_time_list.html'

page = requests.get(url)

doc = lh.fromstring(page.content)

tr_elements = doc.xpath('//tr')

col=[]
i=0
for t in tr_elements[0]:
  i=i+1
  col_name = t.text_content()
  #print(i,col_name)
  col.append((col_name,[]))

for j in range(1,len(tr_elements)):
   
    T=tr_elements[j]
    
   
    if len(T)!=5:
        break
    
    
    i=0
    
    
    for t in T.iterchildren():
        data=t.text_content() 
        
        if i>0:
        
            try:
                data=int(data)
            except:
                pass
        
        col[i][1].append(data)
       
        i+=1
Dict={title:column for (title,column) in col}
df=pd.DataFrame(Dict)
df.head()