# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 22:05:39 2019

@author: erand
"""

import praw
import pandas as pd
import redcreds as creds
from nltk import word_tokenize, pos_tag_sents
import collections

r = praw.Reddit(username = creds.username,            
password = creds.password,            
client_id = creds.client_id,            
client_secret = creds.client_secret,            
user_agent = creds.user_agent) 

submissions = r.subreddit('blackcats').top("all", limit=1000)

subs = []
for sub in submissions:
        subs.append({'Titles': sub.title})
    
subs=pd.DataFrame(subs)
titles = subs['Titles'].tolist()
taggedTitles = pos_tag_sents(map(word_tokenize, titles))

properNouns = []

for title in taggedTitles:
    for word,pos in title:
        if pos=='NNP':
            properNouns.append(word)
            
nameCount = collections.Counter(properNouns)
print(nameCount.most_common(40))


