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

from dataclean import scrape_element,get_url_content,get_subscribers,get_numberoffiles,get_package,get_wiki,get_submodules
from license_file  import  get_license
from print_file import print_file

g = Github(client_id="",client_secret="",per_page=100)
print("Rate remaining ",g.get_rate_limit().rate.remaining)







# -----
if __name__=='main':
    
    debug = open("debug.log", "w")
    outputfile = open("stats.csv", "w")
    outputfile.write("Organization,Name, URL, Forks_Count, Watchers_Count, Stargazers, Release Count, Branch Count, Commit Count, Contrib Count,License, LicenseText, ReadmeText, SubModules, PackageJSON, Patents \n")
    #orgs = ['apple','ibm','google','facebook','twitter','mozilla','twbs','github','jquery','h5bp','angular']
    #orgs = ['apple', 'ibm', 'google', 'facebook', 'twitter', 'mozilla', 'twbs', 'github', 'jquery', 'h5bp', 'angular']
    outputfile.close()
    debug.close()
    orgs = []

    for orgname in orgs:
        for repo in g.get_user(orgname).get_repos():
           #print(repo.name)
           #if(repo.name == 'FreeCAD-addons'):
            #print("Repo URL:", repo.url)
            # print("Repo watchers :", repo.watchers_count)
            # print("Repo stargazers: ", repo.stargazers_count)
            # print("Repo forks count : ", repo.forks_count)
            releases = repo.get_releases()
            relcount = 0
            branchcount = 0
            commitcount =0
            contribcount = 0
            watchers=0
            for rel in releases:
                relcount = relcount + 1;


        if (0):

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36"}
            url = "https://api.github.com/organizations?since="
            sincenum = 24600;
            while (sincenum):
                newurl = url + str(sincenum)
                response = UrlRequest.Request(newurl, headers=headers)
                result = UrlRequest.urlopen(response)
                data = result.read().decode('utf8')
                listofrepos = json.loads(data)
                if len(listofrepos) is 0:
                    sincenum = 0
                else:
                    for ijk in listofrepos:
                        print(ijk["login"])
                    sincenum = sincenum + 100
                #print("Since num", sincenum)
                #print("Rate remaining ", g.get_rate_limit().rate.remaining)

        # -----
    if (1):
        #print(
        #Organization,Name, URL, Forks_Count, Watchers_Count, Stargazers, Release Count, Branch Count, Commit Count, Contrib Count,License )
        # orgs = ['apple','ibm','google','facebook','twitter','mozilla','twbs','github','jquery','h5bp','angular']
        # orgs = ['apple', 'ibm', 'google', 'facebook', 'twitter', 'mozilla', 'twbs', 'github', 'jquery', 'h5bp', 'angular']
        orgs = ['apple']


        #for j in orgs:
        #    print(j)
        #filteredrepos=['azonenberg','FreeCAD']
        filteredrepos=[]
        deprepos=[];
        print("Started Collecting Stats.....")
        repoid=0
        urldict={}
        repodict={}
        #with open('Listofrepos', "r") as myfile:
        if(0):
         with open('Repos3', "r") as myfile:
            for line in myfile:
                lines=line.split("/")
                filteredrepos.append(lines[3])

                repoid=repoid+1
                deprepos.append(lines[4])
                repodict[lines[3]]=lines[4]
                key=lines[3]+"_"+lines[4]
                linestr = line.replace('\n', '')

                urldict[key]=linestr
                #print(lines[3]," ",lines[4])
        # modified on 01-11-2016 if (repo.name in ('FreeCAD-addons', 'openfpga')):
        #filteredrepos = ['azonenberg']
        #for k, v in urldict.items():
        #    print("Key ", k," Value ", v)
        if(0):
            orgrepos=[]
            repoid=0
            #print("Just before scraping",len(filteredrepos))
            filteredrepos=[]
            with open('orglist.main','r') as myfile:
                for line in myfile:
                    line=line.replace('\n','')
                    #if(re.match(r'^d',line)):
                    filteredrepos.append(line)

            for orgname in filteredrepos:
                try:
                    try:
                   #  print("Getting ",orgname)
                     orguser=g.get_user(orgname)
                    except HTTPError as e:
                     print("Error")
                    orgrepos=orguser.get_repos()
                    #orgrepos.append('activemq')
                except HTTPError as e:
                    print("Error")

            #for repo in orgrepos:
        for repo in g.get_repos(since=167170):
                #if(repo.name in ['activemq']):
                    print("Collecting stats for ",repo.id)
                    debug=open("debug.log","a")
                    outputfile = open("stats.csv", "a")
                    debug.write("Repo %s, UserName %s \n" %(repo.name,repo.owner.login))
                    relcount = 0
                    branchcount = 0
                    commitcount = 0
                    contribcount = 0
                    watcherscount=0

                    contents_url = repo.url + "/contents/"
                    packageyes= (get_package(contents_url))
                    raterem = g.get_rate_limit().rate.remaining
                    debug.write("Rate Limit %d \n" %(raterem))
                    if (int(raterem) < 500):
                        print("Sleeping......")
                        time.sleep(7200)
                    if(packageyes):
                        # Created date
                        print("Collecting STATS....")
                        releases = repo.get_releases()
                        created = repo.created_at
                        updated = repo.updated_at
                        size = repo.size
                        langlist = repo.get_languages()
                        languages = []
                        totalfiles = 0
                        for key in langlist.keys():
                            value=langlist[key]
                            #print(key," ",value)
                            languages.append(key)
                            totalfiles = totalfiles + int(value)

                        languages = ":".join(languages)
                        if(repo.forks_count > 1 and repo.fork == 0):
                            print("Getting Releases ")
                            for rel in releases:
                                relcount = relcount + 1;
                            for branches in repo.get_branches():
                                branchcount = branchcount + 1;
                            print("Getting Contributors")
                            for contrib in repo.get_contributors():
                                contribcount = contribcount + 1;

                            for commits in repo.get_commits():
                                commitcount = commitcount + 1;
                            watcherscount=get_subscribers(repo.url)
                            print("LICENSE")
                            glicense=""
                            licensefiles=""
                            glicense,licensefiles = get_license(repo.url)
                            print("DEPS")
                            dependsonpatents,listofpatents=get_wiki(repo.owner.login,repo.name)
                            print("After WIKI")
                            wikitext=[]
                            wikitextfull=""
                            if (os.path.isfile(dependsonpatents)):

                                with open(dependsonpatents, "r", encoding="utf8") as myfile:

                                    for line in myfile:
                                        line = re.sub('[^a-zA-Z0-9\.]', ' ', line)
                                        line = re.sub('\s+', ' ', line)
                                        line.strip()
                                        wikitext.append(line)
                            wikitextfull = " ".join(wikitext)
                            wikitextfull= (wikitextfull[:32000] + '..') if len(wikitextfull) > 32000 else wikitextfull
                            readmetext=[]
                            readmetext1=""
                            gitmodules=[]
                            packagejson=[]
                            dependentrepos =(get_submodules(contents_url))
                            print("Printing DEPS")
                            if(type(dependentrepos) == type(list()) and (len(dependentrepos) > 0)):
                             for i in dependentrepos:

                                if('README' in i):
                                    print("printing README")
                                    with open(i, "r",encoding="utf8") as myfile:
                                        for line in myfile:
                                            line = re.sub('[^a-zA-Z0-9\.]', ' ', line)
                                            line = re.sub('\s+', ' ', line)
                                            line.strip()
                                            readmetext.append(line)
                                    readmetext1=" ".join(readmetext)
                                    readmetext1=(readmetext1[:32000] + '..') if len(readmetext1) > 32000 else readmetext1

                                if ('modules' in i):
                                    print("printing MODULES")
                                    with open(i, "r") as myfile:
                                        for line in myfile:
                                            line = re.sub('[^a-zA-Z0-9\/\.]', ' ', line)
                                            line = re.sub('\s+', ' ', line)
                                            line.strip()
                                            gitmodules.append(line)
                                    gitmodules = " ".join(gitmodules)
                                    gitmodules = (gitmodules[:32000] + '..') if len(gitmodules) > 32000 else gitmodules
                                if ('package' in i):
                                    print("printing PACKAGE")
                                    if (os.path.isfile(i)):
                                        with open(i, "r") as myfile:
                                            for line in myfile:
                                                line = re.sub('[^a-zA-Z0-9\/\.]', ' ', line)
                                                line = re.sub('\s+', ' ', line)
                                                line.strip()
                                                packagejson.append(line)
                                        packagejson=" ".join(packagejson)
                                        packagejson = (packagejson[:32000] + '..') if len(packagejson) > 32000 else packagejson
                            licensetext = []
                            glicense.strip()
                            if(os.path.isfile(licensefiles)):

                                with codecs.open(licensefiles,"r",encoding="utf8") as myfile:

                                    for line in myfile:
                                        line = re.sub('[^a-zA-Z0-9\.]', ' ', line)
                                        line = re.sub('\s+', ' ', line)
                                        line.strip()
                                        licensetext.append(line)
                                licensetext=" ".join(licensetext)
                                licensetext = (licensetext[:32000] + '..') if len(licensetext) > 32000 else licensetext
                            apps_using = []

                            totalfiles = get_numberoffiles(contents_url, 0)
                            print("Printing stat file\n")
                            outputfile.write("%s,%s,%s,%d,%d," %(repo.owner.login,repo.name,repo.html_url,repo.forks_count,watcherscount))
                            outputfile.write("%d,%d,%d,%d,%d," %(repo.stargazers_count, relcount, branchcount, commitcount, contribcount))
                            outputfile.write("%s,%s,%d,%s,%d,%s,\"%s\",\"%s\"" %(str(created),str(updated),size,languages,totalfiles,glicense,licensetext,readmetext1))
                            outputfile.write("\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\n" %(gitmodules, packagejson,wikitextfull,''.join(listofpatents),apps_using))
                            debug.close()
                            outputfile.close()
                            
        repoid=repoid+1

  






