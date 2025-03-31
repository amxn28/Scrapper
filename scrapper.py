import requests
from bs4 import BeautifulSoup
import pandas as pd
import random 

reviewlist=[]
def getRandomProxy():
    #using proxy
    proxy = {
        "http": 
        "https":
    }
    return proxy 
    #resp = requests.get("")
    #print(resp.text)

def extractReviews(reviewUrl, pg):
    resp= requests.get(reviewUrl, proxies=getRandomProxy())    
    soup = BeautifulSoup(resp.text, 'html.parser')
    reviews = soup.findAll('div',{'data-hook': 'review'})
    for item in reviews:
        review ={
            'productTitle': soup.title.text.replace("Amazon.in:Customer Reviews: ", ""),
            'Review Title' : item.find('a', {'data-hook':'review-title'}).text.strip(),
            'Rating' : item.find('i', {'data-hook':'review-star-rating'}).text.strip(), 
            'Review Body' : item.find('span', {'data-hook':'review-body'}).text.strip(),


        }
        reviewlist.append(review)
def totalpages(reviewurl):
    resp=requests.get(reviewurl, proxies=getRandomProxy())
    soup= BeautifulSoup(resp.text, 'html.parser')
    review =soup.find('div', {'data-hook' : "cr-filter-info-review-rating-count"})
    return 1+ int(reviews.text.strip().split(",")[1].split(" ")[0]).replace(",","" )//10

reviewlist = []    
getRandomProxy()

pg = 1
productUrl = 
reviewUrl = productUrl.replace("dp","product-reviews") +  f"?pagenumber={pg}"
npages= totalpages(reviewurl)
print(f"Running for {npages} pages")

for i in range(npages):
    try:
        print(f"Running for page {i+1}")
        reviewUrl = reviewUrl = productUrl.replace("dp","product-reviews") +  f"?pagenumber={i+1}"
        extractReviews(reviewUrl.pg)
    except Exception as e:
        print(e)
    

df=pd.DataFrame(reviewlist)
df.to_excel("output.xlsx", index=False)