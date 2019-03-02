import json
from os.path import basename
import os

url = "https://s.crypko.ai/u/"
json_url = "https://api.crypko.ai/users/"

json_folder = "./json/"

folder_contents = os.listdir(json_folder) # returns contents of json folder

address_list = []

# enumerate over the json files to get usernames
for json_file in folder_contents:
    with open(json_folder + "/" + json_file, "r") as f:
        address = json.loads(f.read())["ownerAddr"]
        if address not in address_list:
            address_list.append(address)
    
with open("unique_addresses.txt", "w") as f:
    l = ""
    for address in address_list:
        l += (address + "\n")
    f.write(l)
