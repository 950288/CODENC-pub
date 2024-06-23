import time
import requests
import traceback
import json

headers = {
    "accept": "application/json",
    "accept-language": "en-GB,en;q=0.9,en-US;q=0.8,zh-CN;q=0.7,zh;q=0.6",
    "content-type": "application/json",
}

offset = 0
numRecords = 50
list = set()
while 1:
    body = {
    "searchText": "\"transcription factor\"",
    "pagination": {"offset": offset, "numRecords": numRecords},
    "documentTypeFilter":{"documentType":"gene","foundOnlyInFields":[]},
    "restrictToProject": "FungiDB",
    "restrictSearchToOrganisms": ["Fusarium fujikuroi IMI 58289"]
    }

    try:
        response = requests.post("https://fungidb.org/site-search/", headers=headers, data=json.dumps(body))

    except:
        traceback.print_exc()
        time.sleep(10)
        continue

    # The response of the request is available in the .json() method of the response object
    data = response.json()["searchResults"]["documents"]

    totalCount = response.json()["searchResults"]["totalCount"]

    if len(data) == 0:
        break

    for i in data:
        list.add(i["wdkPrimaryKeyString"])


    offset += numRecords
    print(f"{len(list)}/{totalCount}")

# save the list to a file
with open("fungi.txt", "w") as f:
    for i in list:
        f.write(i + "\n")

    print("Saved to fungi.txt")




