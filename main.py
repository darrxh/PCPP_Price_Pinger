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

def get_status_list(html_object):
    status_list = []
    retailer_table = html_object.find("table", class_="xs-col-12")
    retailer_list = retailer_table.findall("tr")
    for each_retailer in retailer_list:
        retailer_dict = dict()
        price_string = retailer_list.find("a",class_="pp_async_mr").string
        retailer_dict["price"] = int(price_string[1:])
        retailer_list["name"] = retailer_list.find("td",class_="td__logo")
        retailer_list["url"] = retailer_list.find("td",class_"td__buy").find("a", href=True)
        try:
            retailer_list["stock"] = retailer_list.find("td",class_="td__availability td__availability--outOfStock")
        except Exception:
            retailer_list["stock"] = retailer_list.find("td",class_="td__availability td__availability--inStock")
        status_list.append(retailer_dict)
    return status_list

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

def main():
    command_dict = {"add": add_component,
                    "del": del_component,
                    "update": quick_check,
                    "newconfig": start_new,
                    "start": start,
                    "stop": stop,
                    "help": print_manual}

    while True:
        print (f"{colour.default} -------------------------")
        user_input = input()
        print (f"{colour.default} -------------------------")
        if (user_input in command_dict.keys()):
            command_dict[user_input]()
        elif (user_input == "exit"):
            stop()
            print(f"{colour.red} Program exiting. {colour.default}")
            break
        elif (user_input == ""):
            print (f"{colour.default}\n")
        else:
            print (f"{colour.error} Unknown command. {colour.default}")

if __name__ == '__main__':
    main()