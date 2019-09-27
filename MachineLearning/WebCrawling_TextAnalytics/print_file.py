#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 01:18:56 2018

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

def print_file(download_url,repourl,appendname):
                    licencef=UrlRequest.urlopen(download_url)

                    licensefiles=repourl
#                    licencef=licencef.read().decode(licencef.info().get_content_charset())
                    licencef=licencef.read().decode(licencef.info().get_content_charset(),errors='ignore')

                    line = re.sub('[^a-zA-Z0-9\/\"\:\,\[\}\]\{\-\.]', ' ', licencef)
                    line = re.sub('\s+', ' ', line)
                    #line=licencef
                    jnk=re.sub("https:\/\/api.github.com\/repos\/","",licensefiles)
                    jnk=jnk.split("/")
     #               print(jnk)
                    licensefiles=jnk[0]+"_"+jnk[1] +"_"+appendname+".txt"
      #              print(licensefiles)
                    with open(licensefiles,'w') as output:
                         output.write(line)
                    return(licensefiles)
                    #Changed it from filename to content
                    #return(licencef.read())