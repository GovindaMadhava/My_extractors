#!/usr/bin/env python
# coding: utf-8

# In[1]:


import PyPDF2
import urllib.request
from urllib.request import urlopen
from urllib.request import urlretrieve
import csv
import json
import requests
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup


# In[2]:


def download_file(download_url):
    response = urllib2.urlopen(download_url)
    file = open(download_url, 'wb')
    file.write(response.read())
    file.close()


# In[ ]:


list=[]
dict ={
        "page-url" : row[0], # row[0] is the url of the page / pdf document
        "pdf-url" : ,
        "paragraph" : 
}


# In[ ]:


with open('data.csv', 'wb') as obj:
    csv_reader = csv.reader(obj)
    for row in csv_reader:
        webUrl  = urllib.request.urlopen(row)
        data = webUrl.read()
        list.append(row)


# In[12]:


json_object = json.dumps(list, indent = 4) # creating a json object
with open("output.json", "w") as outfile: # file with given third argument is created with .json extension to store output
    outfile.write(json_object) # the list of dictionaries is written into this newly created json file


# In[ ]:


def is_pdf(url): #This function checks if the url is a pdf(Type-A) or a Type-B link
    parsed = urlparse(url)
    return bool(parsed.netloc) and bool(parsed.scheme)


# In[ ]:


def get_all_links(url): # returns all the urls of a page in case of Type-B url
    urls = set()
    # domain name of the URL without the protocol
    domain_name = urlparse(url).netloc
    soup = BeautifulSoup(requests.get(url).content, "html.parser")


# In[ ]:


for a_tag in soup.findAll("a"): # function to get all the pdf links present in the page in a Type-B url
    href = a_tag.attrs.get("href")
    if href == "" or href is None:
        continue


# In[ ]:


# code to encode characters from other languages to english (utf-8)
from bs4 import BeautifulSoup
markup = b"<h1>xedxe5xecxf9</h1>"
soup = BeautifulSoup(markup, 'html.parser', from_encoding="iso-8859-8")
print(soup.h1)
print(soup.original_encoding)

