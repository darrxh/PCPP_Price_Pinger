from requests import get
from bs4 import BeautifulSoup
from json import dumps, load
from time import sleep
from simpleaudio import WaveObject
regions = ["au", "be", "ca", "de", "es", "fr", "se","in", "ie", "it", "nz", "uk", "us"]

class Component:
    def __init__(self):
        self.url = ""
        self.name = self.title_fetcher()

    def title_fetcher(self):
        new_request = get(self.url)
        new_request = BeautifulSoup(new_request.text, "html.parser")
        return new_request.find("h1", class_="pageTitle").string


class Config:
    def __init__(self):
        self.interval = 3600
        self.component_list = []
        self.region = ""

def request():
    r = get(url)
    print (r.text)
    print (r.headers)

#function returns boolean True or False based on server status for each URL
def clear_status(part_list):
    for each_part in part_list:
        print ("Returned error")
        return False
    print ("Returned okay")
    return True

def input_url():
    url_list = []
    while True:
        print ("Input URL, type/enter x to finish. \n")
        new_part = input(str())
        if (new_part == "x"):
            break
        url_list.append(new_part)
    print ("Total number of URLs inputted: {}".format(len(url_list)))
    return url_list

list = input_url()
clear_status(list)
