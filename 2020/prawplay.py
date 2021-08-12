import os

import praw

creds = {
    "id":"sOQ3dAfz4xy37g",
    "secret":"	Kd-_G8wM1FHJy2SuAktQ6nEe4SA",
    "password":os.environ['reddit'],
    "agent":"comment pickler (by /u/fomenig)",
    "uname":"fomenig",
    "uri":"http://localhost:8080",
}
reddit = praw.Reddit(
    client_id=creds['id'],
    client_secret=creds['secret'],
    password=creds['password'],
    user_agent=creds['agent'],
    username=creds['uname'],
    # redirect_uri=creds['uri'],
)
print(reddit.user.me())   
# print(reddit.auth.url(["identity"], "...", "permanent"))          