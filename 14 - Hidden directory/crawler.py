import requests
import re
import os

def recursive(url):
    os.system("curl " + url + "README")
    suffix = get_info(url)
    for i in suffix:
        recursive(url + i + "/")

def get_info(url):
    i = 4
    liste = list()
    r = requests.get(url)
    html_content = r.text
    result = str(html_content).split("\n")
    while i < len(result) and len(result) > 9:
        liste.append(result[i][9:35])
        i +=1
    return (liste)

recursive("http://10.12.1.107/.hidden/")
