import requests

def request():
    r = requests.get("https://ca.pcpartpicker.com/product/gBWfrH/msi-b450i-gaming-plus-ac-mini-itx-am4-motherboard-b450i-gaming-plus-ac")
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
