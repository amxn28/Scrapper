import requests
from bs4 import BeautifulSoup
import pandas as pd
import random 

reviewlist = []

def getRandomProxy():
    #using proxy - add your proxy details if needed
    proxy = {
        "http": None,  # Replace None with your proxy if available
        "https": None  # Replace None with your proxy if available
    }
    return proxy 

def extractReviews(reviewUrl):
    try:
        resp = requests.get(reviewUrl, proxies=getRandomProxy())    
        soup = BeautifulSoup(resp.text, 'html.parser')
        reviews = soup.findAll('div', {'data-hook': 'review'})
        for item in reviews:
            review_body = item.find('span', {'data-hook': 'review-body'}).text.strip()
            reviewlist.append(review_body)
    except Exception as e:
        print(f"Error extracting reviews: {e}")

def totalpages(reviewurl):
    try:
        resp = requests.get(reviewurl, proxies=getRandomProxy())
        soup = BeautifulSoup(resp.text, 'html.parser')
        reviews = soup.find('div', {'data-hook': "cr-filter-info-review-rating-count"})
        if reviews:
            review_text = reviews.text.strip()
            total_reviews = int(review_text.split(",")[1].split(" ")[0].replace(",", ""))
            return 1 + total_reviews // 10
        return 1
    except Exception as e:
        print(f"Error getting total pages: {e}")
        return 1

# Set your product URL here
productUrl = "YOUR_AMAZON_PRODUCT_URL_HERE"
reviewUrl = productUrl.replace("dp", "product-reviews") + "?pagenumber=1"

npages = totalpages(reviewUrl)
print(f"Running for {npages} pages")

for i in range(npages):
    try:
        print(f"Running for page {i+1}")
        reviewUrl = productUrl.replace("dp", "product-reviews") + f"?pagenumber={i+1}"
        extractReviews(reviewUrl)
    except Exception as e:
        print(f"Error on page {i+1}: {e}")

# Create DataFrame with just review bodies
df = pd.DataFrame(reviewlist, columns=['Review Body'])

# Save to CSV
df.to_csv("reviews.csv", index=False)
print("Reviews saved to reviews.csv")
