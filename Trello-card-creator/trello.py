import os, json
import urllib3
from datetime import datetime
url = 'https://api.trello.com/1/'
api_key = "your_api_key"
api_token = "your_api_token"
auth = 'key={' + api_key + '}&token={' + api_token + '}'
print(auth)



#Getting boards from trello
curlOutputfile = open("output.txt", "w+")
os.system("curl " + "'" + url + "members/me/boards?key={" + api_key + "}&token={" + api_token + "}' > output.txt") #Output will be written to output.txt

#Reading into a txt file and creating a dictionart out of it
rawString = curlOutputfile.read()
dictionary = json.loads(rawString)


#Getting board ID
boardId = 0
for board in dictionary:
    if(board.get("name") == "your_board_name"):
        boardId = board.get("id")

curlOutputfile.close()

#Sending api a GET request to get the lists
os.system("curl " + "'" + url + "boards/" + boardId + "/lists?" + auth + "' > output.txt")

#Reading into a txt file and creating a dictionart out of it
curlOutputfile = open("output.txt", "r")
rawString = curlOutputfile.read()
dictionary = json.loads(rawString)

#Getting list ID
listID = 0
for lists in dictionary:
    if(lists.get("name") == "your_list_name"):
        listID = lists.get("id")


#Some description
date = str(datetime.now().strftime("%H:%M:%S"))

#forming the url
idList = "idList="+str(listID)+"&"
payload = idList + "name=test&desc=" + date + "&" + auth
payloadFinalURL = url + "cards?" + payload

#Sending post request to create new card into the list
os.system("curl -X POST '" + payloadFinalURL+"'")


curlOutputfile.close()