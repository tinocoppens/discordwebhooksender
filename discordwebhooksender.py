#you need
#-python3
#-requests (pip install requests)





#import requests
import requests

#input by user
discordwebhook = input("Discord Webhook : ")
discordwebhookcontent = input("Content : ")
discordwebhookusername = input("Username : ")
discordwebhookpictureurl = input("Profile Picture URL : ")

#define url
url = discordwebhook

#for post req
data = {
    "content" : discordwebhookcontent,
    "username" : discordwebhookusername,
    "avatar_url" : discordwebhookpictureurl
}


#send post request to discord api
requests.post(url, data)


print("Done ! Made by Tino.")
