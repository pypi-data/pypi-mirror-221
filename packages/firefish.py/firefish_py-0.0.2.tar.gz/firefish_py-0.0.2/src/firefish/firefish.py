import os
import requests
from dotenv import load_dotenv
load_dotenv()

token = os.getenv('TOKEN')
instance = os.getenv('INSTANCE')
headers = {
 'Authorization': 'Bearer ' + token,
}

#Post/Note-related
#Create a note
def createnote(t, i):

 if 'i' == 'null':

  json_data = {
  'text': t,
  }


 else:
  json_data = {
  'text': t,
  'fileId': i,
  }

 global response
 response = requests.post('https://' + instance + '/api/notes/create', headers=headers, json=json_data)
 print(response)


#Edit a note
def editnote(i, t):

 json_data = {
 'text': t,
 'editId': i,
 }


 global response
 response = requests.post('https://' + instance + '/api/notes/edit', headers=headers, json=json_data)
 print(response)

#Delete a note
def deletenote(i):


 json_data = {
 'noteId': i,
 }


 global response
 response = requests.post('https://' + instance + '/api/notes/delete', headers=headers, json=json_data)
 print(response)



#Messaging-related

#Get  messages sent by a user
def messages(i, l):

 json_data = {
 'userId': i,
 'limit': l,
 }


 global response
 response = requests.post('https://' + instance + '/api/messaging/messages', headers=headers, json=json_data)
 print(response)

#Send a message
def createmessage(i, t, f):

 if 'f' == 'null':

  json_data = {
  'userId': i,
  'text': t,
  }


 else:
  json_data = {
  'userId': i,
  'text': t,
  'fileId': f,
  }

 global response
 response = requests.post('https://' + instance + '/api/messaging/messages/create', headers=headers, json=json_data)
 print(response)



#Search-related

#Search for users
def searchuser(q, l):

 json_data = {
 'query': q,
 'limit': int(l),
 }

 global response
 response = requests.post('https://' + instance + '/api/users/search', headers=headers, json=json_data)
 print(response)

#Search for users by username and host
def searchuserbyhost(u, h, l):

 json_data = {
 'username': u,
 'host': h,
 'limit': int(l),
 }

 global response
 response = requests.post('https://' + instance + '/api/users/search-by-username-and-host', headers=headers, json=json_data)
 print(response)

#Search for notes
def searchnote(q, l):

 json_data = {
 'query': q,
 'limit': int(l),
 }

 global response
 response = requests.post('https://' + instance + '/api/notes/search', headers=headers, json=json_data)
 print(response)

#Search for (hash)tags
def searchtag(q, l):

 json_data = {
 'query': q,
 'limit': int(l),
 }

 global response
 response = requests.post('https://' + instance + '/api/hashtags/search', headers=headers, json=json_data)
 print(response)


#Drive-related

#Upload local file to drive
def createfile(f, i, n, c):

 files = {
  'file': open(f, 'rb'),
 }


 json_data = {
 'folderId': i, #nullable
 'name': n, #nullable
 'comment': c #nullable
 }

 global response
 response = requests.post('https://' + instance + '/api/drive/files/create', headers=headers, json=json_data, files=files)
 print(response)

