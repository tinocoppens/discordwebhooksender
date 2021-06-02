import requests
discordwebhook = input("Discord Webhook : ")
discordwebhookcontent = input("Content : ")
discordwebhookusername = input("Username : ")
discordwebhookpictureurl = input("Profile Picture URL : ")
data = {"content" : discordwebhookcontent, "username" : discordwebhookusername, "avatar_url" : discordwebhookpictureurl}
requests.post(discordwebhook, data)

