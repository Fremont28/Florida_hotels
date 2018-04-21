#extract the average hotel review score and descriptions from booking.com 
#4/20/18 
from bs4 import BeautifulSoup
import requests
import re
import string 

l=[]
for p in range(0,5): 
    p=p+1
    base_url='https://www.booking.com/searchresults.html?label=gen173nr-1FCAEoggJCAlhYSDNYBHIFdXNfcGGIAQGYATG4AQfIAQzYAQHoAQH4AQKSAgF5qAID;sid=3758ab4bd122c4a08f5f71bd4644af1d;city=20023488;from_idr=1&;ilp=1;d_dcp=1'+str(p)
r=requests.get(base_url)
soup=BeautifulSoup(r.text,"html.parser")
all_score=soup.find_all('span', class_="review-score-badge")

#extracts room descriptions
soup.find_all('p')[0].get_text()
l=[] 
for i in soup:
    l.append(soup.find_all(class_='hotel_desc'))
string_desc=''.join(str(e) for e in l) 
#remove words from the string
string_desc1=string_desc.replace('\n</div>','')
string_desc1=string_desc.replace('<div class=','')
string_desc1=string_desc.replace('\n</div>','')
string_desc1=string_desc.replace('class="hotel_desc">\n','')
string_desc1=string_desc.replace('div','')

#split words 
words1=re.split(r'\W+',string_desc1) 
len(words1) 
#split whitespace and remove punctuation
print(string.punctuation)
table=str.maketrans('','',string.punctuation)
stripped=[w.translate(table) for w in words1] 
#convert to lowercase 
words_lower=[word.lower() for word in stripped] 

#i.word counts
wordcount=dict((x,0) for x in stemmed) 
for i in stemmed:
    if i in wordcount:
        wordcount[i]+=1
type(wordcount) #class dict 

#convert dict to dataframe 
wordcount_df=pd.DataFrame(list(wordcount.items()),columns=['one','two'])

#ii. hotel review scores 
l1=[]
for i in soup:
    l1.append(soup.find_all(class_="review-score-badge"))

#convert list to string 
string1=''.join(str(e) for e in l1)
string2=re.sub('[^0-9]','',string1) 
#split the string after every 2nd character 
def split_n(seq,n):
    while seq:
        yield seq[:n]
        seq=seq[n:]
final_scores=(list(split_n(string2,2)))

#convert list to dataframe 
new_df1=pd.DataFrame({'score':final_scores}) 
#convert non-null to integer?
new_df2=new_df1['score'].astype(str).astype(int)
new_df2.mean() #85.36 (average hotel score in orlando) #repeat with other cities 