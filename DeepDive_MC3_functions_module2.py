#!/usr/bin/env python
# coding: utf-8

# In[5]:


import requests
import pandas as pd


# In[2]:


url = 'https://globalmart-api.onrender.com/mentorskool/v1/sales'
headers = {
    'accept': 'application/json',
    'access_token': 'fe66583bfe5185048c66571293e0d358'
}
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Check for any HTTP errors
    data = response.json()
    # Process and work with the data here
    print(data)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    
# Fetch 500 records

url = 'https://globalmart-api.onrender.com/mentorskool/v1/sales'
headers = {
    'accept': 'application/json',
    'access_token': 'fe66583bfe5185048c66571293e0d358'
}
pages = []
for offset in range(1, 500, 100):
    parameters = {
        'limit': 100,
        'offset': offset
    }
    response = requests.get(url, headers=headers, params=parameters)
    data = response.json()
    pages.extend(data['data'])
main_dict = {'records': pages}


# In[10]:


def api_call(url,token):
    
    headers = {
        'accept': 'application/json',
        'access_token': token
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Check for any HTTP errors
        data = response.json()
        # Process and work with the data here
        print(data)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

    # Fetch 500 records

    headers = {
        'accept': 'application/json',
        'access_token': token
    }
    pages = []
    for offset in range(1, 500, 100):
        parameters = {
            'limit': 100,
            'offset': offset
        }
        response = requests.get(url, headers=headers, params=parameters)
        data = response.json()
        pages.extend(data['data'])
    main_dict = {'records': pages}
    return main_dict


# In[13]:


url = 'https://globalmart-api.onrender.com/mentorskool/v1/sales'
token = 'fe66583bfe5185048c66571293e0d358'
x = api_call(url,token)


# In[14]:


json_data = x['records']
df_json = pd.json_normalize(json_data)
df_json.head()


# In[15]:


df_json['product.sizes']


# In[16]:


new = df_json['product.sizes'].str.split(",", expand = True)
new


# In[17]:


new[55].notnull()


# In[18]:


new[new[[55]].notnull().all(1)]


# In[19]:


df_json.iloc[114]


# In[23]:


def search_product(product_name,df = df_json):
    for i in range(0,len(df_json)):
        if (df_json['product.product_name'][i] == product_name):
            print(i)


# In[24]:


search_product("Mitel 5320 IP Phone VoIP phone")


# In[43]:


df_json.iloc[7]


# In[45]:


df_json['order.order_purchase_date'] = pd.to_datetime(df_json['order.order_purchase_date'])


# In[49]:


df_json['month'] = pd.DatetimeIndex(df_json['order.order_purchase_date']).month
df_json


# In[ ]:


new_df = df_json[]

