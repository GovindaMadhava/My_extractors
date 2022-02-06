#!/usr/bin/env python
# coding: utf-8

# In[1]:


import wikipedia
import json


# In[2]:


keyword = input("--keyword = ") # taking first input argument from user


# In[3]:


num = input("--num_urls = ")# taking second input argument from user


# In[4]:


x = wikipedia.search(keyword,results = num) # searching for given keyword, upto 'num' number of results


# In[5]:


list=[] # this list will contain all dictionaries
for i in x:
    # defining the structure of the dictionary
    dict ={
        "url" : wikipedia.page(i).url, # using this function to get the url of each page
        "paragraph" : wikipedia.summary(i,sentences = 2) # this function used to obtain summary of each keyword's wiki page
    }
    list.append(dict) # append every dictionary into the list
    # wikipedia.summary() may cause DisambiguationError when a keyword means more than one thing


# In[7]:


for j in range(len(list)):
    print (list[j])
    print ("\n")


# In[8]:


op = input("--output = ") # taking third input argument from user


# In[9]:


json_object = json.dumps(list, indent = 4) # creating a json object
with open(op + ".json", "w") as outfile: # file with given third argument is created with .json extension to store output
    outfile.write(json_object) # the list of dictionaries is written into this newly created json file

