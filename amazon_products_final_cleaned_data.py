# -*- coding: utf-8 -*-
"""Untitled12.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tgleZiGYi23Tocm7mBenLe8-1X4U2X3d
"""

import pandas as pd

df=pd.read_csv('/content/amazon_product.csv')
df.head()



"""📦 Dataset Overview:
The dataset consists of Amazon product listings, and contains structured information about a variety of products available on the platform. With a shape of (N rows, M columns) (the exact numbers can be updated if needed), each row represents a unique product and the columns describe different attributes such as product ID, name, brand, price, rating, reviews, availability, and more. This dataset is useful for product analysis, consumer behavior modeling, and recommendation system development.

🧱 Column Structure and Data Types:
The dataset includes several important columns like product_name, brand, price, rating, reviews, and possibly category. Most columns are of object (string) type, especially for categorical fields like brand and product names. Numeric columns like price, rating, and reviews are either floats or integers. This mix of categorical and numerical data makes the dataset suitable for both statistical analysis and machine learning models.
"""



"""Column Descriptions

 1- asin: Amazon Standard Identification Number, a unique identifier for each product.

2- product_title: The name or title of the product.

3- product_price: The current price of the product.

4- product_original_price: The original price of the product before any discounts.

5- currency: The currency in which the product price is listed.

6- product_star_rating: The average star rating of the product.

7- product_num_ratings: The number of ratings the product has received.

8- product_url: The URL to the product’s Amazon page.

9- product_photo: A link to the product’s photo.

10- product_num_offers: The number of different offers available for the product.

11- product_minimum_offer_price: The minimum price of the offers available.

12- is_best_seller: Indicator if the product is a best seller.

13- is_amazon_choice: Indicator if the product is an Amazon's Choice product.

14- is_prime: Indicator if the product is eligible for Amazon Prime.

15- climate_pledge_friendly: Indicator if the product is labeled as Climate Pledge Friendly.

16- sales_volume: The volume of sales for the product.

17- delivery: Information about the delivery options for the product.

18- has_variations: Indicator if the product has variations (e.g., different sizes or colors).

19- product_availability: The availability status of the product.

20- unit_price: The price per unit of measure.

21- unit_count: The number of units included in the product price.
"""



### Issues with the data

 # Dirty Data (quality issues):

1- unnamed column has no use
2-product title names is okay , they have to be in proper format (`consistancy`)
3-asin have some invalid codes (`validity`)
4-product original price have some null values(`completeness`)
5- product star rating have null values (`completeness`)
6-product url and product photo is not needed , but can be used to get the invalid asin codes
7-sales volume have null  (`completeness`)
8- sales volume have some invalid inputs  (`validity`)
9- product availability , unit price , unit count have mostly null values (`completeness`)
10 - product price and product original price have to be in float ('consistancy')

# messy data

1- sales volume numer format needs to be changed  (`consistancy`)
2- delivery column needs to be fixed (`consistancy`)
3-

"""Note - Assessing Data is an Iterative Process

## Data Quality Dimensions

Completeness -> is data missing?

Validity -> is data invalid -> negative height -> duplicate patient id

Accuracy -> data is valid but not accurate -> weight -> 1kg

Consistency -> both valid and accurate but written differently -> New Youk and NY

##Order of severity

Completeness <- Validity <- Accuracy <- Consistency

## Data Cleaning Order

Quality -> Completeness

Tidiness

Quality -> Validity

Quality -> Accuracy

Quality -> Consistency

Steps involved in Data cleaning
Define
Code
Test
"""

df.head()

df['product_title'].head()

df1=df.copy()

df3=pd.read_csv('/content/amazon_product.csv')

df3.head()

#df.drop('Unnamed: 0',axis=1,inplace=True)
df.head()







df['product_original_price']=round(df['product_original_price'],2)

df['product_original_price']

df['product_price']=df['product_price'].str.replace('$',' ').astype('float')

df['product_original_price']=df['product_original_price'].str.replace('$',' ').astype('float')

df.loc[np.isinf(df['product_original_price']), 'product_original_price'] = (
    df['product_price'] * 1.345166835654483
)

df.head()

import numpy as np
df[(df['product_price']>0) & (df['product_price']<1)]
#df['product_price'].replace(0,np.nan,inplace=True)

print(df['product_price'].isna().sum(), (df['product_price'] == 0).sum())

import numpy as np

# Filter out invalid rows
valid_rows = df[
    (df['product_price'] > 0) &
    (~df['product_price'].isna()) &
    (~df['product_original_price'].isna()) &
    (df['product_original_price']>0) &
    (~np.isinf(df['product_price'])) &
    (~np.isinf(df['product_original_price']))
]

# Calculate discount ratio (original / actual) and take the mean
discount_ratio = (
    valid_rows['product_original_price'] /
    valid_rows['product_price']
).mean()

print(discount_ratio)

