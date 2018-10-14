#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: anand
"""
from __future__ import print_function
from github import Github
import urllib,json
import codecs
import urllib.request as UrlRequest
import requests
import base64
from urllib.error import URLError, HTTPError
import re
from bs4 import BeautifulSoup,SoupStrainer
import os
import time
username=b'yyyyyyyyyy'
password=b'xxxxxxxxxx'
base64string = base64.b64encode(username + b":" + password)



def get_license(repo_url):
    headers = {"Authorization": b" Basic " + base64.b64encode(username + b":" + password),
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
    newurl = repo_url+"/license"
    response = UrlRequest.Request(newurl, headers=headers)
    glicense=""
    licensefiles=""
    debug = open("debug.log", "a")
    try:
        result = UrlRequest.urlopen(response)
        data = result.read().decode('utf8')
        repo = json.loads(data)
        if(repo['license']):
                if(repo['license']['name']):
                    glicense=repo['license']['name']
                if(repo['download_url']):
                    licencef=UrlRequest.urlopen(repo['download_url'])
#                    print("Licese")
                    licensefiles=repo_url

                    jnk=re.sub("https:\/\/api.github.com\/repos\/","",licensefiles)
 #                   print(jnk)
                    licensefiles=re.sub("\/","_",jnk) +"_License.txt"
  #                  print(licensefiles)
                    #print("Charater set")
                    #print(licencef.info().get_content_charset())
                    licencef=licencef.read().decode(licencef.info().get_content_charset(),errors='ignore')
                    #print(licencef)
                    line = re.sub('[^a-zA-Z0-9\.]', ' ', licencef)
                    line = re.sub('\s+', ' ', line)
                    #print(line)
                    with open(licensefiles,'w') as output:
                        output.write(line)


    except HTTPError as e:
        debug.write("Error: License Link Doesnt Work %s \n" % repo_url)
        glicense=""
    debug.close()
    return glicense,licensefiles;
