#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 00:15:05 2018

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

def scrape_element(url,whatfor,endat,level):
    #print("Scrape Level")
    #print(level)

    response = UrlRequest.Request(url)
    endlist=[]
    if (level == 3):
        return endlist
    try:
        result = UrlRequest.urlopen(response)
        soup= BeautifulSoup(result.read(),"html.parser")
        linklist=soup.find_all('a')
        uniquelist=[]

        for link in linklist:
         hreflink=link.get('href')
        # print("LINK IS ",hreflink)
         if(hreflink is not None):
             if((link.get('href')).find('www.') == -1):
                fulllink = ("https://github.com" + link.get('href'))
             else:
                 fulllink = link.get('href')
        #     print(fulllink)
             if(fulllink not in uniquelist):
                uniquelist.append(fulllink)
        # print("Length of Unique List")
        # print(len(linklist))
        # print(len(uniquelist))
        for link in uniquelist:
         fulllink=link
         if (endat in fulllink):
             #print("PATENTS")
             #print(fulllink)
             endlist.append(fulllink)
         else:
            if (whatfor in fulllink):
                if((fulllink.find('return_to') == -1) and (fulllink.find('history') == -1)):
                    #print("Next Level of Scraping")
                    #print(fulllink)
                    endlist=endlist+(scrape_element(fulllink,whatfor,endat,level+1))


            # for table in soup.find_all('table'):
            #  for tbody in table.find_all('tbody'):
            #     for tr in tbody.find_all('tr'):
    except HTTPError as e:
        print("Error")
    #print(endlist)
    return (endlist)



def get_wiki(username,reponame):
   # headers = {"Authorization": b" Basic " + base64.b64encode(username + b":" + password),
   #            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
   debug = open("debug.log", "a")
   url="https://github.com/"+username+"/"+reponame+"/wiki"
    #response = UrlRequest.Request(url, headers=headers)
   response = UrlRequest.Request(url)
   listelements=[]
   listelements=scrape_element(url,"Patent","www.google.com/patents",0)
   uniquelist=[]
   #print(listelements)
   for element in listelements:
       if(element not in uniquelist):
           uniquelist.append(element)
   #print (uniquelist)
   try:
        result = UrlRequest.urlopen(response)
        #Convert the html text into proper text
        # soup = BeautifulSoup(result.read(),"html.parser")
        # [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
        # text=soup.get_text()
        # lines = (line.strip() for line in text.splitlines())
        # chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        # text = ' '.join(chunk for chunk in chunks if chunk)
        #print(text.encode('utf-8'))

        filename=username+"_"+reponame+"_wiki.txt"
        with open(filename, 'wb') as output:
            output.write(result.read())
   except HTTPError as e:
             debug.write("Error: WikiLink doesnt work %s %s \n " %(reponame,username))
   debug.close()
   return (filename,uniquelist)

def get_url_content(url_for_scrape,username,reponame):
    try:
        response = UrlRequest.Request(url_for_scrape)
        result = UrlRequest.urlopen(response)
        # Convert the html text into proper text
        soup = BeautifulSoup(result.read(), "html.parser")
        [s.extract() for s in soup(['style', 'script', '[document]', 'head', 'title'])]
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        # print(text.encode('utf-8'))
        filename = username + "_" + reponame + "_scrape.txt"
        with open(filename, 'wb') as output:
            output.write(bytes(text, 'utf-8'))
        return filename
    except HTTPError as e:
        print("Error")
        
def get_subscribers(url):
    headers = {"Authorization": b" Basic " + base64.b64encode(username + b":" + password),
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
    newurl = url
    #print(newurl)
    response = UrlRequest.Request(newurl, headers=headers)
    try:
        result = UrlRequest.urlopen(response)
        data = result.read().decode('utf8')
        repo = json.loads(data)
        return repo['subscribers_count']
    except HTTPError as e:
        print("Error")


def get_numberoffiles(contents_url,level):
    headers = {"Authorization": b" Basic " + base64.b64encode(username + b":" + password),
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
    newurl = contents_url
    debug = open("debug.log", "a")

    deplist = 0
    response = UrlRequest.Request(newurl, headers=headers)
    debug.write("Number of Files %s %d" %(contents_url,level))
    if (level > 3):
        return
    try:
        result = UrlRequest.urlopen(response)
        data = result.read().decode('utf8')
        repo = json.loads(data)
        for sub in repo:
            #   print(sub['type'])
            if (sub['type'] == 'file'):
                #         print("Trying to get README")
                deplist = deplist + 1
                #    print("success")
            if (sub['type'] == 'dir'):
                newcontents_url = sub['url']
                t = get_numberoffiles(newcontents_url, level + 1)
                if (type(t) == type(int)):
                    deplist = deplist + t
        debug.close()
        return (deplist)
    except HTTPError as e:
        debug.write("Error: Number of Files didn't work %s \n" % contents_url)

    debug.close()
    return(0)
def get_package(contents_url):
    headers = {"Authorization": b" Basic " + base64.b64encode(username + b":" + password),
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
    newurl = contents_url
    deplist=[]
    debug = open("debug.log", "a")
    response = UrlRequest.Request(newurl, headers=headers)
    try:
        result = UrlRequest.urlopen(response)
        data = result.read().decode('utf8')
        repo = json.loads(data)

        # if('type' in repo):
        #     if (repo['type'] == 'submodule'):
        #         print("success")
        # else:
        #
        for sub in repo:
             #print(sub['name'])
             if (sub['name'] == 'package.json'):
            #       print("Trying to get PACKAGE")
             #    deplist.append(print_file(sub['download_url'], contents_url, "package"))
                 #print("success")
        #     else:
        #         new_url=sub['url']
        #         get_submodules(new_url)
        #

                return(1)
    except HTTPError as e:
        debug.write("Error: Package Link Doesnt Work %s \n" % contents_url)
     #   glicense = ""
    #return (glicense)
    debug.close()
    return(0)

def get_submodules(contents_url):
    headers = {"Authorization": b" Basic " + base64.b64encode(username + b":" + password),
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
    newurl = contents_url
    deplist=[]
    debug = open("debug.log", "a")
    response = UrlRequest.Request(newurl, headers=headers)
    try:
        result = UrlRequest.urlopen(response)
        data = result.read().decode('utf8')
        repo = json.loads(data)

        # if('type' in repo):
        #     if (repo['type'] == 'submodule'):
        #         print("success")
        # else:
        #
        for sub in repo:
             if (sub['name'] == '.gitmodules'):
           #      print("Trying to get gitmodules")
                 deplist.append(print_file(sub['download_url'],contents_url,"gitmodules"))
                 #print("success")
             if ('README' in sub['name'] and 'pdf' not in sub['name']):
                 if(sub['type'] == 'file'):
         #         print("Trying to get README")
                  deplist.append(print_file(sub['download_url'], contents_url, "README"))
                 #print("success")
             if (sub['name'] == 'package.json'):
          #       print("Trying to get PACKAGE")
                 deplist.append(print_file(sub['download_url'], contents_url, "package"))
                 #print("success")
        #     else:
        #         new_url=sub['url']
        #         get_submodules(new_url)
        #

        return(deplist)
    except HTTPError as e:
        debug.write("Error: Submodules Link Doesnt Work %s \n " % contents_url)
     #   glicense = ""
    #return (glicense)
    debug.close()