df[df['product_original_price'].isnull()]

df[df['product_price'].isnull()]

df['product_original_price']=df['product_original_price'].fillna(0)
df['product_price']=df['product_price'].fillna(0)

df.head()

df[df['product_star_rating'].isnull()]

#df.drop('product_photo',axis=1,inplace=True)
df.drop('product_url',axis=1,inplace=True)

df.head()



df['product_minimum_offer_price']=df['product_minimum_offer_price'].str.replace('$',' ').astype('float')

df['sales_volume']=df['sales_volume'].str.split('+').str[0].str.replace('K',' ')

df['sales_volume']=df['sales_volume']*1000

df2['sales_volume']=df['sales_volume']

df2['sales_volume']

df['sales_volume'] = df3['sales_volume']



print(len(df), len(df2))

df['sales_volume'].astype(int)

df



def convert_to_numeric_or_nan(value):
    try:
        return pd.to_numeric(value)
    except ValueError:
        return np.nan

df['sales_volume']=df['sales_volume'].apply(convert_to_numeric_or_nan)



df.info()

df['sales_volume']=df['sales_volume']*1000

df['sales_volume']

import pandas as p
import seaborn as sns
import matplotlib.pyplot as plt
sns.kdeplot(df['sales_volume'])
plt.show()

#df['sales_volume'].replace(0,df['sales_volume'].median)

median=df['sales_volume'].median()

df['sales_volume'].fillna(median,inplace=True)

df['sales_volume'].info()

df.head(2)









#df.drop('unit_count',axis=1,inplace=True)

# --- 2. Split the column ---

# Split by 'FREE delivery ' and get the parts
# n=1 ensures it splits only at the first occurrence
# expand=True creates new columns from the split parts
split_parts = df['delivery'].str.split('FREE delivery', n=1, expand=True)

# Assign to new columns
# Part 1: Text before 'FREE delivery'
df['text_before_free_delivery'] = split_parts[0].str.strip()

# Part 2: 'FREE delivery' phrase itself
# Use np.where to assign 'FREE delivery' only if split_parts[1] is not NaN (meaning 'FREE delivery' was found)
df['free_delivery_phrase'] = np.where(split_parts[1].notna(), 'FREE delivery', pd.NA)

# Part 3: Text after 'FREE delivery'
df['text_after_free_delivery'] = split_parts[1].str.strip() # .str.strip() for cleanliness

#print("\nDataFrame after splitting:")
#print(df[['your_text_column', 'text_before_free_delivery', 'free_delivery_phrase', 'text_after_free_delivery']])

df

df.rename(columns={
    'text_before_free_delivery': 'Instantly Avilable',
    'free_delivery_phrase': 'FREE Delivery',
    'text_after_free_delivery':'delivery date info'
}, inplace=True)

df.head(10)

df['free_delivery_phrase'].unique()

df['text_before_free_delivery'].unique()

df['text_after_free_delivery'].unique()

df['Instantly Avilable'] = df['Instantly Avilable'].isin([
    'Available instantly',
    'Available instantly on compatible devices'
])

df['FREE Delivery'] = df['FREE Delivery'].isin([
    'FREE delivery'])

#df.drop('delivery date info',axis=1,inplace=True)
#df.drop('delivery_date',axis=1,inplace=True)

df.rename(columns={'raw_extracted':'delivery date'}, inplace=True)

df

df.drop('delivery',axis=1,inplace=True)

df.info()

import pandas as pd
import numpy as np
import re
from datetime import datetime

def extract_delivery_info(text):
    if pd.isnull(text) or text.strip() == '':
        return pd.Series([None, None, None])

    # Pattern to match e.g., "Tue, Aug 6" or "Fri, Sep 20"
    match = re.search(r'\b(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun),?\s+\w+\s+\d{1,2}', text)

    # Fallback: "August 13, 2024" style (release info)
    fallback_match = re.search(r'\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}', text)

    try:
        if match:
            raw_date = match.group()
            parsed_date = datetime.strptime(raw_date.replace(',', ''), "%a %b %d")
            # Default year assumption (set to current year)
            parsed_date = parsed_date.replace(year=datetime.now().year)
        elif fallback_match:
            raw_date = fallback_match.group()
            parsed_date = datetime.strptime(raw_date, "%B %d, %Y")
        else:
            return pd.Series([None, None, None])

        return pd.Series([
            parsed_date.strftime("%A"),       # Day name (e.g., Tuesday)
            parsed_date.strftime("%Y-%m-%d"), # ISO format date
            raw_date                          # Raw extracted string
        ])

    except Exception as e:
        return pd.Series([None, None, None])

# Example usage on a DataFrame
# df['text_before_free_delivery'] = ...  # Your actual column
df[['delivery_day', 'delivery_date', 'raw_extracted']] = df['delivery date info'].apply(extract_delivery_info)

df['delivery date'].isnull().sum()