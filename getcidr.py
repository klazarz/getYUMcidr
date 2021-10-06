#!/usr/bin/env python3
import socket
from bs4 import BeautifulSoup
import requests


# List of OCI IP with CID https://docs.oracle.com/en-us/iaas/tools/public_ip_ranges.json
# YUM endpoints https://docs.oracle.com/en-us/iaas/Content/General/Concepts/addressranges.htm#yum-endpoints

# read from input .txt
# with open('yum_repos.txt') as f:
#     for line in f:
#         line = f.readline().strip()
#         IPAddr = socket.gethostbyname(line)  
#         CIDRAddr = IPAddr + '/32'
#         print (line[4:-11],',',CIDRAddr,',','YUM')        

# read from https://docs.oracle.com/en-us/iaas/Content/General/Concepts/addressranges.htm

url = 'https://docs.oracle.com/en-us/iaas/Content/General/Concepts/addressranges.htm'

html_content = requests.get(url).text

soup = BeautifulSoup(html_content, "lxml")

table = soup.find("table", {"summary":"Regional endpoints for the YUM repositories."})

endpoints=list()
for endpoint in table.find_all("td"):
    form_endpoint = endpoint.text[8:].strip()
    # print(form_endpoint)
    IPAddr = socket.gethostbyname(form_endpoint)  
    CIDRAddr = IPAddr + '/32'
    print (form_endpoint[4:-11],',',CIDRAddr,',','YUM')     



