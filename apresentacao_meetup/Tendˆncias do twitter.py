#!/usr/bin/env python
# coding: utf-8

# In[74]:


import json
from twitter import Twitter, OAuth
import pandas as pd
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')


# In[75]:


file = open("access_twitter.json", "r")
access_twitter = json.loads(file.read())

ACCESS_TOKEN = access_twitter["accessToken"]
ACCESS_TOKEN_SECRET = access_twitter["accessTokenSecret"]
CONSUMER_KEY = access_twitter["consumerKey"]
CONSUMER_SECRET = access_twitter["consumerSecret"]


# In[76]:


auth = OAuth(
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET,
    CONSUMER_KEY,
    CONSUMER_SECRET
)
twitter = Twitter(auth = auth)


# In[77]:


results_rio = twitter.trends.place(_id = 455825)
rj_topicos = []
rj = { "tweets":[] }

for location in results_rio:
    trends = location['trends']
    for item in trends:
        if item['tweet_volume']:
            rj_topicos.append(item['name'])
            rj['tweets'].append(item['tweet_volume']) 


# In[78]:


df = pd.DataFrame(rj, index=rj_topicos)
df


# In[79]:


fig=plt.figure(figsize=(18, 13), dpi= 80, facecolor='w', edgecolor='k')
plt.rcParams.update({'font.size': 22})
df["tweets"].plot.barh(title="Tendências no Twitter")

