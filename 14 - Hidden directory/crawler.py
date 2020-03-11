import requests
import re
import os

def get_info(url):
    i = 4
    liste = list()
    r = requests.get(url)
    html_content = r.text
    result = str(html_content).split("\n")
    if len(result) < 34:
        return (liste)
    while i < 30:
        liste.append(result[i][9:35])
        i+=1
    return (liste)

def recursive(url):
    suffix = get_info(url)
    os.system("curl " + url + "README")
    for i in suffix:
        recursive(url + i + "/")

recursive("http://10.12.1.107/.hidden/")
