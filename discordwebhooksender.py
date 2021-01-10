#import requests
import requests

#input by user
discordwebhook = input("Discord Webhook : ")
discordwebhookcontent = input("Content : ")
discordwebhookusername = input("Username : ")
discordwebhookpictureurl = input("Profile Picture URL : ")

#define url
url = discordwebhook

#packet
data = {
    "content" : discordwebhookcontent,
    "username" : discordwebhookusername,
    "avatar_url" : discordwebhookpictureurl
}


#Post data to url
requests.post(url, data)


print("Done ! Made by Tino.")
