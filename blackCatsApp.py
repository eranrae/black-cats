# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 22:05:39 2019

@author: erand
"""

import praw
import pandas as pd
import redcreds as creds

r = praw.Reddit(username = creds.username,            
password = creds.password,            
client_id = creds.client_id,            
client_secret = creds.client_secret,            
user_agent = creds.user_agent) 

submissions = r.subreddit('blackcats').top("day", limit=100)

subs=[]
for sub in submissions:
        subs.append({'Titles': sub.title})
    
pd.DataFrame(subs)


