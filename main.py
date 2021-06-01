import time
import os
from pypresence import Presence

if os.name == 'nt':
   os.system('title DiscordRPC - https://github.com/dylandevzzz/discordrpc_py') # sets status title to

application = int(input("Application ID: "))

rpc = Presence(application)
rpc.connect()
details = input("Details: ")
state = input("State: ")
limg = input("Large Image Name: ")
simg = input("Small Image Name: ")
txt = input("Large Image Text: ")
rpc.update(details=details, state=state, large_image=limg, small_image=simg, large_text=txt)
while True:
    time.sleep(0.5)