# H&M Website Data Crawling
import requests as re
import pandas as pd
import json
offset = 0
data = []
while True:
    url = f"https://www2.hm.com/en_us/men/new-arrivals/view-all/_jcr_content/main/productlisting.display.json?sort=stock&image-size=small&image=model&offset={
        offset}&page-size=36"
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    res = re.get(url, headers=headers)
    response = res.json()
    product_len = len(response["products"])
    if product_len != 0:
        for i in range(product_len):
            try:
                title_ = response["products"][i]["title"]
            except:
                title_ = "Not Available"
            try:
                category_ = response["products"][i]["category"]
            except:
                category_ = "Not Available"
            try:
                damStyleWith_ = response["products"][i]["damStyleWith"]
            except:
                damStyleWith_ = "Not Available"
            try:
                percentageDiscount_ = response["products"][i]["percentageDiscount"]
            except:
                percentageDiscount_ = "Not Available"
            try:
                price_ = response["products"][i]["price"]
            except:
                price_ = "Not Available"
            try:
                redPrice_ = response["products"][i]["redPrice"]
            except:
                redPrice_ = "Not Available"
            try:
                sellingAttribute_ = response["products"][i]["sellingAttribute"]
            except:
                sellingAttribute_ = "Not Available"
            try:
                swatchesTotal_ = response["products"][i]["swatchesTotal"]
            except:
                swatchesTotal_ = "Not Available"
            dict_data = {
                "title": title_,
                "category": category_,
                "damStyleWith": damStyleWith_,
                "percentageDiscount": percentageDiscount_,
                "price": price_,
                "redPrice": redPrice_,
                "sellingAttribute": sellingAttribute_,
                "swatchesTotal": swatchesTotal_
            }
            data.append(dict_data)
            # print(dict_data)
    else:
        break
    offset += 36
# print(len(data))
df = pd.DataFrame(data)
df.to_csv("H&M Website Men's Category Data Extraction", index=True)
